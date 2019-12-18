from django.http import HttpResponse, Http404
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from polls.models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # == question = get_object_or_404(Question, pk = question_id)

    context = {
        'question': question,
    }
    # return HttpResponse(f"You're looking at question {question_id}.")
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # choices = question.choice_set.all()
    context = {'question': question}
    return render(request, 'polls/results.html', context)
    # response = "you're looking at the results of question {}"
    # return HttpResponse(response.format(question_id))


def vote(request, question_id):
    # 특정 Question에 해당하는
    # 특정 Choice의 votes를 1 늘리기

    # 이후 특정 Question에 해당하는 results 페이지로 이동
    if request.method == 'POST':
        # GET으로 전달된 question_id에 해당하는 Question객체
        question = get_object_or_404(Question, pk=question_id)
        choice_pk = request.POST['choice']
        choice = get_object_or_404(Choice, pk=choice_pk)
        choice.votes += 1
        choice.save()
        return redirect('polls:results', question_id=question_id)

    # return HttpResponse(f"You're voting on question {question_id}")
