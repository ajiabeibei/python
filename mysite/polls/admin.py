from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class ChoiceInline(admin.StackedInline):
	"""docstring for ChoiceInline"""
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	"""docstring for QuestionAdmin"""
	fieldsets = [
		( "information",  {'fields':['question_text','pub_date']}),
	]	
	inlines = [ChoiceInline]
		


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice) 


