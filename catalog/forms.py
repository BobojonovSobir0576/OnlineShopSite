from django import forms
from catalog.models import *

class SeassonForm(forms.ModelForm):
    class Meta:
        model = Seasson
        fields = ("__all__")
        
class CarTypesForm(forms.ModelForm):
    class Meta:
        model = CarTypes
        fields = ("__all__")
        
class CountryManufacterForm(forms.ModelForm):
    class Meta:
        model = CountryManufacter
        fields = ("__all__")
        
class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ("__all__")
        
class GuideCharacteristicForm(forms.ModelForm):
    class Meta:
        model = GuideCharacteristic
        fields = ("__all__")
        
class GuideUnitsMeasurementForm(forms.ModelForm):
    class Meta:
        model = GuideUnitsMeasurement
        fields = ("__all__")