from django.db import models

class Github(models.Model):
    login = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    #avatar = models.ImageField(upload_to='avatar_media', null=True ,blank=True)

    def __str__(self):
        return self.login
