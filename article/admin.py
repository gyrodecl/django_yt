from django.contrib import admin
from article.models import Article
from article.models import Comment

admin.site.register(Article)  #registers the Article class with admin system
admin.site.register(Comment)