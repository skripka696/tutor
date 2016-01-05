from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.template import RequestContext, loader


class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, pk):
    p = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn'tslect a choice. ",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(p.pk,)))
