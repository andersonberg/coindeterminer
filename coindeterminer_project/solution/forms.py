from django import forms

class InputForm(forms.Form):
    input_file = forms.FileField(label='Choose a file')
