from rest_framework.response import Response
from rest_framework import status
import requests
from payment.autentication import paypalToken
from shop_payment_service.domain import paypal_url, order_detail_url


def get_order(pk, token, data=None):
    """Get order"""
    if not token and pk == None:
        return Response({'detail': 'No credentials provided'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        order_url = f'{order_detail_url}/{pk}/token={token}'
        if data is None:
            response = requests.get(order_url)
        response = requests.patch(order_url, data=data)
    except ConnectionError as c:
        return Response({'detail': f'No connection with {order_url}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if response.status_code == 200:
            return response
    return Response({'detail': 'No order found'}, status=status.HTTP_404_NOT_FOUND)


def paypal_payment(request):
    """payment order with paypal"""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {paypalToken()}',
    }
    try:
        response = requests.post(
            paypal_url, headers=headers, json=request.data)
    except ConnectionError as c:
        return Response({'detail': f'No connection'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        if response.status_code == 201:
            return response
    return Response({'detail': 'No order found'}, status=status.HTTP_404_NOT_FOUND)
