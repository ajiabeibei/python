from django.db import models

from django.utils import timezone

# Create your models here.
class Question(models.Model):
	#继承自models.Model
	#问题内容，展现在数据库，pub_date数据录入时间
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField("date published")

	def __str__(self):
		return self.question_text


class Choice(models.Model):
	'''建立两个model，（问题，时间）（意见，票数）'''
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
	 	return self.choice_text

		
		