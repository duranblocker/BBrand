from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	name = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

"""class Projects(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.ForeignKey(Post, on_delete=CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})"""

		
class Svg(models.Model):
	title = models.ForeignKey(Post, on_delete=models.CASCADE)
	wallType = models.TextField(default="wall")  # wall, parameter or roof
	wallRefNum = models.FloatField(default=1)
	path = models.TextField(default="<path d='M")
	width = models.FloatField(default=800)
	height = models.FloatField(default=800)		

	
#	def __str__(self):
#		return self.path

#	def get_absolute_url(self):
#		return reverse('svg-detail', kwargs={'pk': self.pk})

class SvgPath(models.Model):
	title = models.ForeignKey(Svg, on_delete=models.CASCADE)
	PathRefNum = models.IntegerField(1)
	pathType = models.CharField(max_length=10) # l, A, C or Q			
	startx = models.FloatField()			
	starty = models.FloatField()
	endx = models.FloatField()
	endy = models.FloatField()		
	data1 = models.FloatField()			
	data2 = models.FloatField()			
	data3 = models.FloatField()			
	data4 = models.FloatField()			
	data5 = models.FloatField()			
	data6 = models.FloatField()			
	data7 = models.FloatField()			
	data8 = models.FloatField()			
	data9 = models.FloatField()

	# def __str__(self):
	#	return self.title

	# def get_absolute_url(self):
	#	return reverse('svgpath-detail', kwargs={'pk': self.pk})

	# def __str__(self):
	#	return f'{self.user.username} Profile'

	# def save(self, **kwargs):
	#	super().save()