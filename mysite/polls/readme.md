## django笔记

* 命令安装django,pip install django2.0.2

* 检查是否安装成功

  * python3   import django  django.VERSION

### 新建项目



* django-admin startproject mysite 项目名称为mysite

* 目录结构为

  > mysite/
  > 
  >     manage.py
  >     mysite/
  >     __init__.py
  >     setting.py
  >     urls.py
  >     wsgi.py

* 运行站点服务器 python manage.py runserver

      *   runserver 自动加载

* 检验打开浏览器[http://127.0.0.1:8000/](http://127.0.0.1:8000/) 不行换端口

  ### 新建app

* python manage.py startapp polls app名称为polls

* 将app名称添加到setting.py中的INSTALLED_APPS=["polls.apps.PollsConfig",]不要忘记逗号

* 设置数据库绑定，默认使用sqlite3

* 编辑polls/views.py

  * 导入from django.http HttpResponse*   def index(request)
  * return HttpResponse"返回HttpResponse内容不常用"
  * 使用较多的是from django.shortcuts import render 返回是 return render(request,"polls/XXX.html",context)
  * context是字典类型，可以包含模型中的数据、没有可以省略
  * views中的函数接受第一个参数是 request

* 新建polls/urls.py

  * from django.urls import path 和  .  views
  * 新建 urlpatterns 数组path( "",views.index,name="index"),
  * path函数有四个参数，route是URL检索匹配用的正则表达式，view是调用视图中的函数，kwargs传递信息不常用，name
  * path的第一个参数，可以包含<int:nmb>使nmb作为形参传递，传递字符串直接使用<>

* 将polls的urls.py添加到站点的mysite/urls.py

* 导入 from django.urls import include urlpatterns 数组添加path("polls/",include("polls.urls")),

* 运行站点服务器浏览器打开[http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/)

  ### 创建model

* class Question(models.Model):学习models.Model类的属性和方法

* question_text=models.CharField(max_length=200)

* 每一个类都是一个table，每个属性都是一个字段作为数据库的column名,字段类型可以是IntegerField、CharField、DateField

* 可以创建数据库表的关系

* def **str**(self):函数方便识别Question.object

* 激活模型，创造迁移 makemigration polls , 执行迁移 migrate

* 创建管理员用户 createsuperuser(uesr:jbb,password:123456)

* admin.py中添加模型admin.site.register(polls)

* 登录 [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) 给模型添加数据

  ### 编辑templates

* 新建文件夹/mysite/polls/temlpates/polls

* 存放views的render第二个参数"polls/XXX.html"文件

* from .models import Question 引用数据时使用 data = Question.objects.order_by("question")使用时将表数据排序才能索引

* comtext={"data_name_":data,}  "data_name_"是data数据在html中引用的名字

* 在HTML中{{数据}} 逻辑语言使用{% if a!=true %}  执行语句 {% endif %}  {% for a in list %}  执行语句 {% endfor %}

* URL命名空间href={% url polls:index data %}

* url是指urls.py的app_name属性index指的是url.py中的path的name参数

* 数据库库中为每个字段创建primary_id默认从1 开始，而不是list的检索序号 所以可以使用question.id在html中，在url中可以使用question_id作为形参

* Question.objects具有get(question_id)方法，

  ### 404界面

* from django.http import Http404 抛出Http404异常

* 或者使用 from django.shortcuts import get_object_or_404

  * get_object_or_404(Question，pk=question_id)函数第一个参数model名称，第二个数字作为Question.objects的get方法参数

### 表单form界面

* html界面编辑表单、from标签的action属性为处理表单数据的{%url"polls:vote"question.id%}method为"post"传递大量表单数据不建议使用get

  - {% csrf_token %}放在form标签后面防止恶意攻击

  * input标签的name属性、value属性对应传递处理数据时使用的 数据库字段名和字段值
  * for循环，forloop.counter表示循环次数
  * 提交表单的submit，不要忘了。

* views处理传递进的数j据  

  - request.POST["var_name"]，是一个字典类似的对象，可以获得访问提交的数据

  * 通过models.Model类的属性和方法，set和get方法改变数据库表存放值
  * 表单提交完成后界面刷新到对应question.id的result界面,可以返回http.HttpResponseRedirect(reverse("",args=()))

### 使用通用视图

* 导入django.views的generic类，通用视图类generic.BaseView中的as_view()函数

* 在url.py中path函数的第二个参数变为IndexView.as_view(),传递的参数为pk,对于没有html的vote不用改动

* view.py视图class类IndexViews继承自(grneric.ListView)，参数的值需要使用函数声明

  - context_object_name被赋值的变量名

  * def建立返回队列的函数get_queryset返回list对象Question.objects.order_by("pub_date")[:5]
  * view.py视图class类DetailView继承自(grneric.DetailView)，参数的值均为Questoin的字段
  * model=Question、声明模板template_name="appname/index.html"

### 测试text
* 编写test.py文件，运行 ~ test polls  

### 静态文件
* html模板的style样式文件可以放在polls/static/polls/style.css,引用时的链接可以是{% load static %}生成静态文件绝对网址
href="{% static 'polls/style.css'%}"
* html模板的图片image文件可以放在polls/static/polls/images/tupian.jpg下,引用时的链接可以是url('images/tupian.jpg')

### admin管理界面
* 在polls/admin.py中添加包含Fieldset属性的继承子类，管理admin界面QuestionAdmin(admin.ModelAdmin):
* fieldsets=['界面','存放顺序']，也可以分组别名，定义多列继承其他类

### 定制打包站点
* 在站点目录包含manage下新建文件夹templates/admin
* settings.py添加TEMPLATES=[]数组，内容的作用是一个加载路径
* polls/setup.py设置打包站点的信息
* 新建polls/MANIFEST.in文件，包括打包内容、在执行python setup.py sdist打包

