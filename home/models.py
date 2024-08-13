from django.db import models
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    city = models.CharField(max_length=200, default='')
    venuname = models.CharField(max_length=200, help_text='add venue name', default='')
    name = models.CharField(max_length=200,default='',verbose_name=' Shwo name')
    discription = models.TextField(default='')
    slug = models.SlugField(unique=True)
    platinum_seats = models.IntegerField(default=0)
    gold_seats = models.IntegerField(default=0)
    silver_seats = models.IntegerField(default=0)
    platinum_price = models.IntegerField(default=0)
    gold_price = models.IntegerField(default=0)
    silver_price = models.IntegerField(default=0)
    last_date=models.DateField(default=timezone.now)
    image = models.FileField(upload_to='home/live_show/')
    timestamp=models.DateField(default=timezone.now )

    class Meta:
        unique_together = ('slug','name')
        verbose_name='Live_Show'
        

    def __str__(self):
        return self.name

class Booking(models.Model):
    visitor_name=models.CharField(max_length=200,default='')
    phone_number=models.IntegerField(default=0)
    event_name=models.CharField(max_length=200,default='')
    platinum_seats = models.IntegerField(default=0)
    gold_seats = models.IntegerField(default=0)
    silver_seats = models.IntegerField(default=0)
    time_choice=(
        ('Moring 10-12','Moring 10-12'),
        ('12-2 ','12-2'),
        ('2-4','2-4'),
        ('4-6','4-6'),
        ('6-8','6-8'),        
        ('night 8-10','night 8-10'),
    )

    time_preference=models.CharField(max_length=20,choices=time_choice,default=0)
    booking_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.visitor_name

class CheckOut(models.Model):
    booking_id= models.AutoField(primary_key=True)
    net_price=models.IntegerField()
    name=models.CharField(max_length=90)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.IntegerField()
# class BookinValidation(models.Model):
#     visitor_name=models.CharField(max_length=200,default='')
#     phone_number = models.IntegerField(default=0)
#     time_preference = models.CharField(max_length=10, default=0)
#     platinum_seats = models.IntegerField(default=0)
#     gold_seats = models.IntegerField(default=0)
#     silver_seats = models.IntegerField(default=0)
#     booked_date=models.DateField(default=timezone.now)
#
#     def __str__(self):
#         return self.visitor_name
#
#

