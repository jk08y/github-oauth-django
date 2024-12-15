from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'accounts/login.html')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')