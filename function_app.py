import logging
import azure.functions as func
from core.injection_container import database, finance
from core.historian import Historian
from datetime import datetime

app = func.FunctionApp()

@app.schedule(schedule="0 30 23 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def trigger_24h(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    time = datetime.now()
    historian = Historian(database(), finance())
    historian.update_dbs(time)
    logging.info(f"{time} - Update!")
