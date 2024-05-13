from datetime import datetime
from supabase import Client

class SupabaseMock:
    def stocks(self) -> list[str]:
        pass

    def last_update(self, stock_name: str) -> None | datetime:
        pass

    def insert(self, table: str, data: dict) -> None:
        pass

    def update_changes(self,  stock_name: str) -> None:
        pass