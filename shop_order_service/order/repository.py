from rest_framework.response import Response
from rest_framework import status
import requests
import jwt
from datetime import datetime, timedelta

domain = '127.0.0.1:8000'


def get_product(product_id, domain=domain):

    try:
        product_url = f'http://{domain}/api/product-detail/{product_id}'
        response = requests.get(product_url)
    except ConnectionError as c:
        return Response({'detail': f'No connection with {product_url}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if response.status_code == 200:
            return response  # .json()
        return Response({'detail': 'No products'}, status=status.HTTP_404_NOT_FOUND)


def get_user_auth(data=[]):

    if not data:
        return Response({'detail': 'No credentials provided'}, status=status.HTTP_404_NOT_FOUND)
    try:
        login_url = 'http://127.0.0.1:8002/user/dj-rest-auth/login/'
        response = requests.post(login_url, data=data)
    except:
        return Response({'detail': f'No connection with {login_url}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if response.status_code == 200:
            token = response.json()['access']
            paylod = jwt.decode(token, key='secret', algorithms=['HS256'], verify=False,  options={'verify_signature': False})
            print('Token payload: ', paylod)
            headers = {"Authorization": f"Bearer {token}"}
            data_url = 'http://127.0.0.1:8002//user/dj-rest-auth/user/'
            response = requests.get(data_url, headers=headers)
            return response
        return  Response({'detail': 'No user found with this credentials'}, status=status.HTTP_404_NOT_FOUND)
