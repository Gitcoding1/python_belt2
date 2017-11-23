from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User

def flash_errors(errors, request):
    for error in errors:
       messages.error(request, error)

def current_user(request):
    return User.objects.get(id=request.session['user_id'])

def user(request, id):
    context={
        'user' : current_user(request),
    }
    return render(request, 'user.html', context)

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method =="POST":
        errors = User.objects.validate_registration(request.POST)

        if not errors:
            user = User.objects.create_user(request.POST)
            request.session['user_id'] = user.id
            return redirect(reverse('main'))

        flash_errors(errors, request)
    return redirect(reverse('landing'))

def login(request):
    if request.method == "POST":
        check = User.objects.validate_login(request.POST)
        

        if 'user' in check:
            request.session['user_id'] = check['user'].id
            return redirect(reverse('main'))

        flash_errors(check['errors'], request)
    return redirect(reverse('landing'))

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')

    return redirect(reverse('landing'))
