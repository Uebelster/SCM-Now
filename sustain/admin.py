from django.contrib import admin
from .models import account, accountbusinesstype, businesstype, report, reporttype, participant, article, commentsintern, commentsextern, commentreview

admin.site.register(account)
admin.site.register(accountbusinesstype)
admin.site.register(businesstype)
admin.site.register(report)
admin.site.register(reporttype)
admin.site.register(participant)
admin.site.register(article)
admin.site.register(commentsintern)
admin.site.register(commentsextern)
admin.site.register(commentreview)

# Register your models here.
