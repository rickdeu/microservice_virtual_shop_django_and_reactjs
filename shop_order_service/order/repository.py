from rest_framework.response import Response
from rest_framework import status
import requests

domain = '127.0.0.1:8000'
def get_product(product_id, domain=domain):

    try:
        product_url = f'http://{domain}/api/product-detail/{product_id}'
    except ConnectionError as c:
        return Response({'detail': f'No connection with {product_url}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        response = requests.get(product_url)
        if response.status_code == 200:
            return response  # .json()
        return Response({'detail': 'No products'}, status=status.HTTP_404_NOT_FOUND)
