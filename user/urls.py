from django.urls import path, include
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path(r'login/', authViews.LoginView.as_view(template_name='user/auth.html'), name='auth'),
    path(r'accounts/profile/', views.profile, name='profile'),
    path(r'exit/', authViews.LogoutView.as_view(template_name='user/exit.html'), name='exit'),
    path('social-auth/', include('social_django.urls', namespace="social")),

    path(r'pass-reset/',
         authViews.PasswordResetView.as_view(template_name='user/reset_password.html'), name='pass-reset'),

    path(r'password_reset_confirm/<uidb64>/<token>/',
         authViews.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path(r'password-reset/done/',
         authViews.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
         name='password_reset_done'),

    path(r'password_reset_complete/',
         authViews.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),
]
