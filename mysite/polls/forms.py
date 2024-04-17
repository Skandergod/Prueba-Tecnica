from django import forms  
from polls.models import Pizza  

class PizzaForm(forms.ModelForm):  

    class Meta:  
        model = Pizza  
        fields = "__all__"  