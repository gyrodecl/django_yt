from django.http import HttpResponse
from django.template.loader import get_template    #looks at templates found 
from django.template import Context                #in path specified in settings.py file
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

'''
Django Class-Based Views
'''
class HelloTemplate(TemplateView):
    template_name = 'hello_class.html'
    
    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Russell'
        return context    

#These 3 views are the function-based views
def hello(request):
    name ="Russell"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name            
    return HttpResponse(html)

def hello_template(request):
    name="Russell"
    template = get_template("hello.html")
    html = template.render(Context({'name': name}))
    return HttpResponse(html)

#does what the above function does in fast way
def hello_template_simple(request):
    name = "Russell"
    return render_to_response('hello.html', {'name':name})
