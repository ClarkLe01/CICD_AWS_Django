from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Question,Choice

import math
class Circle:
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError('The radius cannot be negative')

        self._radius = radius

    def area(self) -> float:
        return math.pi * math.pow(self._radius, 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

def sum(a, b):
    return a + b

class HomeView(TemplateView):
    template_name = "myapp/home.html"

    def get_context_data(self, **kwargs):
        assets = ["Điện thoại","PC","Laptop"]
        cname = "Devices"
        kwargs = {'name':cname,'assets':assets}
        return super().get_context_data(**kwargs)

def viewlist(request):
    list_question = Question.objects.all()
    # list_question = get_object_or_404(Question,pk=2)
    context = {"dsquest":list_question}
    return render(request,"polls/question_list.html",context)

def detailView(request,question_id):
    q = Question.objects.get(pk=question_id)
    context = {"qs":q}
    return render(request,"polls/detail_question.html",context)

def vote(request,question_id):
    q = Question.objects.get(pk=question_id)
    try:
        catched_data = request.POST["choice"]
        a = q.choice_set.get(pk=catched_data)
        
    except:
        return HttpResponse("Lỗi không có choice")
    a.vote = utils.sum(a.vote,1)
    a.save()
    context = {"q":q}
    return render(request,"polls/result.html",context)