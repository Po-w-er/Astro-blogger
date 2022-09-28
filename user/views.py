from django.shortcuts import render, redirect
from django.contrib import messages
from .form import RegistrationForm, UserUpdateForm, ProfileForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your Account has been created, {username.capitalize()}.")
            return redirect("webby-home")
    else:
        form = RegistrationForm()
    
    return render(request,"user/register.html", { 'form': form})


def account(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('account')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
    context = {
        'u_form': u_form, 
        'p_form': p_form 
    }
    return render(request,"user/account.html", context)