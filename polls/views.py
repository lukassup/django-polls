# -*- coding: utf-8 -*-

"""polls views."""

from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    """polls recent questions index view."""

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        now = timezone.now()
        return Question.objects.filter(pub_date__lte=now).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """polls question detail view."""

    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """polls question results view."""

    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, pk):
    """polls question vote view."""
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) as e:
        # redisplay the voting form with errors
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # NOTE: avoid race conditions
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id, )))
