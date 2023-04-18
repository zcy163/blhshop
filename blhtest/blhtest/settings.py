"""
Django settings for blhtest project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f+5q%jn5olkmf6354m#fei#u5!c_7+&d01t#)0z^!ud)fh(#xq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 添加第三方库
INSTALLED_APPS.extend([
    'rest_framework',
    'rest_framework.authtoken',
    'werkzeug_debugger_runserver',
    'django_extensions',
])

# 自定义应用
INSTALLED_APPS.extend([
    'applications.kwaixiaodian.apps.KwaixiaodianConfig',
])

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blhtest.urls'

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

WSGI_APPLICATION = 'blhtest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blhwxamp',
        'USER': 'blhwxamp',
        'PASSWORD': '123456',
        'HOST': '121.36.26.112',
        'PORT': '3306',
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 中文

TIME_ZONE = 'Asia/Shanghai'  # 时区

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


########################################################################################################
# SSL配置
########################################################################################################
SECURE_SSL_REDIRECT = True


########################################################################################################
# Reids配置
########################################################################################################
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://121.36.26.112:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "decode_responses": True
            },
            "PASSWORD": "123456"
        },
    }
}


########################################################################################################
# Celery配置
########################################################################################################
CELERY_TIMEZONE = TIME_ZONE
BROKER_URL = "redis://:123456@121.36.26.112:6379/0"
CELERY_RESULT_BACKEND = "redis://:123456@121.36.26.112:6379/0"
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERYBEAT_SCHEDULE = {
    'kwaixiaodian_refresh_token': {
        'task': 'applications.kwaixiaodian.tasks.refresh_token',
        'schedule': 10
    }
}

########################################################################################################
# 快手电商平台配置
########################################################################################################
KWAIXIAODIAN_HOST = "https://open.kwaixiaodian.com"
KWAIXIAODIAN_API_HOST = "https://openapi.kwaixiaodian.com"
KUAISHOU_HOST = "https://open.kuaishou.com"
KWAIXIAODIAN_OAUTH2_AUTHORIZE_URL = "https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/oauth2/access_token"
KWAIXIAODIAN_APP_ID = "ks686517468460941728"
KWAIXIAODIAN_APP_SECRET = "8_jgQcgFCYLJGO-lrAD4Mg"
KWAIXIAODIAN_SIGN_SECRET = "48c8f5d9c8c70facbd84e00fbace5f5a"
KWAIXIAODIAN_REDIRECT_URI = "https://wxamp.blhlm.com/kwaixiaodian/oauth2/authorize"
KWAIXIAODIAN_SCOPE = "merchant_distribution"
KWAIXIAODIAN_RESPONSE_TYPE = "code"
KWAIXIAODIAN_GRANT_TYPE = "code"
KWAIXIAODIAN_SIGN_METHOD = "MD5"

