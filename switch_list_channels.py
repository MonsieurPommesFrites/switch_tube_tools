import requests

ORIGIN = 'https://tube.switch.ch'

# Insert your SWITCHtube token here
TOKEN = 'REPLACE_WITH_PERSONAL_TOKEN_STRING'

# Get channels and show their id and title.
response = requests.get(
    ORIGIN + '/api/v1/channels?role=contributor',
    headers={'Authorization': 'Token ' + TOKEN}
    )
for channel in response.json():
    print("{id}: {name}".format(id=channel['id'], name=channel['name']))