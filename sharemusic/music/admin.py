from django.contrib import admin
from .models import EmailAllowed,PublicPrivate,Protected
# Register your models here.
admin.site.register(EmailAllowed)
admin.site.register(PublicPrivate)
admin.site.register(Protected)
