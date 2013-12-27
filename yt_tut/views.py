#site-wide views for our authentication system
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth     #auth object for our authentication system
from django.core.context_processors import csrf   #cross-site request forgery system
#csrf embeds a special token into your forms that only your
#website can verify.  Stops this cross-site forgery.
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm  #our custom form
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
import logging
logr = logging.getLogger(__name__)  #will help us know what data we got
import os

def login(request):
    c= {}
    #c['name'] = os.getcwd()
    c.update(csrf(request))    #don't need to pass this c for render since
    return render(request,'login.html', c)   #uses RequestContext

#the token, the username, and password get
#passed from the login form to auth_view
def auth_view(request):
    username = request.POST.get('username','')  #empty string is value if 'username' not found
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
        #if authentication system finds a user, it gives us a User object
        #otherwise if doesnt find one with matching username and password,
        #it will return None
        #.authenticate tells you the user exists but doesn't instantiate the user as loggedin
    if user is not None:       #.login actually logs in the user to our system.
        auth.login(request, user)      #should use (reverse on these urls)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render(request, 'loggedin.html',
                  {'full_name': request.user.username})

def invalid_login(request):
    return render(request, 'invalid_login.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

#most basic registration is username and password
'''
First version using built-in UserCreationForm
'''
'''
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():   #validator for the form
            form.save()     #in real-world, wouldn't make user active until email validation
            return HttpResponseRedirect('/accounts/register_success')
    else:
        args = {}    #this part is sent the first the user visits the page
        args['form'] = UserCreationForm()   #empty RegistrationForm--knows how to render itself
        return render(request, 'register.html', args)   #dont need to pass in csrf
                                                        #when use render()
'''

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():   #validator for the form
            form.save()     #in real-world, wouldn't make user active until email validation
            return HttpResponseRedirect('/accounts/register_success')
    else:    #this is when user first goes to registration page(GET request)
        args = {}    #this part is sent the first the user visits the page
        args['form'] = MyRegistrationForm()   #our custom registration form
        return render(request, 'register.html', args)

def register_success(request):
    return render(request, 'register_success.html')

#SessionWizardView is a class-based view
class ContactWizard(SessionWizardView):
    template_name = "contact_form.html"   #sends in a wizard instance
    
    #need to define what happens when wizard is done collecting info
    #need to override the done function for this particular class
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        return render_to_response("done.html", {'form_data':form_data})

#this happens after all 3 forms are done---here we'll email it off    
def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    
    logr.debug(form_data[0]['subject'])
    logr.debug(form_data[1]['sender'])
    logr.debug(form_data[2]['message'])
    
    #subject, message, sender, recipient into send_mail
    #we changed fail_silently to False to get error messages
    send_mail(form_data[0]['subject'],
              form_data[2]['message'],
              form_data[1]['sender'],
              ['gyrodecode@outlook.com'],fail_silently=False)
    
    return form_data