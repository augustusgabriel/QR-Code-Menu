from django import forms


class QrCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=50,
        label='Nome do Restaurante',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do Restaurante',
        })
        )
    url = forms.URLField(
        max_length=200,
        label='Menu URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite a URL do menu',
        })
        )