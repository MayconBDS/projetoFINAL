from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Deixe sua opinião...'}),
        }
