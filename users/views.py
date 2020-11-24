from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Your account has been created! You can login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',  {'form': form})
