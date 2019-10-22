from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistration,ProfileImage
from django.contrib.auth.decorators import login_required



def registration(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Пользователь {username} был успешно создан, войдите в аккаунт.')
            return redirect('auth')
    else:
        form = UserRegistration(request.POST)
    return render(request,'user/registrations.html',{'form':form,'title':'Регистрация пользователя'})

@login_required
def profile(request):
    if request.method == "POST":
        img_profile=ProfileImage(request.POST,request.FILES,instance=request.user.profile)
        # update_user=UserUpdateForm(request.POST,instance=request.user)
        if img_profile.is_valid():
            # update_user.save()
            img_profile.save()
            messages.success(request,f'Данные успешно изменены.')
            return redirect('profile')
    else:
            img_profile=ProfileImage(instance=request.user.profile)
            # update_user=UserUpdateForm(instance=request.user)
    data ={
    'img_profile' : img_profile,
    # 'update_user': update_user
    }
    return render(request, 'user/profile.html',data)
    
