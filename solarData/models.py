from django.db import models

class dataSolar(models.Model):
	days = models.DateField()
	hourly = models.TimeField()
	voltage = models.FloatField()
	currents = models.FloatField()
	power = models.FloatField()
	temp = models.IntegerField()
	intensity = models.IntegerField()


	#def __str__(self):
	#	return self.voltage

