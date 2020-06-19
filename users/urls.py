from django.urls import path
from users.views import RegisterView, ImageCodeView, SmscodeView, LoginView, LogoutView, ForgetPassword, UserCenterView, \
    Write

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('imagecode/', ImageCodeView.as_view(), name='imagecode'),
    path('smscode/', SmscodeView.as_view(), name='smscode'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgetpassword/', ForgetPassword.as_view(), name='forgetpassword'),
    path('center/', UserCenterView.as_view(), name='center'),
    path('write/',Write.as_view(), name='write'),
]
