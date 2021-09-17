from django import forms
from cart.models import Cart
# 클라이언트 화면에 입력 폼을 만들어주려고
# 클라이언트가 입력한 데이터에 대한 전처리

class AddProForm(forms.Form):
    amount = forms.IntegerField(label='수량', initial=1,min_value=1)

class SearchForm(forms.Form):
    search_word = forms.CharField(max_length=100)