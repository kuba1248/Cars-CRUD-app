from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Brand(models.Model):
    Brand = models.CharField(max_length=128,default='BMW',
                            help_text='The company name of the cars',
                            validators=[MinLengthValidator(3, 'minimum 3 chars')])

    class Meta:
        ordering = ['-id', '-Brand']

    def __str__(self):
        return self.Brand


class Cars(models.Model):
    BODY_STYLE_CHOICES = (
        ('car', 'седан'),
        ('suv', 'SUV'),
        ('truck', 'Pickup Truck'),
        ('van', 'Minivan'),
        ('univ', 'универсал'),
    )
    FUEL_TYPE_CHOICES = (
        ('gas', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
        ('other', 'Other'),
    )
    DRIVETRAIN_CHOICES = (
        ('AWD', 'All Wheels Drive'),
        ('FWD', 'Front Wheels Drive'),
        ('RWD', 'Rear Wheels Drive'),
        ('4*4', '4*4'),
        ('other', 'Other'),
    )
    TLIKE_CHOICES = (
        ('like', 'like'),
        ('dislike', 'dislike'),
    )
    TRATING_CHOICES = (
        ('5', 'отлично'),
        ('4', 'хорошо'),
        ('3', 'нормально'),
        ('2', 'плохо'),
        ('1', 'очень плохо'),
    )
    COLOR_TYPE_CHOICES = (
        ('black', 'black'),
        ('white', 'white'),
        ('red', 'red'),
        ('yellow', 'yellow'),
        ('green', 'green'),
    )

    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=False, related_name='cars')
    modeli = models.CharField(max_length=128, unique=True)
    probeg = models.PositiveIntegerField(null=False)

    year = models.IntegerField(default=2020)
    price = models.DecimalField(max_digits=20,decimal_places=2,default=0)
    color = models.CharField(max_length=20,default='gas',
                                 choices=COLOR_TYPE_CHOICES)

    engine = models.CharField(max_length=20,default='AWD',
                             choices=DRIVETRAIN_CHOICES)
    style = models.CharField(max_length=20,default='car',
                             choices=BODY_STYLE_CHOICES)
    fuel_type = models.CharField(max_length=100,default='gas',
                                 choices=FUEL_TYPE_CHOICES)

    comment = models.TextField(blank=True)
    i_like = models.CharField(max_length=20,default='like',
                             choices=TLIKE_CHOICES)
    i_rating = models.CharField(max_length=20,default='5',
                             choices=TRATING_CHOICES)

    class Meta:
        ordering = ['-id', '-brand']

    def is_valid_milage(self):
        return self.probeg >= 0

    def __str__(self):
        return self.modeli
