from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML

# Formulario de contacto usando crispy-forms con Bootstrap 5
class ContactForm(forms.Form):
    # Campo de nombre completo
    nombre = forms.CharField(
        label='Nombre completo',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre completo'
        })
    )

    # Campo de email válido
    email = forms.EmailField(
        label='Correo electrónico',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        })
    )

    # Campo de asunto del mensaje
    asunto = forms.CharField(
        label='Asunto',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '¿Sobre qué quieres contactarnos?'
        })
    )

    # Campo de mensaje principal (textarea)
    mensaje = forms.CharField(
        label='Mensaje',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Escribe tu mensaje aquí...'
        })
    )

    # Selector de tipo de consulta (opcional)
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

    # Configuración crispy-forms para el layout

    # self: Referencia a la instancia del formulario que se está creando
    # *args: Argumentos posicionales variables (tupla)
    # **kwargs: Argumentos con nombre variables (diccionario)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()  # Inicializa helper de crispy-forms
        self.helper.form_method = 'post'  # Método del formulario
        self.helper.form_class = 'contact-form'  # Clase CSS personalizada
        self.helper.attrs = {'novalidate': ''}  # Desactiva validación HTML5

        # Define layout responsivo con Bootstrap 5
        self.helper.layout = Layout(
            # Fila 1: Nombre y Email en 2 columnas
            Row(
                Column('nombre', css_class='col-md-6 mb-3'),
                Column('email', css_class='col-md-6 mb-3'),
            ),
            # Fila 2: Asunto ancho completo
            Row(
                Column('asunto', css_class='col-md-12 mb-3'),
            ),
            # Fila 3: Tipo de consulta
            Row(
                Column('tipo_consulta', css_class='col-md-12 mb-3'),
            ),
            # Fila 4: Mensaje (textarea grande)
            Row(
                Column('mensaje', css_class='col-md-12 mb-3'),
            ),
            # Botón de envío ancho completo
            Submit('submit', 'Enviar Mensaje', css_class='btn btn-primary btn-lg w-100'),
        )