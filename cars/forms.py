from django import forms
from cars.models import Brand, Cars


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'
