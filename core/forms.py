from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML


class ContactForm(forms.Form):  # Formulario crispy-forms con Bootstrap 5
    nombre = forms.CharField(
        label='Nombre completo',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre completo'
        })
    )

    email = forms.EmailField(
        label='Correo electrónico',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        })
    )

    asunto = forms.CharField(
        label='Asunto',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '¿Sobre qué quieres contactarnos?'
        })
    )

    mensaje = forms.CharField(
        label='Mensaje',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Escribe tu mensaje aquí...'
        })
    )

    tipo_consulta = forms.ChoiceField(
        label='Tipo de consulta',
        required=False,
        choices=[
            ('', 'Selecciona un tipo'),
            ('general', 'Consulta General'),
            ('prensa', 'Prensa y Medios'),
            ('colaboracion', 'Colaboración'),
            ('partnership', 'Partnership'),
            ('otro', 'Otro'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()  # Configuración crispy-forms
        self.helper.form_method = 'post'
        self.helper.form_class = 'contact-form'
        self.helper.attrs = {'novalidate': ''}

        self.helper.layout = Layout(  # Layout responsivo Bootstrap 5
            Row(
                Column('nombre', css_class='col-md-6 mb-3'),  # 2 columnas
                Column('email', css_class='col-md-6 mb-3'),
            ),
            Row(
                Column('asunto', css_class='col-md-12 mb-3'),
            ),
            Row(
                Column('tipo_consulta', css_class='col-md-12 mb-3'),
            ),
            Row(
                Column('mensaje', css_class='col-md-12 mb-3'),
            ),
            Submit('submit', 'Enviar Mensaje', css_class='btn btn-primary btn-lg w-100'),
        )

