from django.urls import path
from .views import home_page, kapcsolat, about, velemeny, contact_user, stilus_proba

urlpatterns = [
    path('', home_page, name="home"),
    path('contact_user/', contact_user, name="contact_user"),
    path('velemeny/', velemeny, name="velemeny"),
    path('contact/', kapcsolat, name="contact"),
    path('about/', about, name="about"),
    path('stilus_proba/', stilus_proba, name="stilus_proba"),

]