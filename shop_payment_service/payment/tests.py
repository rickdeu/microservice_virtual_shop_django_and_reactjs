from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from payment import views
from payment.autentication import login_user


class PaymentPayPalServiceAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.pk = 2
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
     
        }

    def test_post_and_get_payment(self):
        login = login_user(email='user@gmail.com', password='ndh*8987979878')
        print('Login payment: ', login.json()['access'])

        url = reverse(views.PaymentOrderCreate.name,  None, {self.pk, login.json()['access']})

        response = self.client.post(url, data=self.data, format='json')
        #print('Response payment: ', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


