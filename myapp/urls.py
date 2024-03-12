from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about_view, name='about_view'),
    path('function/', views.function_view, name='function_view'),
    path('class/', views.ClassView.as_view(), name='class_view'),
    path('theme/', views.ThemeView.as_view(), name='theme'),
    path("news/", views.news_view, name='news_view'),
    path("climate/", views.climate_veiw,name='climate_veiw'),
   path("health/", views.health_veiw,name=' health_veiw'),
   path("busines/", views.business_veiw,name='business_veiw')
  
]
