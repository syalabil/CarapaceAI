from django.contrib import admin
from .models import *

# Register your models here.

class HistoryAdmin(admin.ModelAdmin):
    model = History
    list_display = ['id', 'result_video','tested_on',"passed"]

admin.site.register(History,HistoryAdmin)
admin.site.register(Video)
