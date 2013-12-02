from django.db import models
from time import time
from django.conf import settings
from yt_tut import settings


#the model system knows to pass an instance from Django to a method and filename
#we'll generate a string--we want it to go to our storage location for user_uploaded_files
#from MEDIA_ROOT  and we'll add a filename of the timestamp and _ for formatting 
def get_upload_file_name(instance, filename):
    #return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)
    return settings.UPLOAD_FILE_PATTERN % (str(time()).replace('.','_'), filename)
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name, null=True,blank=True)  #get_upload_file_name is a function we'll create
                                    #easier to have a function to do logic, like associate with specific user
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/articles/get/%i/" % self.id
    
    def get_thumbnail(self):
        thumb = str(self.thumbnail)
        if not settings.DEBUG:
            thumb = thumb.replace('assets/','')
        return thumb
    
    def as_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "likes": self.likes
        }

class Comment(models.Model):
    name = models.CharField(max_length=200)
    #first_name = models.CharField(max_length=200)
    #second_name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    article = models.ForeignKey(Article)  #relationship betweem Comment and Article

    def __unicode__(self):
        return self.name + " on article: " + str(self.article)