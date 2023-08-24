# import apps
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from shop_payment_service import settings
import json
import base64
import stripe
# local imports
from payment.serializers import PaymentSerializer
from payment.models import Payment
from rest_framework.decorators import api_view
import requests
# class view payment


class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    name = 'payment-list'


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    name = 'payment-detail'


class PaymentServiceAPI(APIView):
    name = 'payment-service'

    serializer_class = PaymentSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        response = {}
        if serializer.is_valid():
            data_dict = serializer.data
            stripe.api_key = settings.SECRET_KEY_STRIPE
            response = self.strip_card_payment(
                request=request, data_dict=data_dict)
            print('Response 1: ', response)
            return Response(response)
        return Response({'errors': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def strip_card_payment(self, request, data_dict):
        try:
            card_information = {
                'type': 'card',
                'id': data_dict['order'],
                'card': {
                    'number': data_dict['card_number'],
                    'exp_month': data_dict['expiry_month'],
                    'exp_year': data_dict['expiry_year'],
                    'cvc': data_dict['cvc'],
                },
            }
            print('Data serializer: ', data_dict)
            payment_intent = stripe.PaymentIntent.create(
                amount=1002,
                currency='usd',
            )
            payment_intent_modified = stripe.PaymentIntent.modify(
                payment_intent['id'],
                payment_method=card_information['id']
            )
            try:
                payment_confirm = stripe.PaymentIntent.confirm(
                    payment_intent['id']
                )
                payment_intent_modified = stripe.PaymentIntent.retrieve(
                    payment_intent['id'])
                payment_confirm = {
                    'strip_payment_error': 'Failed',
                    'code': payment_intent_modified['last_payment_error']['code'],
                    'message': payment_intent_modified['last_payment_error']['message'],
                }
                if payment_intent_modified and payment_intent_modified['status'] == 'succeeded':
                    response = {
                        'message': 'Card Payment Success',
                        'status': status.HTTP_200_OK,
                        'card_details': card_information,
                        'payment_intent': payment_intent_modified,
                        'payment_confirm': payment_confirm
                    }
                response = {
                    'message': 'Card Payment Failed',
                    'status': status.HTTP_400_BAD_REQUEST,
                    'card_details': card_information,
                    'payment_intent': payment_intent_modified,
                    'payment_confirm': payment_confirm
                }

            except:
                response = {
                    'error': 'Your card number is incorrect',
                    'status': status.HTTP_400_BAD_REQUEST,
                    'payment_intent': {'id': None},
                    'payment_confirm': {'status': 'Failed'}
                }
        except Exception as e:
            response = {'status': status.HTTP_400_BAD_REQUEST,
                        'message': e, }
        return response


@api_view(['GET'])
def create_payment(request):
    stripe.api_key = settings.SECRET_KEY_STRIPE
    try:

        payment_intent_create = stripe.PaymentIntent.create(
            amount=1099,
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "4242424242424242",
                "exp_month": 8,
                "exp_year": 2024,
                "cvc": "314",
            },
        )
        try:
            stripe.PaymentIntent.modify(
                payment_intent_create['id'],
                metadata={
                    "number": '4242424242424242',
                    "exp_month": '83',
                    "exp_year": '2023',
                    "order_id": "6735",
                },
            )
            stripe.PaymentIntent.confirm(
                payment_intent_create['id'],
                payment_method="pm_card_visa",
            )
            payment_intent_retrieve = stripe.PaymentIntent.retrieve(
                payment_intent_create['id'],
            )
            print('Response: strip: ', payment_intent_retrieve)
            # return Response(payment_intent_modify)
            if payment_intent_retrieve and payment_intent_retrieve['status'] == 'succeeded':
                response = {
                    'message': 'Card Payment Success',
                    'status': status.HTTP_200_OK,
                    'card_details': 'card_information',
                    'payment_intent': payment_intent_retrieve,
                    'payment_confirm': payment_confirm
                }
                response = {
                    'message': 'Card Payment Failed',
                    'status': status.HTTP_400_BAD_REQUEST,
                    'card_details': 'card_information',
                    'payment_intent': payment_intent_retrieve,
                    'payment_confirm': payment_confirm
                }
            return response
        except:
            payment_confirm = stripe.PaymentIntent.confirm(
                payment_intent_create['id'],
                payment_method="pm_card_visa",
            )
            payment_intent_retrieve = stripe.PaymentIntent.retrieve(
                payment_intent_create['id'])
            payment_confirm = {
                'strip_payment_error': 'Failed',
                'code': payment_intent_retrieve['last_payment_error']['code'],
                'message': payment_intent_retrieve['last_payment_error']['message'],
            }
    except stripe.error.CardError as e:
        print('Status is: %s' % e.http_status)
        print('Code is: %s' % e.code)
        # param is '' in this case
        print('Param is: %s' % e.param)
        print('Message is: %s' % e.user_message)
        return Response(e)
    except stripe.error.RateLimitError as e:
        # Too many requests made to the API too quickly
        return Response(e)
    except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe's API
        return Response(e)
    except stripe.error.AuthenticationError as e:
        # Authentication with Stripe's API failed
        # (maybe you changed API keys recently)
        return Response(e)
    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        return Response(e)
    except stripe.error.StripeError as e:
        # Display a very generic error to the user, and maybe send
        # yourself an email
        return Response(e)
    except Exception as e:
        # Something else happened, completely unrelated to Stripe
        return Response(e)


class PayPalPaymentServiceAPI(APIView):
    name = 'paypal-service'

    def paypalToken(self, client_id, client_secret):
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

    def post(self, request, format=None):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.paypalToken(client_secret=settings.SECRET_KEY_PAYPAL, client_id=settings.CLIENT_ID)}', }

        response = requests.post(
            'https://api-m.sandbox.paypal.com/v2/checkout/orders', headers=headers, json=request.data)
        if response.status_code == 201:
            return Response(response)
        return Response({'errors': response.json()['name'], 'status': response.status_code})


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'payments': reverse(PaymentList.name, request=request),


            }
        )
