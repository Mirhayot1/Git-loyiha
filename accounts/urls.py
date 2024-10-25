from django.urls import path
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from .views import user_login, dashboard_view, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', dashboard_view, name='user_profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
# html css js>>>https://codepen.io/codyhouse/pen/QWpVKB