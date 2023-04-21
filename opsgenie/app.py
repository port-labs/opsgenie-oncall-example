## Import the needed libraries
import requests
from decouple import config
import schedule
import time


# Get environment variables using the config object or os.environ["KEY"]
OPSGENIE_API_KEY = config("OPSGENIE_API_KEY")
PORT_WEBHOOK_URL = config("PORT_WEBHOOK_URL")
OPSGENIE_API_URL = "https://api.opsgenie.com/v2"


def add_entity_to_port_webhook(entity_object):
    """A function to create the passed entity in Port

    Params
    --------------
    entity_object: dict
        The entity to add in your Port catalog
    
    Returns
    --------------
    response: dict
        The response object after calling the webhook
    """
    response = requests.post(PORT_WEBHOOK_URL, json=entity_object)
    print(response.json())


def retrieve_oncall_users():
    """A function to make API request to OpsGenie's who is on call endpoint"""

    ## First, get OpsGenie Schedules
    headers = {'Authorization': f'GenieKey {OPSGENIE_API_KEY}'}
    schedule_response = requests.get(f'{OPSGENIE_API_URL}/schedules', headers=headers)
    schedules = schedule_response.json()['data']

    ## Iterate through the schedules and save all on-call users
    for schedule in schedules:
        on_call_response = requests.get(f'{OPSGENIE_API_URL}/schedules/{schedule["id"]}/on-calls', headers=headers)
        data = on_call_response.json()["data"]["onCallParticipants"]
        for user in data:
            entity = {
            "identifier": user["id"],
            "title": schedule["name"],
            "on_call": user["name"],
            "user_type": user["type"]
            }
            add_entity_to_port_webhook(entity)


# schedule the OpsGenie API call to be made every 60 minutes
schedule.every(5).minutes.do(retrieve_oncall_users)

# run the scheduler indefinitely while sleeping at 10 minutes interval to avoid exhaustive CPU consumption
while True:
    schedule.run_pending()
    time.sleep(1) 