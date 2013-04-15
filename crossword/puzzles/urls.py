from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from puzzles.models import Puzzle
from puzzles import views

urlpatterns = patterns('',
    url(r'^$',
        views.PuzzleListView.as_view(),
        name='list'),

    url(r'^(?P<pk>\d+)/$',
        views.PuzzleDetailView.as_view(),
        name='detail'),
    url(
        r'^api/(?P<pk>[-\w]+)/$',
        views.PuzzleObjectApiView.as_view(),
        name='puzzle_object_api'
    ),
)