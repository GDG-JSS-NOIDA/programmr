from django.conf import settings

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GoogleProfile(models.Model):

	user = models.ForeignKey(User)
	google_user_id = models.CharField(max_length=100)
	access_token = models.CharField(max_length=100)

	def __unicode__(self):
		return self.user.username


class UserProfile(models.Model):
	
	user = models.ForeignKey(User)
	name=models.CharField(max_length=120)
	email_ID=models.EmailField(max_length=200, blank=True)
	avatar=models.URLField(max_length=120)
	year=models.CharField(max_length=120)
	branch=models.CharField(max_length=120)
	mobile_no=models.CharField(max_length=120)
	timestamp=models.DateTimeField(auto_now=True,auto_now_add=False)
	total_score=models.IntegerField(default=0)

	def __unicode__(self):
		return self.name



class Question(models.Model):
	
	title=models.CharField(max_length=120)
	detail=models.TextField()
	constraint=models.CharField(max_length=120)
	input_format=models.TextField()
	output_format=models.TextField()
	sample_testcase=models.TextField()
	testcase_input=models.FileField(upload_to="Testcase",max_length=100)
	testcase_output=models.FileField(upload_to="Testcase",max_length=100)
	total_submissions=models.IntegerField(default=0)
	correct_submissions=models.IntegerField(default=0)
	accuracy=models.DecimalField(max_digits=5, decimal_places=2, default=0)
	

	def __unicode__(self):
		return self.title



class Submission(models.Model):

	ques_ID = models.ForeignKey(Question)
	user_ID=models.CharField(max_length=120)
	question_ID=models.CharField(max_length=120)
	status=models.CharField(max_length=120)
	source_code_URL=models.URLField(max_length=120)
	date=models.DateTimeField(auto_now=True,auto_now_add=False)

	def __unicode__(self):
		return self.status


class Announcement(models.Model):
	announcement=models.TextField()
	image = models.ImageField(upload_to="images", blank=True)

	def __unicode__(self):
		return self.announcement


