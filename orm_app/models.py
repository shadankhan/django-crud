from django.db import models

# Create your models here.
class Recruiter(models.Model):
	name = models.CharField(max_length=100)
	number = models.IntegerField()

	def __str__(self):
		return self.name

class Candidate(models.Model):
	name= models.CharField(max_length=100)
	recruiter = models.ManyToManyField(
		Recruiter,
		)

	def __str__(self):
		return self.name
