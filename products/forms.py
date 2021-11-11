""" This sets the form parameters for Profile app"""
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Department


class ProductForm(forms.ModelForm):
    """ A form which contains product information """

    class Meta:
        """ This class defines meta behaviour of above class """
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label="Image", required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        departments = Department.objects.all()
        display_names = [(d.id, d.get_display_name()) for d in departments]

        self.fields['department'].choices = display_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
