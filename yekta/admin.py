from django.contrib import admin
from .models import URL
from .models import RequestLog

admin.site.register(URL)
admin.site.register(RequestLog)