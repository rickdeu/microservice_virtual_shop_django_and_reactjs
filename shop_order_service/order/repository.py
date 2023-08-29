from rest_framework.response import Response
from rest_framework import status
import requests
from shop_order_service.domain import user_auth_url, product_detail_url


def get_product(product_id):

    try:
        product_url = f'{product_detail_url}/{product_id}'
        response = requests.get(product_url)
    except ConnectionError as c:
        return Response({'detail': f'No connection with {product_url}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if response.status_code == 200:
            return response  # .json()
        return Response({'detail': 'No products'}, status=status.HTTP_404_NOT_FOUND)


def login_user(email, password):
    if email is None and password is None:
            return Response({'detail': 'No credentials provided'}, status=status.HTTP_204_NO_CONTENT)
    try:
         response = requests.post(f'{user_auth_url}/login/',data={'email':email, 'password':password})

    except ConnectionError as c:
            return Response({'detail': f'No connection'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if response.status_code == 200:
            return response
    return  Response({'detail': 'No user found with this credentials'}, status=status.HTTP_204_NO_CONTENT)


def get_user_auth(token):
    if not token:
        return Response({'detail': 'No credentials provided'}, status=status.HTTP_404_NOT_FOUND)
    try:
        headers = {"Authorization": f"Bearer {token}"}
        data_url = f'{user_auth_url}/user/'
        response = requests.get(data_url, headers=headers)

    except:
        return Response({'detail': f'No connection with '}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        if response.status_code == 200:
            return response
    return  Response({'detail': 'No user found with this credentials'}, status=status.HTTP_401_UNAUTHORIZED)


