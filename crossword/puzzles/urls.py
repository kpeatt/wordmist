from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from puzzles.models import Puzzle
from puzzles.views import PuzzleListView, PuzzleDetailView

urlpatterns = patterns('',
    url(r'^$',
        PuzzleListView.as_view(),
        name='list'),

    url(r'^(?P<pk>\d+)/$',
    PuzzleDetailView.as_view(),
    name='detail'),
)