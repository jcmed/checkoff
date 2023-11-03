from django.db import models

class Reports(models.Model):
	date= models.CharField(max_length=50, null=True)
	number= models.IntegerField(null=True)
	crew= models.CharField(max_length=50, null=True)
	status= models.CharField(max_length=50, null=True)
	unit= models.IntegerField(null=True)


	def __str__(self):
		
		return self.date

class Checkoff(models.Model):
	unit= models.IntegerField(primary_key=True)
	miles= models.IntegerField(null=True)
	status= models.CharField(max_length=100, null=True)
	date= models.DateTimeField(null=True)
	assignment= models.CharField(max_length=100, null=True)
	unit_raw= models.CharField(max_length=100, null=True)

	def __str__(self):

		return self.unit
 