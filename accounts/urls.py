from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

import accounts.views as accounts_views

urlpatterns = [
    path("register", accounts_views.RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("my-uploads", accounts_views.MyUploadsListView.as_view(), name="my-uploads"),
    path("logout", LogoutView.as_view(), name="logout"),
]
