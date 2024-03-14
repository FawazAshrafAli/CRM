from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),  # home page view
    # path('home/', views.HomeView.as_view(), name='home'),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterUserView.as_view(), name="register"),
]
