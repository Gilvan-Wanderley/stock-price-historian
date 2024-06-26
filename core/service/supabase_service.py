from datetime import datetime
from supabase import Client

class SupabaseService:
    def __init__(self, client: Client, email: str, password: str) -> None:
        self._client = client
        self._email = email
        self._password = password

    def sign_out(self):
        self._client.auth.sign_out()

    def sign_in(self):
        self._client.auth.sign_in_with_password({"email":self._email, "password":self._password})

    def stocks(self) -> list[str]:        
        table = self._client.table("stocks").select("name").execute()
        return list(map(lambda x: x["name"], table.data))
    
    def last_update(self, stock_name: str) -> None | datetime:
        responde = self._client.table("stocks").select("last_update").eq("name",stock_name).execute()
        date = responde.data[0]["last_update"]
        return None if date == None else datetime.strptime(date, '%Y-%m-%d')

    def insert(self, table: str, data: dict) -> None:
        try:
            self._client.table(table).insert(data).execute()
        except:
            raise Exception(f"Invalid insert in {table}.")
    
    def update_changes(self,  stock_name: str) -> None:
        last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._client.table("stocks").update({"last_update": last_update}).eq("name", stock_name).execute()
