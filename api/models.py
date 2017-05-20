from django.db import models

# Create your models here.
from django.db import models

class BucketList(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    date_created= models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now= True)

    def __str__(self):
        return "{}".format(self.name)



