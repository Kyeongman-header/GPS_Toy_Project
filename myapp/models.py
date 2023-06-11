from django.db import models
from django.utils import timezone

 
# Create your models here.
class arduino(models.Model):
    name=models.CharField(max_length=200)
    langitude=models.FloatField(default=0)
    longitude=models.FloatField(default=0)
    pub_date=models.DateTimeField(auto_now=True)

    def to_json(self):
    	return {
            "name": self.name,
            "langitude": self.langitude,
            "longitude": self.longitude,
            "pub_date": self.pub_date,
        }
