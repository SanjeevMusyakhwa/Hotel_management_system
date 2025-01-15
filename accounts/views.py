from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()  # Automatically handles password hashing
                messages.success(request, "Account created successfully. Please login.")
                return redirect('accounts:login')
            except IntegrityError:
                messages.error(request, "An account with this phone number or email already exists.")
            except Exception as e:
                messages.error(request, f"Unexpected error: {e}")
        else:
            # Correctly access and print non-field errors for debugging
            print("Non-field errors:", form.non_field_errors())
            for field, errors in form.errors.items():
                print(f"Field: {field}, Errors: {errors}")
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        # Ensure phone_number and password are provided
        if not phone_number or not password:
            messages.error(request, "Phone number and password are required.")
            return render(request, 'accounts/login.html')

        # Authenticate the user
        user = authenticate(request, username=phone_number, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            messages.success(request, "Logged in successfully.")
            return redirect('dashboard:dashboard')  # Replace 'dashboard:dashboard' with your desired URL name
        else:
            messages.error(request, "Invalid phone number or password. Please try again.")

    # Render the login page for GET or in case of failed login
    return render(request, 'accounts/login.html')
  
def LogoutView(request):
  logout(request)
  messages.success(request, "You've been sucessfully logged out")
  return redirect('website:index')

