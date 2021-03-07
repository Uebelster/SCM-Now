from django import template
from django.db import models
from sustain.models import commentreview
 
register = template.Library()
 
# All custom template tag go here
@register.simple_tag
def countpositive(commentid, type):
    if type=="Intern":
        counter= commentreview.objects.filter(commentsintern=commentid, positive="P").count()
    else:
        counter= commentreview.objects.filter(commentsextern=commentid, positive="P").count()
    return counter

@register.simple_tag
def countnegative(commentid, type):
    if type=="Intern":
        counter= commentreview.objects.filter(commentsintern=commentid, positive="N").count()
    else:
        counter= commentreview.objects.filter(commentsextern=commentid, positive="N").count()
    return counter 