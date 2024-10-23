from django.shortcuts import HttpResponseRedirect, render, get_object_or_404, reverse
from django.db.models import F
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")

class DetailView(generic.DetailView):
    template_name = "polls/details.html"
    model = Question

class ResultsView(generic.DetailView):
    template_name = "polls/results.html"
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = Choice.objects.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "You didn't select a choice",
        }
        return render(request, "polls/details.html", context)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))


