from django.db import models

class Choice(models.Model):
	options = (
		('web','web'),
		('linux','linux'),
		('cloud','cloud'),
		('others','others')
		)
	name = models.CharField(max_length=10,choices=options,default='others')
	def __str__(self):
		return self.name

class Author(models.Model):
	author_name = models.CharField(max_length=15,blank=True)
	def __str__(self):
		return self.author_name


class Blog(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(max_length=5000)
	publish_date = models.DateTimeField(auto_now_add=True)
	category = models.ManyToManyField(Choice,default='others') 
	author = models.ForeignKey(Author,on_delete=models.CASCADE)
	image = models.ImageField(blank=True)
	class Meta:
		ordering = ['-publish_date']
		
	def __str__(self):
		return f'{self.title} - {self.author}'

	def save(self, *args, **kwargs):
		self.title = self.title.lower()
		return super(Blog, self).save(*args, **kwargs)



