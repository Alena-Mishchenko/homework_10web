
from django import forms
from .models import Author, Quote

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ['fullname', 'born_date', 'born_location', 'description']


#     def clean_fullname(self):
#         fullname = self.cleaned_data.get('fullname')
#         if Author.objects.filter(fullname=fullname).exists():
#             raise forms.ValidationError("Author with this full name already exists.")
#         return fullname
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'born_date': forms.TextInput(attrs={'class': 'form-control'}),
            'born_location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        if Author.objects.filter(fullname=fullname).exists():
            raise forms.ValidationError("Author with this full name already exists.")
        return fullname
# class QuoteForm(forms.ModelForm):
#     class Meta:
#         model = Quote
#         fields = ['quote', 'author', 'tags']
#         widgets = {
#             'tags': forms.TextInput(attrs={'rows': 4,'placeholder': 'Enter tags, separated by commas'}),
#         }

class QuoteForm(forms.ModelForm):
    quote = forms.CharField(max_length=255,required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter quote"}))
    author = forms.ModelChoiceField(queryset=Author.objects.all().order_by('fullname'), required=True,
                                    widget=forms.Select(attrs={"class": "form-control"}))
    tags = forms.CharField(required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter tags, separated by commas"}))

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
