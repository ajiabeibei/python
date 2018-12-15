from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from django.views import generic

from .models import Question,Choice
# Create your views here.
'''
def index(request):
	#使用Question.objects需要排序才能变成可迭代数列
	latest_question_list = Question.objects.order_by("pub_date")[:5]
	context = {"latest_question_list":latest_question_list}
	return render(request,"polls/index.html",context)


def detail(request,question_id):
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Exception:
	# 	raise Http404("Question 不存在")
	question = get_object_or_404(Question,pk=question_id)
	return render(request,"polls/detail.html",{"question":question,})



def result(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,"polls/result.html",{"question":question,})
'''
class IndexView(generic.ListView):
	#需要告诉视图latest_question_list是什么
	template_name = "polls/index.html"
	context_object_name ="latest_question_list"

	def get_queryset(self):
		return Question.objects.order_by("pub_date")[:5]

class DetailView(generic.DetailView):
	#html中的question对应就是models中的Question的字段
	model = Question
	template_name = "polls/detail.html"

class ResultView(generic.DetailView):
	model = Question
	template_name = "polls/result.html"
	


def vote(request,question_id):
	#处理表单的views函数
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST["choice"])
	except KeyError :
		return render(request,"polls/detail.html",{
			"question":question,
			"error_message":"没有做出选择，请选择",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse("polls:result",args=(question.id,)))
    	# 表单提交完成后界面刷新到对应question.id的result界面 

def clean(request,question_id):
	#通过get方法，清理表单投票机制
	question = get_object_or_404(Question,pk=question_id)
	for selected_choice in question.choice_set.order_by("id"):
		selected_choice.votes = 0
		selected_choice.save()
		
	return HttpResponseRedirect(reverse("polls:result",args=(question.id,)))
		#清空votes的数值。返回刷新到对应question.id的result界面