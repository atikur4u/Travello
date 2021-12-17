from django.db import models

# Create your models here.
class Destinations(models.Model):
    destination_image = models.ImageField(upload_to='pics')
    spec_offer_text_center = models.BooleanField(default=False)
    destination_title = models.CharField(max_length=30)
    destination_subtitle = models.TextField()
    destination_price = models.IntegerField()

    stars = (
        ('5 Stars Hotel', '5 Star'),
        ('4 Stars Hotel','4 Star'),
        ('3 Stars Hotel', '3 Star'),
        ('2 Stars Hotel', '2 Star'),
        ('1 Stars Hotel', '1 Star'),
        ('0 Stars Hotel', '0 Star'),
    )
    Stars_Hotel = models.CharField(max_length=32, choices=stars, default="0 Stars Hotel")

    Incl = (
        ('Partially Subsidized' , 'Partially Subsidized'),
        ('All Inclusive', 'All Inclusive'),
    )
    Inclusive = models.CharField(max_length=20, choices=Incl, default='Partially Subsidized')
    
    
    Flight_tickets = models.BooleanField(default=False)
    
    
    Guided_visits = models.BooleanField(default=False)