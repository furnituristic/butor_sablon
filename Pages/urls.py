from django.urls import path
from .views import home_page, kapcsolat, about, velemeny, contact_user

urlpatterns = [
    path('', home_page, name="home"),
    path('contact_user/', contact_user, name="contact_user"),
    path('velemeny/', velemeny, name="velemeny"),
    path('contact/', kapcsolat, name="contact"),
    path('about/', about, name="about"),
]