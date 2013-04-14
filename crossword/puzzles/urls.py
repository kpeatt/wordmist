from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from puzzles.models import Puzzle
from puzzles import views

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Puzzle.objects.all(),
            context_object_name='puzzle_list',
            template_name='puzzles/index.html'),
        name='index'),
    url(r'^(?P<puzzle_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Puzzle,
            template_name='puzzles/results.html'),
        name='results'),
)