from django import forms

class ContatoForm(forms.Form):
    telefone = forms.CharField(
        label="Telefone",
        max_length=19,
        widget=forms.TextInput(
            attrs={
                'placeholder': '+ (99) 99999-9999',
                'id': 'Cellphone',
            }
        )
    )
