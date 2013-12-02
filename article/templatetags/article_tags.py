from django import template

#we're going to register new template tags
#register is a decorator--#gives extra functionality to function
register = template.Library()

@register.filter(name='article_shorten_body')   #doesn't matter what function name is.  the name here is what is used in template
def article_shorten_body(bodytext,length):   #1st var is the value, 2nd variable is the argument to the function
    if len(bodytext) > length:
        text = "%s ..." % bodytext[1:length]
    else:
        text = bodytext
    return text