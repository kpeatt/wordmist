from django.views.generic import ListView, DetailView, View
from django.views.generic.detail import SingleObjectMixin

from core.views import ObjectApiMixin
from puzzles.models import Puzzle, Source

# Mixins

# Classes

class PuzzleListView(ListView):
    model = Puzzle

class PuzzleDetailView(DetailView):
    context_object_name = "puzzle"
    model = Puzzle

    def get_context_data(self, **kwargs):
        context = super(PuzzleDetailView, self).get_context_data(**kwargs)

        # Get all the clues and number them
        puzzle = self.get_object()
        context['clues'] = puzzle.get_clues()

        return context

# APIs

class PuzzleObjectApiView(ObjectApiMixin, View):
    model = Puzzle
