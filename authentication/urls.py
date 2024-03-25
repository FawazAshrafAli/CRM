from django.urls import path
from .views import (LoginView, LogoutView, RegisterUserView, 
                    CrmUserDetailView, Error404, Error500)

app_name = "authentication"

urlpatterns = [
    path('', LoginView.as_view(), name='login'),  # home page view    
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterUserView.as_view(), name="register"),
    path('detail/<pk>', CrmUserDetailView.as_view(), name="detail"),

    path('error404', Error404.as_view(), name="error404"),
    path('error500', Error500.as_view(), name="error500"),
]
