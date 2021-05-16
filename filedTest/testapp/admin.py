from django.contrib import admin
from . models import song
from . models import podcast
from . models import audiobook
# Register your models here.
admin.site.register(song)
admin.site.register(podcast)
admin.site.register(audiobook)
