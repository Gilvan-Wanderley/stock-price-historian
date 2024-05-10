import os, yfinance
from supabase import create_client
from .service import FinanceService, SupabaseService

def database():
    return SupabaseService(create_client(os.environ["URL"], os.environ["KEY"]))

def finance():
    return FinanceService(yfinance.Ticker)