from django import forms
from .models import Category


class lcaScoreForm(forms.Form):
	cateID = 0
	categories = []
	for item in Category.objects.all():
		categories.append([cateID, item])
		cateID = cateID + 1

	category = forms.ChoiceField(widget = forms.Select(), choices = categories, required = True)

	def clean_category_name(self):
		category_name = self.cleaned_data.get('category_name')
		return category_name
	
	# classiID = 0
	# activities = []
	

	# classification = forms.ChoiceField(widget = forms.Select(), choices = activities, required = True)




# class lcaScoreForm(forms.Form):
# 	production_name = forms.CharField(label='Production Name', max_length=100)

# 	def clean_production_name(self):
# 		production_name = self.cleaned_data.get('production_name')
# 		return production_name
