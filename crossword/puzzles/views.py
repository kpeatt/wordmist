from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from puzzles.models import Puzzle

def index(request):
    puzzle_list = Puzzle.objects.all()
    context = {
        'puzzle_list': puzzle_list,
    }
    return render(request, 'puzzles/index.html', context)

def detail(request, puzzle_id):
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
    contents = puzzle.read_puzzle()
    clues = contents.clue_numbering()
    return render(request, 'puzzles/detail.html', {
    	'puzzle': puzzle,
    	'clues': clues
    })