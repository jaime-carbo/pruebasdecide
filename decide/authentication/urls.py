from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

from .views import GetUserView, LogoutView, RegisterView, WelcomeView, LoginView, GoogleView, EmailLoginView
from django.views.generic import TemplateView 


urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    path('getuser/', GetUserView.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('bienvenida/<str:username>/', WelcomeView.as_view(), name='bienvenida'),
    path("accounts/", include("allauth.urls")),
    path('google/', TemplateView.as_view(template_name='google/login.html'), name='google-login'),
    path('login-page/', LoginView.as_view(),name='login-sin-google'),
    path('login-page2/', EmailLoginView.login_correo,name='login-sin-google-email'),
    path('accounts/profile/', GoogleView.as_view(), name='incioGoogle')
 
    


]
