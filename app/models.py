from django.db import models

# Create your models here.
class field_name(models.Model):
    name_field_value_x= (
        ('1','a'),     
        ('2', 'b'),
        ('3','c'),
    )
    name_field_value_x = models.CharField(max_length=50,default="name_field_value_x",choices=name_field_value_x)


    name_field_value_y= (
        ('1','k'),     
        ('2', 'l'),
        ('3','m'),
    )
    name_field_value_y = models.CharField(max_length=50,default="name_field_value_y",choices=name_field_value_y)