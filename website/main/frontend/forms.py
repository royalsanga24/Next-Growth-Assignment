from django import forms


class AppForm(forms.Form):
    CATEGORY_CHOICES = (
    ('entertaiment','Entertainment'),
    )
    SUB_CATEGORY_CHOICES = (
    ('social media','Social Media'),
    ('games', 'Games'),
    ('finance','Finance'),
    ('education','Education'),
    ('other','Other'),
    )
    name = forms.CharField(max_length=100, required=True)
    link = forms.URLField(max_length=100, required=True)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    sub_category = forms.ChoiceField(choices=SUB_CATEGORY_CHOICES)
    points = forms.IntegerField(label="Points")

class CompleteTaskForm(forms.Form):
    file = forms.FileField(required=True)