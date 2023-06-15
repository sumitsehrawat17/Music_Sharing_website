from django.db import models
from users.models import CustomUser
from django.core.validators import FileExtensionValidator
import os
# Create your models here.

class EmailAllowed(models.Model):
    email = models.EmailField(primary_key=True)


def get_upload_path(instance, filename):
    return os.path.join('music', filename)

class Music(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path,validators=[FileExtensionValidator(allowed_extensions=['mp3','wav'])])
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class PublicPrivate(Music):
    type_of = models.CharField(choices=[("public","Public"),("private","Private")],max_length=7)
    

class Protected(Music):
    allowed_emails = models.ManyToManyField(EmailAllowed)


