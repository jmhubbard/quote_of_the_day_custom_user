from django.urls import path, include
from users.views import UserCreate, UserDeleteView, useraccountview
from main.views import UserLoginView, UserLogoutView

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('add/', UserCreate.as_view(), name='user-add'), #Create user page
    path('logout/' , UserLogoutView.as_view(), name='logout'),
    path('delete_account/<int:pk>/', UserDeleteView.as_view(), name='delete_account'),
    path('account_page/', useraccountview, name='account_page')
        # path('', include('django.contrib.auth.urls')), #accounts/login = login page
        # path('accounts/', include('django.contrib.auth.urls')), #accounts/login = login page
        
]
