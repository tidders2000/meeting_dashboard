from django.contrib import admin
from .models import Risk, Action, Rag

# Register your models here.
admin.site.register(Risk)
admin.site.register(Action)
admin.site.register(Rag)
