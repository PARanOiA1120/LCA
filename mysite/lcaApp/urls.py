from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^$', TemplateView.as_view(template_name='home.html')),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]