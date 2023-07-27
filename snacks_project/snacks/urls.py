from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, SnacksPageView

urlpatterns= [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('snacks/', SnacksPageView.as_view(), name='snacks')
]