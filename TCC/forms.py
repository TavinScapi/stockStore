from django import forms
from .models import Fornecedor, Produto

from django import forms

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'endereco', 'telefone', 'email', 'servicos', 'foto']  # Adiciona 'foto' aos campos


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade', 'categoria', 'fornecedor', 'estoque_minimo', 'estoque_maximo']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descrição do produto'}),
            'estoque_minimo': forms.NumberInput(attrs={'placeholder': 'Estoque mínimo'}),
            'estoque_maximo': forms.NumberInput(attrs={'placeholder': 'Estoque máximo'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['fornecedor'].queryset = Fornecedor.objects.all()



# forms.py
from django import forms
from .models import Funcionario

class CadastroFuncionarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Funcionario
        fields = ['firstname', 'lastname', 'email', 'phone', 'username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# forms.py
from django import forms
from .models import Funcionario

# forms.py
from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['firstname', 'lastname', 'email', 'phone', 'username', 'photo']

class FuncionarioForm2(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['firstname', 'lastname', 'email', 'phone', 'username', 'password']

