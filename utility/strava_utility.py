import requests

auth_url = "https://www.strava.com/oauth/token"
# strava token renew
def renew_token():
    payload = {
        'client_id': "47979",
        'client_secret': 'e3938884e234926885109ba4726449f7e036be1a',
        'refresh_token': 'a0c2468b904c99aca9ad0d68f17c781304007e47',
        'grant_type': "refresh_token",
        'f': 'json'
    }
    print("Requesting Token...\n")
    res = requests.post(auth_url, data=payload, verify=False)
    try:
        access_token = res.json()['access_token']
    except :
        print("json.decoder.JSONDecodeError")
    print("Access Token = {}\n".format(access_token))
    return access_token