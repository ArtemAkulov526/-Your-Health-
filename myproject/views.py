from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from myproject.models import Services, Appointment, Departments
from myproject.forms import RegistrationForm, AppointmentForm, ServiceForm


def home(request):
    return render(request, 'index.html')

def departments(request):
    return render(request, 'departments.html')

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html',{'services':services}) 

def about(request):
    return render(request, 'about.html')

def account(request):
    if not request.user.is_authenticated:
        # User is not authenticated (anonymous user)
        return redirect('Авторизація') 
    else:
        username = request.user.username.replace('_', ' ')
        email=request.user.email
        appointments = Appointment.objects.filter(user=request.user)
        # User is authenticated (logged in)
        return render(request, 'account.html',{'username':username, 'email':email, 'appointments':appointments})

@login_required
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('Особистий кабінет')  
    else:
        form = AppointmentForm()

    departments = Departments.objects.all()  
    context = {'form': form, 'departments': departments}
    return render(request, 'appointment.html', context)
    
def render_department(request, department_id, template_name):
    """
    Generalized view to render department data.
    :param request: HttpRequest object
    :param department_id: ID of the department to filter
    :param template_name: Template file to render
    :return: HttpResponse with rendered template
    """
    mydata = Services.objects.filter(Department_id=department_id).values()
    template = loader.get_template(template_name)
    context = {
        'services': mydata,
    }
    return HttpResponse(template.render(context, request))

def ear(request):
    return render_department(request, 1, 'ears.html')

def therapy(request):
    return render_department(request, 2, 'therapy.html')

def allergy(request):
    return render_department(request, 3, 'allergy.html')

def gyne(request):
    return render_department(request, 4, 'gynecology.html')

def gastro(request):
    return render_department(request, 5, 'gastro.html')

def derma(request):
    return render_department(request, 6, 'derma.html')

def endokryn(request):
    return render_department(request, 7, 'endokryn.html')

def endo(request):
    return render_department(request, 8, 'endo.html')

def immo(request):
    return render_department(request, 9, 'immo.html')

def cardio(request):
    return render_department(request, 10, 'cardio.html')

def mamo(request):
    return render_department(request, 11, 'mamology.html')

def neurology(request):
    return render_department(request, 12, 'neurology.html')

def proctology(request):
    return render_department(request, 13, 'proctology.html')

def urology(request):
    return render_department(request, 14, 'urology.html')

def signup(request):
    username = ''  
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name_with_spaces = request.POST.get('username', '')
            username = name_with_spaces.replace(' ', '_')
            user = form.save()
            login(request, user)
            return redirect('Особистий кабінет')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form,'username': username})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Особистий кабінет')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Головна сторінка')

def deleteappointment(request, AppointmentID):  
    appoid = Appointment.objects.get(pk=AppointmentID)  
    appoid.delete()  
    return redirect('Особистий кабінет')

def administrator(request):
    services = Services.objects.all()
    return render(request, 'administrator.html',{'services':services}) 

def ServiceNewForm(request):
    if request.method == "POST":  
        form = ServiceForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('Сайт для персоналу')  
            except:  
                pass
    else:  
         form=ServiceForm()
    return render(request,'service_new_form.html', {'form': form})

def update_service(request, ServiceId):  
    services = Services.objects.get(pk=ServiceId)  
    form=ServiceForm(request.POST or None, instance=services)
    if form.is_valid():  
            try:  
                form.save()  
                return redirect('Сайт для персоналу')  
            except:  
                pass
    return render(request,'service_update.html', {'services': services, "form":form })

def deleteservice(request, ServiceId):  
    orderid = Services.objects.get(pk=ServiceId)  
    orderid.delete()  
    return redirect('Сайт для персоналу')

def appoint(request):
    appointments=Appointment.objects.all()
    return render(request, 'appoint.html',{'appointments':appointments})





    