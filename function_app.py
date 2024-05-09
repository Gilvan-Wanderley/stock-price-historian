import logging
import os
import azure.functions as func
from supabase import create_client, Client


app = func.FunctionApp()

@app.schedule(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def trigger_24h(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    url = os.environ["URL"]
    key = os.environ["KEY"]
    client: Client = create_client(url, key)
    client.table("Test").insert({}).execute()
