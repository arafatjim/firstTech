"""
URL configuration for firstTech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstTech import views;
from firstTech import news;
urlpatterns = [
    path('', views.mainPage, name='home'),
    path('admin/', admin.site.urls),
    path('about-us/',views.aboutUs, name='about-us'),
    path('featured-products/',views.featuredProducts, name='featured-products'),
    path('user-form/',views.userForm, name='user-form'),
    path('sign-up/',views.signUpPage, name='sign-up'),
    path('todays-offer/',views.offers, name='todays-offer'),
    path('welcome-text/',views.welcomeText, name='welcome-text'),
    path('submit-form/',views.sumbmitForm, name='submit-form'),
    
    
    path('todays-weather/', news.todaysWeather),
    path('events/',views.events),
    path('club/',views.club),
    path('contact-us/',views.contactUs, name='contact-us'),
    path('gallery/',views.gallery),
    # path('contact-us/<int:detailsId>/',views.contactUsDetails),
    # path('contact-us/<str:detailsId>/',views.contactUsDetails),
    path('contact-us/<slug:detailsId>/',views.contactUsDetails),

    path('calculator/',views.calculator, name='calculator'),
    path('calculator2/',views.calculator2, name='calculator2'),
] 
