from django.urls import path, include, re_path
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    re_path(
        r'dj-rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
        name='account_confirm_email',
    ),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),


]