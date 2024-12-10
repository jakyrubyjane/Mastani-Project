from django.shortcuts import render, redirect
from .forms import UpdateSeller
from django.contrib import messages
# Create your views here.

def dashboard (request):
    if request.user.is_authenticated:
        user = request.user

    else:
        user = None

    return render(request, 'seller_app/dashboard.html', {'user':user})

def profile_view(request):
   # update user data

    user_auth = request.user

    if request.method == 'POST':
        form = UpdateSeller(request.POST, instance=user_auth)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Anda Telah Di Perbaharui!')
            return redirect('profile_view')
    else:
        form = UpdateSeller(instance=user_auth)


    return render(request, 'seller_app/profile.html', {'form':form})
