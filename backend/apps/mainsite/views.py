from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from ..core.models.user import User
from django.shortcuts import redirect
from django.urls import reverse
from .forms import TelegramRegistirationForm
from django.contrib.auth import login, authenticate
import urllib

from django_telegram_login.widgets.constants import (
    SMALL,
    MEDIUM,
    LARGE,
    DISABLE_USER_PHOTO,
)
from django_telegram_login.widgets.generator import (
    create_callback_login_widget,
    create_redirect_login_widget,
)
from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import (
    NotTelegramDataError,
    TelegramDataIsOutdatedError,
)

bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import (
    NotTelegramDataError,
    TelegramDataIsOutdatedError,
)


def index(request):
    # Initially, the index page may have no get params in URL
    # For example, if it is a home page, a user should be redirected from the widget
    if not request.GET.get('hash'):
        return HttpResponse('Handle the missing Telegram data in the response.')

    try:
        result = verify_telegram_authentication(bot_token=bot_token, request_data=request.GET)

    except TelegramDataIsOutdatedError:
        return HttpResponse('Authentication was received more than a day ago.')

    except NotTelegramDataError:
        return HttpResponse('The data is not related to Telegram!')

    # Or handle it as you wish. For instance, save to the database.
    return HttpResponse('Hello, ' + result['first_name'] + '!')


def callback(request):
    telegram_login_widget = create_callback_login_widget(bot_name, size=SMALL)
    print(request.GET)
    context = {'telegram_login_widget': telegram_login_widget}
    return render(request, 'callback.html', context)


def home(request):
    telegram_login_widget = create_redirect_login_widget(
        '/check', bot_name, size=LARGE, user_photo=DISABLE_USER_PHOTO
    )

    context = {'telegram_login_widget': telegram_login_widget}
    return render(request, 'home.html', context)


def check(request):
    if not request.GET.get('hash'):
        return HttpResponse('Handle the missing Telegram data in the response.')

    try:
        result = verify_telegram_authentication(bot_token=bot_token, request_data=request.GET)

    except TelegramDataIsOutdatedError:
        return HttpResponse('Authentication was received more than a day ago.')

    except NotTelegramDataError:
        return HttpResponse('The data is not related to Telegram!')
    try:
        User.objects.get(telegram_username=result['username'])
    except User.DoesNotExist:
        context = {'username': result['username'],
                   'first_name': result['first_name'],
                   'photo_url': result['photo_url']
                   }
        return redirect(reverse('register')+ f"?{urllib.parse.urlencode(context)}")
    else:
        user = authenticate(request, username=result['username'])
        login(request, user)
        return redirect(reverse('home'))

    return HttpResponse('Hello, ' + result['first_name'] + '!')


def register(request):
    if request.method == 'GET':
        telegram_username = request.GET.get('username')

        form = TelegramRegistirationForm(initial={'username': telegram_username})

    if request.method == 'POST':
        telegram_first_name = request.GET.get('first_name')
        telegram_username = request.GET.get('username')
        telegram_photo_url = request.GET.get('photo_url')
        #telegram_last_name = request.GET.get('last_name')
        form = TelegramRegistirationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            User.objects.create_user(
                                username=username,
                                password=raw_password,
                                telegram_username=telegram_username,
                                first_name=telegram_first_name,
                                last_name="telegram_last_name",
                                )
            return redirect('home')
    return render(request, 'signup.html', {'form': form})
