from tastypie.resources import ModelResource   #in web, everything is resource---going to base web service off of our Article model 
from tastypie.constants import ALL   #this constant lets us set the query types that we can perform on our models
#ex: instead of listing everything, you could filter, use a like or contains
from article.models import Article

#simple API
'''
class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'  #when webservice is called on our urls, its name is called 'article'.  will be /article/ in url
'''
class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        filtering = {"title": ALL}   #could do   {"title": "contains"} which
        #would mean you could only use the contains filter.  Instead
        #we're going to say we'll allow all type of filtering on the "title" keyword