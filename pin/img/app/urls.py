from django.urls import path
from .views import MainView, CreateUser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main/', MainView.as_view(), name='main'),
    path("reg/", CreateUser.as_view(), name='reg'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)