from django import forms
from app_recipes.models import Dishes, StepDishes, Comments, Category


class DishesForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'add__input',
                                                                    'placeholder': 'Введите название'}))
    descr = forms.CharField(label='', required=False, widget=forms.Textarea(
        attrs={'class': 'add__area', 'placeholder': 'Можете оставлять любые описания, ссылки и т.д.'}))

    cat_id = forms.ModelChoiceField(label='', queryset=Category.objects.all(), empty_label=None,
                                    widget=forms.Select(attrs={'class': 'add__select'}))
    photo = forms.ImageField(label='', widget=forms.FileInput(attrs={'class': 'add__photo'}))
    video = forms.FileField(label='', widget=forms.FileInput(attrs={'class': 'add__video'}), required=True)

    class Meta:
        model = Dishes
        fields = 'title', 'descr', 'cat_id', 'photo', 'video'

        # widget = forms.FileInput(attrs={'class': 'add__photo'}


class StepsForm(forms.ModelForm):
    class Meta:
        model = StepDishes
        fields = 'pic', 'desc'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
