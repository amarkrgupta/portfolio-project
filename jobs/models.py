from django.db import models

# Create your models here.
class Job(models.Model):

	
	image=models.ImageField(upload_to='images/')		#new property callled image that will store an image like JPGs and PNGs
	summary= models.CharField(max_length=200)

	def __str__(self):
		return self.summary
