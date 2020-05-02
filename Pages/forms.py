from django import forms

class ContactForm(forms.Form):
    dim1 = forms.IntegerField(max_value=10000)
    dim2 = forms.IntegerField(max_value=10000)
    dim3 = forms.IntegerField(max_value=10000)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)
