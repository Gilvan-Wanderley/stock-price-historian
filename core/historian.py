from datetime import datetime, timedelta
from .service import FinanceService, SupabaseService

class Historian:
    START_DATA = datetime(2022, 12, 31)

    def __init__(self, database: SupabaseService, finance: FinanceService) -> None:        
        self._database = database
        self._finance = finance

    def update_dbs(self, until: datetime):
        self._database.sign_in()
        for stock_name in self._database.stocks():
            last_update = self._database.last_update(stock_name=stock_name)
            last_update = self.START_DATA if last_update == None else last_update
            total_days = (until - last_update).days
            if total_days > 0:
                for day in range(1, total_days):
                    start = last_update + timedelta(days=day)
                    end = start + timedelta(days=1)
                    df = self._finance.history(stock_name, start, end)
                    if df is not None:
                        for index, row in df.iterrows():
                            data = self._finance.get_data(index, row) 
                            self._database.insert(stock_name, data)
            self._database.update_changes(stock_name)
        self._database.sign_out()