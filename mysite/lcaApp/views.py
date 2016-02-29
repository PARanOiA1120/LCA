from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf

from .forms import lcaScoreForm
from .models import Category, Classification

from brightway2 import *
from scipy.stats import kendalltau
import numpy as np



def index(request):
    db = Database("ecoinvent 3.2 cutoff")

    #classifications = [activity.get('classifications') for activity in db]

    # add item to Category
    # for classification in classifications:
    #     for item in classification:
    #         if len(Category.objects.filter(category_name = item[0])) == 0:
    #             category = Category(category_name = item[0])
    #             category.save()


    # add item to Classification
    # for classification in classifications:
    #     for item in classification:
    #         category = Category.objects.get(category_name = item[0])
    #         if len(category.classification_set.filter(classification = item[1])) == 0:
    #             category.classification_set.create(classification = item[1])
            # c = category.classification_set.filter(classification = item[1])
            # c.delete()


            

    # activities = [(activity.get('classifications'), activity.get('name')) for activity in db]

    # for activity in activities:
    #     if len(Activity.objects.filter())


    # print(db.random())

     # num_exchanges = [activity.name for activity in db]
     # print(num_exchanges)

    # LCA calculation
    # lca = LCA(demand={db.random(): 1}, method=methods.random())
    
    # LCIA correlation
    # gwp, usetox = ('IPCC 2013', 'climate change', 'GWP 100a'), ('USEtox', 'human toxicity', 'total')
    # activity = db.random()
    # lca = LCA({activity: 1}, method=gwp); 
    # lca.lci(factorize=False); 
    # lca.lcia()
    # print(lca.score)
    
    # results = np.zeros((2, 1000))
    # for x, method in enumerate((gwp, usetox)):
    #     lca.switch_method(method)
    #     for y, activity in enumerate(db):
    #         if y == 1000:
    #             break
    #         lca.redo_lcia({activity: 1})
    #         results[x, y] = lca.score

    # print(kendalltau(*results))


    form = lcaScoreForm(request.POST or None)

    c = Context({
        'form': form,
        'categories': Category.objects.all(), 
    })


    if form.is_valid():
        # instance = form.save(commit=False)
        print(request.POST.get('category_name'))


    return render(request, "lcaApp/index.html", c)
    #return HttpResponse(loader.get_template('lcaApp/index.html').render(c))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)