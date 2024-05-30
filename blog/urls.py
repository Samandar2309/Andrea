from django.urls import path
from .views import home, fashion, travel, about, contact1_view
urlpatterns = [
    path('', home, name='home'),
    path('fashion.html/', fashion, name='fashion'),
    path('travel.html/', travel, name='travel'),
    path('about.html/', about, name='about'),
    path('contact.html/', contact1_view, name='contact1'),

]
