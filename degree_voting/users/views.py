from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# message.debug
# message.info
# message.success
# message.warning
# message.error


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('polls-home')

    context = {
        'title': 'Register',
        'form': form
    }
    return render(request, 'users/register.html', {'context': context})
