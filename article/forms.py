from django import forms
from models import Article, Comment

#use ModelForm
class ArticleForm(forms.ModelForm):    
    
    class Meta:    #this class defines anything that's not a form field
        model = Article       #so form is now bound to Article model 
        fields = ('title','body','pub_date','thumbnail')   #so by not listing the likes fields
                                #we keep it from being displayed
    
#now a form for our comments
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name','body')
    
