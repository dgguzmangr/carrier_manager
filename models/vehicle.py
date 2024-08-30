from tortoise import fields
from tortoise.models import Model

class Vehicle(Model):
    id = fields.IntField(pk=True)
    identification = fields.CharField(max_length=50)
    long = fields.FloatField()
    width = fields.FloatField()
    high = fields.FloatField()
    weight = fields.FloatField()
    
    class Meta:
        table = "vehicles"
