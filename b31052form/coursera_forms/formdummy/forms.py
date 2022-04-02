#forms.py 
from distutils.command.clean import clean
from django import forms

class	DjangoForm(forms.Form):
  text = forms.CharField(label='Отзыв',  
  max_length=10) 
  grade = forms.IntegerField(label='Оценка', min_value=1, max_value=100)
  image = forms.FileField(label='Фотография', initial='cccc')


  def clean_text(self):
    if "abc" not in self.cleaned_data['text']:
      print(111)
      raise forms.ValidationError('Вы не о том пишете')
    pass

