from django.db import models

class Inventory(models.Model):
	code = models.CharField(unique=True, max_length=25)
	name = models.CharField(max_length= 80)
	category = models.CharField(max_length = 80)
	price_1 = models.FloatField()
	price_2 = models.FloatField()
	price_3 = models.FloatField()
	price_4 = models.FloatField()
	download = models.BooleanField(default=False)

	def __str__(self):
		return self.name +' | '+self.code

