"""
Настройки Django для проекта demodjango.

Сгенерировано «django-admin startproject» при использовании Django 3.1.1.

Дополнительные сведения см.
https://docs.djangoproject.com/en/3.1/topics/settings/

Полный список настроек и их значений см.
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Создавать пути внутри проекта нужно следующим образом: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Настройки быстрого старта разработки — не подходят для продакшена
# См. https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# ПРЕДУПРЕЖДЕНИЕ ПО БЕЗОПАСНОСТИ: держите секретный ключ, используемый в производстве, в секрете!
SECRET_KEY = 'Секретный ключ на то и секретный'

# ПРЕДУПРЕЖДЕНИЕ ПО БЕЗОПАСНОСТИ: не запускайте программу с включенным режимом отладки!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'portal.iro23.ru']


# Определение приложения

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demoapp',
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

ROOT_URLCONF = 'demodjango.urls'

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

WSGI_APPLICATION = 'demodjango.wsgi.application'


# База данных
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': 'Пароль от БД',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Проверка пароля
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Интернационализация
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Статические файлы (CSS, JavaScript, Изображения)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
