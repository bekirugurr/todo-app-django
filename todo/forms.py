from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):
        
    class Meta:
        model = Todo
        fields = '__all__'
        # is_done = forms.BooleanField(widget=forms.HiddenInput(), initial=False) 
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '⚡ Enter task title', 'class': 'input-style', 'style' : 'padding: .5rem 1rem; border-color: #0D6EFD;'}),
            
            'content': forms.Textarea(attrs={'placeholder': '💪 What are you going to do?', 'class': 'input-style', 'rows' :3,'col':120, 'style':'resize:none; padding: .5rem 1rem;  border-color: #0D6EFD;' }),

            'priority': forms.Select(attrs={'class': 'input-style', 'style' : 'padding: .5rem 1rem; border-color: #0D6EFD; width: calc(100% - 5rem);'}),
            
            'tag': forms.TextInput(attrs={'placeholder': '🔖 Enter task tag ', 'class': 'input-style', 'style' : 'padding: .5rem 1rem; border-color: #0D6EFD; width: calc(100% - 5rem);'}),
        }
        

