import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

def get_bearer(username, password):
    url = 'https://oauth.fatsecret.com/connect/token'
    client = BackendApplicationClient(client_id=username)
    oauth = OAuth2Session(client=client, scope='barcode')
    token = oauth.fetch_token(token_url=url,client_id=username,client_secret=password)
    print(token)
    return oauth

def get_food_id(oauth, barcode):
    url = 'https://platform.fatsecret.com/rest/server.api'
    headers={'Content-Type':'appplication/json'}
    params={'method':'food.find_id_for_barcode','barcode':barcode,'format':'json'}
    # r = requests.post(url, headers=headers, params=params, auth=oauth)
    r = oauth.post(url, headers=headers, params=params)
    print(r.json())

def main():
    from config import CLIENT_ID, SECRET_KEY
    oauth = get_bearer(CLIENT_ID, SECRET_KEY)
    get_food_id(oauth, '8714100868171')
if __name__ == '__main__':
    main()