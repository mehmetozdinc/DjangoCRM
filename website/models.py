from django.db import models

class Record(models.Model):
    created_date=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=20)

    def __str__(self):
        return ("{}{}".format(self.first_name,self.last_name))
    
    class Meta:
        ordering = ('id',)
