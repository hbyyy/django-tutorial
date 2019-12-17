from django.http import HttpResponse, Http404
# Create your views here.
from django.shortcuts import render
from django.template import loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {
        'question': question,
    }
    # return HttpResponse(f"You're looking at question {question_id}.")
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "you're looking at the results of question {}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
