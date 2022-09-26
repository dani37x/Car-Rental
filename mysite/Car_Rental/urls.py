from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.log_to_account, name='log_to_account'),
    path('accounts/logout/', views.logout_view, name='logout_view'),
    path('car/', views.car, name='car'),
    # path('detail/<id>/', views.detail, name='detail'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="change.html"), name="password_reset"),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]