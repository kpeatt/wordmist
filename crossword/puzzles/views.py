from django.views.generic import ListView, DetailView

from puzzles.models import Puzzle

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
        contents = puzzle.read_puzzle()
        context['clues'] = contents.clue_numbering()
        
        return context