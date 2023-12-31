"""
Django settings for shop_payment_service project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^0&7y5=z&8-%(qy1=js7%#dsamk0bfu*%7yrg(!w^i0tl=z&)*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

  
    'payment',
    # instaled apps
    'rest_framework',
    'corsheaders',
      "payments", # payment method
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop_payment_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop_payment_service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

SECRET_KEY_STRIPE = 'sk_test_51NgtPHA8Oef8p9EQdBLgD3KuBXSeny5Uvyd72QV7bMl2Zyz8gYgpdXCTjtaAsNaMUD74QP4ySvG5H9LVLCFbW7a700vi5kXHUk'
PUBLIC_KEY_STRIPE ='pk_test_51NgtPHA8Oef8p9EQq7ti4KIINsVampsa4ITdImboL7KAo3r3t07udEtklO3g93JnJaie7VmPtvygMqSDfDfMMOBV00ZXpfPMl8'


# PAYMENT METHODS
PAYMENT_HOST = '0.0.0.0:8003'
PAYMENT_USES_SSL = False
# optional
#PAYMENT_VARIANT_FACTORY = "mypaymentapp.provider_factory"

# PAYPAL
CLIENT_ID = 'AXvcINdvWQUhrlDcIV7XAu44KHrsI5P-rGqGBPqowUCWUxtxLeucbf1jL4nQquTKlz8_-ddZhdVtAZD5'
SECRET_KEY_PAYPAL = 'EOC9gj3x-67wT6_v13WpE6dIfN1670gs5N31NImL9jqSzgSmWH9DGcn6LX1kZJNAAV3EHLj6hFw0eGsK'