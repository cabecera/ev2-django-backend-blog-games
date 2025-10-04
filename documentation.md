
# CSS
## Estructura para css recomendada

bloggames/
├─ manage.py
├─ bloggames/         # proyecto
│  └─ settings.py
└─ core/               # app "core"
   ├─ templates/
   │  └─ core/
   │     ├─ base.html
   │     └─ index.html
   └─ static/
      └─ core/
         ├─ css/
         │  ├─ vars.css           # variables CSS (custom properties)
         │  ├─ base.css           # layout, grid, typography
         │  ├─ components.css     # botones, forms, cards
         │  └─ pages/
         │     └─ index.css       # CSS específico de la home
         └─ js/
            └─ index.js


### En base.html

Debemos tener estilos globales.

  <!-- Variables y estilos globales -->
  <link rel="stylesheet" href="{% static 'core/css/vars.css' %}">
  <link rel="stylesheet" href="{% static 'core/css/base.css' %}">
  <link rel="stylesheet" href="{% static 'core/css/components.css' %}">


### En index.html -- bloque para inyectar CSS específico

Esto viene desde un .css especificamente para index.html.

{% block extra_css %}
<link rel="stylesheet" href="{% static 'core/css/pages/index.css' %}">
{% endblock %}



### Cómo funciona la herencia de estilos en Django

Cuando tenemos en index.html  {% extends "core/base.html" %}

Significa que todo el contenido de base.html se carga primero, incluyendo los <link rel="stylesheet" ...> que importan los CSS globales (base.css, components.css, etc.).
Luego Django reemplaza los bloques ({% block content %}, {% block extra_css %}, etc.) con el contenido de tu index.html.

### Funcionamiento de navagador

Entonces, el navegador:
Carga primero base.css (por eso todos los títulos, el body, etc., ya tienen estilos globales).
Luego carga index.css, que puede agregar o sobrescribir estilos específicos para la página de inicio.

<head>
  <link rel="stylesheet" href="/static/core/css/base.css">
  <link rel="stylesheet" href="/static/core/css/pages/index.css">
</head>
<body>
  <header>
    <h1 class="site-title">BlogGames</h1>
  </header>
  <h2 class="home-title">Últimas noticias</h2>
  <p>Bienvenido al blog de videojuegos más completo.</p>
</body>
