from django.db import models

class Reports(models.Model):
	date= models.CharField(max_length=50)
	number= models.IntegerField()
	crew= models.CharField(max_length=50)
	status= models.CharField(max_length=50)
	unit= models.IntegerField()


	def __str__(self):
		
		return self.date



 