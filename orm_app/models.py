from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	city = models.CharField(max_length=100)
	contact_number = models.IntegerField()
	image = models.ImageField(upload_to="static/profile_image", null=True, blank=True)
	pub_date=models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return self.user.username

class Post_ad(models.Model):
	title= models.CharField(max_length=100)
	description = models.TextField()
	image=models.ImageField(upload_to='static/product_image')
	price=models.IntegerField()
	pub_date=models.DateTimeField(auto_now_add=True)
	profile = models.ForeignKey(
		Profile,
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return self.title
