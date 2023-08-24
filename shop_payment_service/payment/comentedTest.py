from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from payment.models import Payment
from payment import views


class PaymentAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse(views.PaymentList.name)
        self.payment_data = {
            "order": "1",
            'user': '1',
            "payment_method": "card",
            "payment_status": True,
            "amount": "299.00",
            "currency": "AKz",

            "card_number": "2024",
            "expiry_month": "5",
            "expiry_year": "2024",
            "cvc": "123"
        }

    def test_post_and_get_payment(self):
        """test payment"""
        response = self.client.post(
            self.url, self.payment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

    def test_post_with_the_same_order_and_payment_status_payment(self):
        """test post with same orderId and payment_status"""
        response = self.client.post(
            self.url, self.payment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

        response = self.client.post(self.url, self.payment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_payment_detail(self):
        """test get payment"""
        response = self.client.post(
            self.url, self.payment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

        url = reverse(views.PaymentDetail.name, None,
                      {Payment.objects.get().pk})
        response = self.client.get(url, format='json')
        #print('Get payment detail: ', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['order'], Payment.objects.get().order)

    def test_update_payment(self):
        """test update payment"""
        response = self.client.post(
            self.url, self.payment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

        """New data to update"""
        payment_data = {
            "order": "1",
            'user': '1',

            "payment_method": "ATM",
            "payment_status": True,
            "amount": "299.00",
            "currency": "AKz",
            "card_number": "2024",
            "expiry_month": "5",
            "expiry_year": "2024",
            "cvc": "123"
        }
        url = reverse(views.PaymentDetail.name, None,
                      {Payment.objects.get().pk})
        response = self.client.put(url, payment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['payment_status'], True)

    def test_update_single_field_payment(self):
        """test update payment"""
        response = self.client.post(
            self.url, self.payment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

        """New data to update"""
        payment_data = {

            "payment_status": True,
        }
        url = reverse(views.PaymentDetail.name, None,
                      {Payment.objects.get().pk})
        response = self.client.patch(url, payment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['payment_status'], True)

    def test_delete_payment(self):
        """test delete payment"""
        response = self.client.post(
            self.url, self.payment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

        url = reverse(views.PaymentDetail.name, None,
                      {Payment.objects.get().pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PaymentServiceAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse(views.PaymentServiceAPI.name)
        self.payment_data = {
            "order": "1",
            'user': '1',
            "payment_method": "card",
            "payment_status": True,
            "amount": 299,
            "currency": "usd",

            "card_number": "2024",
            "expiry_month": "5",
            "expiry_year": "2024",
            "cvc": "123"
        }

    def test_post_and_get_payment(self):
        """test payment"""
        response = self.client.get(
            self.url, format='json')
        print('Response payment: ', response)
        #self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(Payment.objects.count(), 1)

  