from django.db import models

# Create your models here.
class Nerong(models.Model):
# 每一个类都是一个table，每个属性都是一个字段作为数据库的column名；
	nerong_id = models.IntegerField(default=0)
	nerong_title = models.CharField(max_length=200)
	nerong_text = models.CharField(max_length=600)
	def __str__(self):
		return self.nerong_title

#激活模型,创造迁移 ...makemigrations learn
#完成迁移 ...migrate learn  