from django.shortcuts import render
from basicapp.forms import UserForm

# Create your views here.


def index(request):
    return render(request, 'basicapp/index.html')


def user_login(request):
    return render(request, 'basicapp/login.html')


def user_reg(request):

    registered = False

    if request.method == 'POST':
