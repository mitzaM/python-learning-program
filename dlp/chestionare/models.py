from django.db import models

# Create your models here.

class Test(models.Model):
	name = models.CharField(max_length = 200)
	description = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name

class Page(models.Model):
	order = models.IntegerField()
	test = models.ForeignKey(Test)
	def __unicode__(self):
		return str(self.order)

class Question(models.Model):
	text = models.CharField(max_length = 200)
	page = models.ForeignKey(Page)
	def __unicode__(self):
		return self.text

class Result(models.Model):
	text = models.CharField(max_length = 200)
	limit = models.IntegerField()
	test = models.ForeignKey(Test)
	def __unicode__(self):
		return self.text

class Response(models.Model):
	text = models.CharField(max_length = 200)
	score = models.IntegerField()
	question = models.ForeignKey(Question)
	def __unicode__(self):
		return self.text
