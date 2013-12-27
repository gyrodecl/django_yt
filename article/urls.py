from django.conf.urls import patterns, include, url
from api import ArticleResource

article_resource = ArticleResource()  #created an instance of our ArticleResource

urlpatterns = patterns('',
    url(r'^all/$', 'article.views.articles', name="all"),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article', name="get_article"),
    url(r'^language/(?P<language>[a-z\-]+)/$','article.views.language', name="language"),
    url(r'^create/$', 'article.views.create', name="create_article"),      #view accesses our ModelForm
    url(r'^like/(?P<article_id>\d+)/$','article.views.like_article', name="like_article"),
    url(r'^add_comment/(?P<article_id>\d+)/$','article.views.add_comment',name="add_comment"),
    url(r'^search/$', 'article.views.search_titles'),
    url(r'^api/', include(article_resource.urls)),  #these urls automatically come from ModelResource
    url(r'^my_version_api/$', 'article.views.api_myway'),
    url(r'^$', 'article.views.articles', name="all")
)