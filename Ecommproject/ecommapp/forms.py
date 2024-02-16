from django import forms
from django.contrib.auth.models import User
from ecommapp.models import Cart,Orders
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User  
        fields=["first_name","last_name","email","username","password1","password2"]


class SignInForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)

# class CartForm(forms.Form):
#     quantity=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","value":1}))

class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields=["quantity"]

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=["address"]
        

