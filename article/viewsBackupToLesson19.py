from django.shortcuts import render
from article.models import Article, Comment
from django.http import HttpResponse  #need this for cookies
from django.http import HttpResponseRedirect
from forms import ArticleForm, CommentForm
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic import TemplateView
import json
from django.core import serializers
'''
basic articles view before sessions

def articles(request):
    return render(request,'article/articles.html',
                  {'articles':Article.objects.all()})
'''

def articles(request):
    language = 'en-us'     #default value is 'en-us'; will store from cookie
    session_language = 'en-us'    #stores what's in our session
    
    if 'lang' in request.COOKIES:    #if 'lang' in cookies
        language = request.COOKIES['lang']   #then we'll store it
   
    if 'lang' in request.session:     #session is an array
        session_language = request.session['lang']
   
    return render(request, 'article/articles.html',
                  {'articles':Article.objects.all(),
                   'language': language,
                   'session_language' : session_language
                   })

def article(request, article_id=1):
    return render(request, 'article/article.html',
                 {'article': Article.objects.get(id=article_id)})

    #this function will set a cookie with value 'lang'
def language(request, language='en-us'):
    response = HttpResponse("setting language to %s" % language)  #just shows to user
    response.set_cookie('lang', language)   #cookies are set on response
    request.session['lang'] = language      #with sessions, set on session dictionary in request
    return response

#Corresponds with lecture#12--Article creation form
def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)  #this binds data to the form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()
    args = {}
    args['form'] = form
    return render(request, 'article/create_article.html', args)

def like_article(request, article_id):
    if article_id:
        art = Article.objects.get(id=article_id)
        art.likes += 1
        art.save()
    #click like, then re-render page
    return HttpResponseRedirect('/articles/get/%d' % art.id)

#the fields in the model that we didn't get set in the form
#by the user, we need to make sure they're set in the view
#LOOK into in the Model definition if you can have things set automatically
#pub_date for Comment can't be null so need to save that
def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)
    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            #different from before since need to associate comment and article
            c = f.save(commit=False)  #.save returns an instance of comment
            c.pub_date = timezone.now()    #manually put in pub_date
            c.article = a     #need to manually establish article relationship
            c.save()
            return HttpResponseRedirect(reverse('get_article', args=(article_id,)))
    else:
        context = {}
        context['form'] = CommentForm()
        context['article'] = a
        return render(request,'article/create_comment.html',context)

#respond to AJAX calls---search for articles
def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ""
    #use filter----contains means use the like '%' filter in SQL
    articles = Article.objects.filter(title__contains=search_text)
    return render(request, 'ajax_search.html', {'articles': articles})

'''
def api_myway(request):
    #lets try to return the first article as json
    article = Article.objects.all()
    a = serializers.serialize("json", article)
    return HttpResponse(json.dumps(a), content_type="application/json")
'''

def api_myway(request):
    first_article = Article.objects.get(id=1).as_dict()
    return HttpResponse(json.dumps(first_article), content_type='application/json')
