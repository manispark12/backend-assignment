from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'language', 'question_hi', 'question_bn')
    search_fields = ('question',)
    list_filter = ('language',)

admin.site.register(FAQ, FAQAdmin)



# Register your models here.
