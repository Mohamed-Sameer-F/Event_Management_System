from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=50)
    attendees=models.IntegerField()
    def __str__(self):
        return self.title

class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_ph=models.CharField(max_length=12)
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

