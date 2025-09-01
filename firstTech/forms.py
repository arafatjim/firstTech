from django import forms
class UserForm(forms.Form):
          n1 = forms.CharField(label='Number 1', max_length=100, widget=forms.NumberInput(attrs={'placeholder':'Enter Number 1'}))

          n2 = forms.CharField(label='Number 2', max_length=100, widget=forms.NumberInput(attrs={'placeholder':'Enter Number 1'}))
          email= forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'placeholder':'Enter Email'}))