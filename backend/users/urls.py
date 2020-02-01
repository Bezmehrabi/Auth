from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from knox import views as knox_views


from .views import RegisterAPIView, LoginAPIView, UserAPI


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('main/', UserAPI.as_view()),
]