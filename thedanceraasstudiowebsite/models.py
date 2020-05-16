from django.db import models

class userDetails(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    email=models.EmailField(max_length=256)
    message=models.CharField(max_length=3000,blank=True,null=True)

    def __str__(self):
        return self.name