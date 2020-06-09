from django.db import models

class Choice(models.Model):
	types = (
		('tech','tech'),
		('social','social'),
		('travel','travel'),
		('food','food'),
		('others','others'),
		)
	name = models.CharField(max_length=10,choices=types,default='others')

	def __str__(self):
		return self.name

class Authors(models.Model):
	author_name = models.CharField(max_length=15,blank=False)

	def __str__(self):
		return self.author_name


class Blog(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(max_length=2000)
	publish_date = models.DateTimeField(auto_now_add=True)
	category = models.ManyToManyField(Choice) 
	author = models.ForeignKey(Authors,on_delete=models.CASCADE)
	image = models.ImageField(null=True)

	class Meta:
		ordering = ['-publish_date']
	
	def __str__(self):
		return f'{self.title} ({self.publish_date})'



