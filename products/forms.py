from django import forms
from products.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category #Category Table
        fields = "__all__" # its load all category field from bakend
        #fields = {'name'} #this is manual 

        #fields = "__all__" # its exclude name field and loaded rest of left field from backend
        #exclude = ['name']
        
    def clean_name(self):
         print("clean name", self.cleaned_data['name'])
         return self.cleaned_data


     
