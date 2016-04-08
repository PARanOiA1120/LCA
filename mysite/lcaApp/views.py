from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf

from .forms import lcaScoreForm
from .models import Category, Classification, Activity, Methods

from brightway2 import *
from scipy.stats import kendalltau
import numpy as np



def index(request):
    db = Database("ecoinvent 3.2 cutoff")

    #setting up database
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
            

    # activities = [activity for activity in db]
    # for activity in activities:
    #     for classi in activity.get('classifications'):
    #         category = Category.objects.get(category_name = classi[0])
    #         classification = Classification.objects.get(category = category, classification = classi[1])
    #         if len(Activity.objects.filter(category = category, classification = classification, activity_name = activity.get('name'))) == 0:
    #             ac = Activity(category = category, classification = classification, activity_name = activity.get('name'))
    #             ac.save()



    # LCA calculation
    # lca = LCA(demand={db.random(): 1}, method=methods.random())
    
    # LCIA correlation

    
    # results = np.zeros((2, 1000))
    # for x, method in enumerate((gwp, usetox)):
    #     lca.switch_method(method)
    #     for y, activity in enumerate(db):
    #         if y == 1000:
    #             break
    #         lca.redo_lcia({activity: 1})
    #         results[x, y] = lca.score

    # print(kendalltau(*results))

    # for method in methods.items():
    #     if len(Methods.objects.filter(method = method[0])) == 0:
    #         m = Methods(method = method[0])
    #         m.save()


    form = lcaScoreForm(request.POST or None)

    context = {
        'form': form,
        'categories': Category.objects.all(), 
        'category_picked':'',
        'classifications':'',
        'classification_picked': '',
        'activities': '',
        'activity_picked': '',
        'methods': '',
        'method_picked': '',
        'lcaScore': '',
    }

    if form.is_valid():
        # instance = form.save(commit=False)
        category_selected = request.POST.get("Category")
        classification_selected = request.POST.get("Classification")
        activity_selected = request.POST.get("Activity")
        method_selected = request.POST.get("Method")
        filtered_acti = ''
        lcaScore = ''

        #filter classification list based on category selected
        cate_Obj = Category.objects.get(category_name = category_selected)
        filtered_classi = cate_Obj.classification_set.all()

        context = {
            'form': form,
            'categories': Category.objects.all(),
            'category_picked':category_selected, 
            'classifications': filtered_classi,
            'classification_picked': '',
            'activities': '',
            'activity_picked': '',
            'methods': '',
            'method_picked': '',
            'lcaScore': '',
        }


        #filter activity list based on category and classification selected
        if(classification_selected != None):
            classi_Obj = Classification.objects.get(category = cate_Obj, classification = classification_selected)
            filtered_acti = [ac.activity_name for ac in Activity.objects.filter(category = cate_Obj, classification = classi_Obj)]
            context = {
                'form': form,
                'categories': Category.objects.all(),
                'category_picked':category_selected, 
                'classifications': filtered_classi,
                'classification_picked': classification_selected,
                'activities': filtered_acti,
                'activity_picked': '',
                'methods': Methods.objects.all(),
                'method_picked': '',
                'lcaScore': '',
            }




        if(activity_selected != None):
            ac_level = request.POST.get("Level")
            
            tmp = method_selected.replace(")", "")
            tmp = tmp.replace("(", "")
            tmp = tmp.replace("\'", "")
            arr = tmp.split(", ")

            method = (arr[0], arr[1], arr[2])


            
            for activity in db:
                if (activity.get('name') == activity_selected):
                  
                    lca = LCA({activity: ac_level}, method = method); 
                    lca.lci(factorize=False); 
                    lca.lcia()
                    lcaScore = lca.score
                    break

            context = {
                'form': form,
                'categories': Category.objects.all(),
                'category_picked':category_selected, 
                'classifications': filtered_classi,
                'classification_picked': classification_selected,
                'activities': filtered_acti,
                'activity_picked': activity_selected,
                'methods': Methods.objects.all(),
                'method_picked': method_selected,
                'level': ac_level,
                'lcaScore': '',
            }


    return render(request, "lcaApp/index.html", context)




def contact(request):
    form = ContactForm(request.POST or None)

    context = {
        'form': form,
    }
    return render(request, "lcaApp/contact.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)