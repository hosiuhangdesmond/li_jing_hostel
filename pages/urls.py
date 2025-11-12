from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('office-style', views.office_style, name='office_style'),
    path('romantic-style', views.romantic_style, name='romantic_style'),
    path('family-friendly', views.family_friendly, name='family_friendly'),
    path('study-focused', views.study_focused, name='study_focused'),
    path('room-prices', views.room_prices, name='room_prices'),
    path('personal-data', views.personal_data, name='personal_data'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
]