from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Contact, Knowledge
from django.contrib.auth import authenticate, login, logout as user_logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    knowledge = Knowledge.objects.all()
    return render(request, 'core/index.html', locals())


# Blog View.
def blog(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact.objects.create(full_name=full_name, email=email,subject=subject, message=message)
        send_mail(subject, message, email, ['deepvk575@gmail.com'])
    # else:
        # return HttpResponse('invalid header found.')
    return render(request, 'core/blog.html', locals())

# Dashboard View.
# @login_required(login_url='/login/dashboard/')
def dashboard(request):
    if request.user.is_staff == True:
        return render(request, 'core/dashboard/dashboard.html')
    else:
        return HttpResponseRedirect('/login/dashboard/')


# Login Dashboard View.
# @login_required(login_url='/')
def login_dashboard(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        check = request.POST['check']
        user = authenticate(username=username, password=password, check=check)
        if user is not None:
            if user.is_staff == True:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
            else:
                return redirect('/login/dashboard/')
    return render(request, 'core/dashboard/login_dashboard.html', locals() )




# Logout View..
def logout(request):
    user_logout(request)
    return redirect('/')

@login_required(login_url='/login/dashboard/')
def dash_contact_info(request):
    contact = Contact.objects.all()
    return render(request, 'core/dashboard/dash_contact_info.html', locals())


@login_required(login_url='/login/dashboard/')
def dashboard_contact(request):
    return render(request, 'core/dashboard/dash_contact.html')

# Home Slider View.
@login_required(login_url='/login/dashboard/')
def dashboard_home_slider(request):
    form = Knowledge.objects.all()
    return render(request, 'core/dashboard/dashboard_home_slider.html', locals())



# Home Slider Add Image View.
@login_required(login_url='/login/dashboard/')
def dashboard_home_slider_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        user = Knowledge.objects.create(title=title, image=image)
    return render(request, 'core/dashboard/dashboard_home_slider_add.html', locals())

