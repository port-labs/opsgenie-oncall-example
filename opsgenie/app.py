## Import the needed libraries
import requests
from decouple import config


# Get environment variables using the config object or os.environ["KEY"]
# These are the credentials passed by the variables of your pipeline to your tasks and in to your env
OPSGENIE_API_KEY = config("OPSGENIE_API_KEY")
CLIENT_ID = config("PORT_CLIENT_ID")
CLIENT_SECRET = config("PORT_CLIENT_SECRET")
OPSGENIE_API_URL = "https://api.opsgenie.com/v2"
PORT_API_URL = "https://api.getport.io/v1"


## Get Access Token
credentials = {'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET}
token_response = requests.post(f'{PORT_API_URL}/auth/access_token', json=credentials)
access_token = token_response.json()['accessToken']

# You can now use the value in access_token when making further requests
headers = {
	'Authorization': f'Bearer {access_token}'
}
blueprint_id = 'service'


def add_entity_to_port(entity_object):
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
    response = requests.post(f'{PORT_API_URL}/blueprints/{blueprint_id}/entities?upsert=true&merge=true', json=entity_object, headers=headers)
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
                "properties": {
                    "on_call_user": user["name"] if user["type"] == "user" else "developer@getport.io",
                    "on_call_team": user["name"] if ((user["type"] == "team") or (user["type"] == "escalation")) else "Developer Team"
                },
                "relations": {}
                }
            add_entity_to_port(entity)

retrieve_oncall_users()