from django.shortcuts import render, redirect

# this decorators helps to check if a user is already authenticated or not


def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
