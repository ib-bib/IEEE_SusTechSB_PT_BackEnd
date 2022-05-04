from django.http import HttpResponseRedirect
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        seleted_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        seleted_choice.votes += 1
        seleted_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# //////////////////////////////////////////////////////////////// #
# def index(request):
#     latest_questions_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', ' .join([q.q_txt for q in latest_questions_list])
#     # template = loader.get_template('polls/index.html')
#     context = {'latest_questions_list': latest_questions_list, }
#     return render(request, 'polls/index.html', context)
#     # return HttpResponse(template.render(context, request))
#     # return HttpResponse('Hello Django, this is the index page of the polls app')


# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)

# Create your views here.
