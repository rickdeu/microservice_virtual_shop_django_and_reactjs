from rest_framework.response import Response
from rest_framework import status
import requests


def get_order(pk, token, data=None):
    if not token and pk == None:
        return Response({'detail': 'No credentials provided'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        order_url = f'http://127.0.0.1:8001/order-detail/{pk}/token={token}'
        if data is None:
            response = requests.get(order_url)
        response = requests.patch(order_url, data=data)
    except ConnectionError as c:
        return Response({'detail': f'No connection with {order_url}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if response.status_code == 200:
            return response 
    return Response({'detail': 'No order found'}, status=status.HTTP_404_NOT_FOUND)

