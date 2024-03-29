from django.contrib.messages import constants as messages
import os
import environ
import django_heroku    
from pathlib import Path

# read the .env file
environ.Env.read_env()
env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = env('DEBUG')
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'pages',
    'listings',
    'users',
    'blog',
    'subscriptions',
    'codes',
    # 'chat',
    'django_private_chat2.apps.DjangoPrivateChat2Config',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.postgres',

    'crispy_forms',
    'phonenumber_field',

    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
]

SITE_ID = 1

# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    # "allauth.account.auth_backends.AuthenticationBackend",
]

AUTH_USER_MODEL = 'users.User'
ACCOUNT_USER_MODEL_USERNAME_FIELD = "number"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'verify-view'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_FORMS = {'login': 'users.forms.LoginForm'}
ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.RegisterForm'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'realestate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'realestate.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rentroom',
        'USER': 'postgres',
        'PASSWORD': 'daniel15',
    }
}

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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())

PAYSTACK_SECRET_KEY = os.environ['PAYSTACK_SECRET_KEY']
PAYSTACK_PUBLIC_KEY = os.environ['PAYSTACK_PUBLIC_KEY']

PAYPAL_RECEIVER_EMAIL = 'ayomidedans@gmail.com'
PAYPAL_TEST = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# myaccount.google.com/lesssecureapps
# accounts.google.com/DisplayUnlockCaptcha

# myaccount.google.com/apppasswords

# Email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'djangotest62@gmail.com'
EMAIL_HOST_PASSWORD = 'testdjango_99'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False


# CHAT_WS_SERVER_HOST = 'localhost'
# CHAT_WS_SERVER_PORT = 5002
# CHAT_WS_SERVER_PROTOCOL = 'ws'
