"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.home, name='Головна сторінка'),
    path('departments/', views.departments, name='Відділення'),
    path('services/',views.services, name='Послуги'),
    path('about_us/',views.about,name='Про нас'),
    path('account/', views.account, name='Особистий кабінет'),
    path('appointment/',views.appointment, name='Записатися на прийом'),
    path('ears/', views.ear, name='Отоларингологія'),
    path('therapy', views.therapy,name='Терапевтія'),
    path('allergy/',views.allergy,name="Алергологія"),
    path('gynecology/',views.gyne,name="Гінекологія"),
    path('gastro/',views.gastro,name="Гастроентологія"),
    path('derma/',views.derma,name="Дерматологія"),
    path('endokryn/',views.endokryn,name="Ендокринологія"),
    path('endo/',views.endo,name="Ендоскопія"),
    path('immunology/',views.immo,name="Імунологія"),
    path('cardiology/',views.cardio,name="Кардіологія"),
    path('mamology/',views.mamo,name="Мамологія"),
    path('proctology/',views.proctology,name="Проктологія"),
    path('neurology/',views.neurology,name="Неврологія"),
    path('urology/',views.urology,name="Урологія"),
    path('login.html/',views.user_login,name="Авторизація"),
    path('registration.html/',views.signup,name="Регістрація"),
    path('logout/',views.user_logout,name="Вихід з акаунту"),
    path('administrator/',views.administrator, name='Сайт для персоналу'),
    path('new_service/',views.ServiceNewForm, name='Додати запис'),
    path('edit_service/<ServiceId>/',views.update_service, name='Редагувати запис'),
    path('delete_service/<ServiceId>/',views.deleteservice, name='Видалити запис'),
    path('appointments/',views.appoint, name='Записи на прийом'),
    path('delete_appointment/<AppointmentID>/',views.deleteappointment, name='Скасування запису'),

]

#python manage.py runserver