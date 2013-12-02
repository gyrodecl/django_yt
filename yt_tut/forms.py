#currently we're using UserCreationForm in
#django.contrib.auth.forms in our def register_user() function
#we're going to subclass that UserCreationForm which
#by default only gives username password  passwordconfirmation
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#subclass of UserCreationForm--can look at the code
#for UserCreationForm in django.contrib.auth
class MyRegistrationForm(UserCreationForm):
    #easier since just need to specify form fields
    #we already have username, password1 and password2 from UserCreationForm superclass
    email = forms.EmailField(required=True)    
    
    #Meta inner class in django is a class container with
    #some options attached to model.  Like a namespace
    #put a . before accessing values in the inner class Completely different from
    #Python metaclasses (totally different)
    class Meta:        #embedded class; holds anything that isn't a form field
        model = User   #holds metadata: what model is, what fields are
        fields = ('username','email','password1','password2')
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        #user.first_name = self.cleaned_data['first_name']
        #user.last_name = self.cleaned_data['last-name']
        if commit:
            user.save()
        return user
    

#this is what the save function looks like in django.contrib.auth
#which we're overriding
'''
class UserCreationForm
def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password1"])   #need to sanitize data
    if commit:
        user.save()
    return user
'''

'''Form Wizard Example----linking 3 contact forms together'''
class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    
class ContactForm2(forms.Form):
    sender = forms.EmailField()
    
class ContactForm3(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

