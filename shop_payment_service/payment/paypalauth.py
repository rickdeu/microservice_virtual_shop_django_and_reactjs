from shop_payment_service import settings
import base64
import requests
from rest_framework.response import Response
from rest_framework import status


def paypalToken(client_secret=settings.SECRET_KEY_PAYPAL, client_id=settings.CLIENT_ID):
    url = 'https://api-m.sandbox.paypal.com/v1/oauth2/token'
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic {0}".format(base64.b64encode((client_id + ":" + client_secret).encode()).decode())
    }
    response = requests.post(url, data, headers=headers)
    return response.json()['access_token']

def get_user_auth(token):
    if not token:
        return Response({'detail': 'No credentials provided'}, status=status.HTTP_404_NOT_FOUND)
    try:
        #paylod = jwt.decode(token, key='secret', algorithms=['HS256'], verify=False,  options={'verify_signature': False})
        headers = {"Authorization": f"Bearer {token}"}
        data_url = 'http://127.0.0.1:8002//user/dj-rest-auth/user/'
        response = requests.get(data_url, headers=headers)

    except:
        return Response({'detail': f'No connection with '}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        if response.status_code == 200:
            return response
    return  Response({'detail': 'No user found with this credentials'}, status=status.HTTP_401_UNAUTHORIZED)


def login_user(email, password):
    if email is None and password is None:
            return Response({'detail': 'No credentials provided'}, status=status.HTTP_204_NO_CONTENT)
    try:
         response = requests.post('http://127.0.0.1:8002//user/dj-rest-auth/login/',data={'email':email, 'password':password})

    except ConnectionError as c:
            return Response({'detail': f'No connection'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if response.status_code == 200:
            return response
    return  Response({'detail': 'No user found with this credentials'}, status=status.HTTP_204_NO_CONTENT)



