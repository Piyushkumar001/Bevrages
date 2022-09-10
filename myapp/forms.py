from django import forms
from .models import *

class OrderdetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ['order_id','product_id','quantity','total_price']
        widgets = {'order_id':forms.Select(attrs = {'class':'form-control'}),
		           'product_id':forms.Select(attrs = {'class':'form-control'}),
		           'quantity':forms.TextInput(attrs = {'class':'form-control'}),
				   # 'state':forms.Select(attrs = {'class':'form-control'}),
				   'total_price':forms.NumberInput(attrs = {'class':'form-control'}),
        }