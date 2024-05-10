import os
from datetime import datetime
from supabase import Client

class SupabaseService:
    def __init__(self, client: Client) -> None:
        self._client = client

    def auth(method):
        def wrapper(self):
            self._client.auth.sign_in_with_password({"email":os.environ["EMAIL"], "password":os.environ["PASSWORD"]})
            result = method(self)
            print("Sign out")
            self._client.sign_out()
            return result
        return wrapper    
    
    @auth
    def stocks(self) -> list[str]:
        table = self._client.table("stocks").select("name").execute()
        return list(map(lambda x: x["name"], table.data))
    
    @auth
    def last_update(self, stock_name: str) -> None | datetime:
        responde = self._client.table("stocks").select("last_update").eq("name",stock_name).execute()
        date = responde.data[0]["last_update"]
        return None if date == None else datetime.strptime(date, '%Y-%m-%d')

    @auth
    def insert(self, table: str, data: dict) -> None:
        try:
            self._client.table(table).insert(data).execute()
        except:
            raise Exception(f"Invalid insert in {table}.")
    
    @auth
    def update_changes(self,  stock_name: str) -> None:
        self._client.auth.sign_in_with_password({"email":os.environ["EMAIL"], "password":os.environ["PASSWORD"]})
        last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._client.table("stocks").update({"last_update": last_update}).eq("name", stock_name).execute()
        self._client.sign_out()
