from django.db import models		# import means import another files components
from django.utils import timezone

class Post(models.Model):						# definition of a model, Post is the name of model (it always write down in Capital letters)
	author = models.ForeignKey('auth.User')		# link of another model's
	title = models.CharField(max_length=200)	# the number of letter is limited by max_length
	text = models.TextField()
	created_date = models.DateTimeField(
			default = timezone.now)
	published_date = models.DateTimeField(
			blank = True, null = True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title	
