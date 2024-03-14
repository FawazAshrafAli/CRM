from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import View
from django.contrib.auth import  authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CrmUser
from django.db.utils import IntegrityError

class RegisterUserView(TemplateView):
    template_name = 'authentication/register.html'

    def post(self, request, *args, **kwargs):
        context = {}
        message = None
                
        email = request.POST.get("email")        
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")

        required_fields = ["email", "password", "repeat_password"]

        for field in required_fields:
            if not locals()[field]:
                message = f"{field.capitalize()} field cannot be blank"                
                break
            else:
                context.update({str(field.lower()): locals()[field]})                

        if not message:
            if password != repeat_password:
                message = "Passwords do not match."
                context.update({"password": password})

            if not message:
                try:
                    user = User.objects.create_user(username=email, password=password)
                    crm_user = CrmUser.objects.create(user=user, email=email)

                    if not crm_user:
                        user.delete()
                    else:
                        messages.success(request, "User creation successful")
                        login(request, user)
                        return redirect(reverse('dashboard:deals_dashboard'))
                except IntegrityError:
                    message = "User with the given email id already exists"
                    context.update({"repeat_password": repeat_password})

        if message:
            messages.error(request, message)        
        return render(request, self.template_name, context)

class LoginView(View):
    template_name = 'authentication/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('dashboard:deals_dashboard'))
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect(reverse('dashboard:deals_dashboard'))
            else:
                messages.error(request, 'Invalid username or password')                

        return redirect(reverse('authentication:login'))
        
        
class LogoutView(LoginRequiredMixin, View):
    login_url = 'authentication:login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('authentication:login'))
    

# class HomeView(LoginRequiredMixin, TemplateView):
#     template_name = "authentication/home.html"
#     login_url = 'login'
#     redirect_field_name = 'home'
#     raise_exception = True

#     def handle_no_permission(self):
#         return redirect(reverse(self.login_url))
