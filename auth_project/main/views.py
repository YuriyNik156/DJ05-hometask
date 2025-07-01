from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # заменишь на нужный URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def home(request):
    return render(request, 'main/home.html')
