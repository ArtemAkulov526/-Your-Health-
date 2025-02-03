from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from myproject.models import Appointment, Services, Departments

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name','email', 'password1', 'password2')

class AppointmentForm(forms.ModelForm):
        department = forms.ModelChoiceField(
        queryset=Departments.objects.all(),
        to_field_name="DepartmentName",
        label="Department Name"
        )
        class Meta:
           model = Appointment
           fields = ['department', 'NameOfService', 'AppointmentDate', 'AppointmentTime']
           widgets = {
               'AppointmentDate': forms.DateInput(attrs={'type': 'date'}),
               'AppointmentTime': forms.TimeInput(attrs={'type': 'time'}),
        }

class ServiceForm(forms.ModelForm):
        department = forms.ModelChoiceField(
        queryset=Departments.objects.all(),
        to_field_name="DepartmentName",
        label="Department Name"
    )
        class Meta:
            model = Services
            fields = ('department', 'NameOfService')
