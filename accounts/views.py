from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.db import IntegrityError

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        try:
            if form.is_valid():
                user = form.save(commit=False)  # Create user instance without saving
                user.full_name = form.cleaned_data.get('full_name')  # Set `full_name`
                user.save()  # Save user to the database
                messages.success(request, "Account created successfully. Please login.")
                return redirect('accounts:login')
            else:
                messages.error(request, "Please correct the errors below.")
        except IntegrityError:
            messages.error(request, "An account with these details already exists.")
        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)
