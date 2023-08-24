from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from payment.models import Payment
from payment import views
import json


class PaymentPayPalServiceAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse(views.PayPalPaymentServiceAPI.name)
        self.data = {
            "intent": "CAPTURE",
            "application_context": {
                "notify_url": "https://virtualshop.co.ao",
                "return_url": "https://virtualshop.co.ao/return",
                "cancel_url": "https://virtualshop.co.ao/cancel",
                "brand_name": "VIRTUAL SHOP",
                "landing_page": "BILLING",
                "shipping_preference": "NO_SHIPPING",
                "user_action": "CONTINUE"
            },
            "purchase_units": [
                {
                    "reference_id": "294375635",
                    "description": "TEST PAYMENT VIRTUAL SHOP",

                    "custom_id": "ANGOLA1",
                    "soft_descriptor": "VIRTUAL SHOP",
                    "amount": {
                        "currency_code": "USD",
                        "value": "200",
                        "breakdown": {
                            "item_total": {
                                    "currency_code": "USD",
                                    "value": "180.00"
                            },
                            "shipping": {
                                "currency_code": "USD",
                                "value": "20.00"
                            },


                        }

                    },
                }
            ],
            "items": [
                {
                    "name": "T-Shirt",
                    "description": "Green XL",
                    "sku": "sku01",
                    "unit_amount": {
                        "currency_code": "USD",
                        "value": "90.00"
                    },
                    "tax": {
                        "currency_code": "USD",
                        "value": "10.00"
                    },
                    "quantity": "1",
                    "category": "PHYSICAL_GOODS",
                },
                {
                    "name": "Shoes",
                    "description": "Running, Size 10.5",
                    "sku": "sku02",
                    "unit_amount": {
                        "currency_code": "USD",
                        "value": "45.00"
                    },
                    "tax": {
                        "currency_code": "USD",
                        "value": "5.00"
                    },
                    "quantity": "2",
                                "category": "PHYSICAL_GOODS"
                }
            ],
            "shipping": {
                "method": "United States Postal Service",
                "name": {
                    "full_name": "Andre Hangalo"
                },
                "address": {
                    "address_line_1": "123 Townsend St",
                    "address_line_2": "Floor 6",
                    "admin_area_2": "San Francisco",
                    "admin_area_1": "CA",
                    "postal_code": "94107",
                    "country_code": "US"
                }
            }

        }

    def test_post_and_get_payment(self):
        """test payment"""
        response = self.client.post(self.url, data=self.data, format='json')
        #print('Response payment: ', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_payment(self):
        """test payment"""
        response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        pk = response.json()['id']

        url = reverse('payment-detail', None, {pk})
        # get payment after create
        response = self.client.get(url, format='json')
        print('Request payment: ', response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
