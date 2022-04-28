from django.http import HttpResponse
from .models import Question
# from django.template import loader
from django.shortcuts import render, get_object_or_404


def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', ' .join([q.q_txt for q in latest_questions_list])
    # template = loader.get_template('polls/index.html')
    context = {'latest_questions_list': latest_questions_list, }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # return HttpResponse('Hello Django, this is the index page of the polls app')


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
