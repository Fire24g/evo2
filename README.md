Gestión de Inventario Escolar – Django Web App

Descripción del Proyecto:
Este proyecto es una aplicación web desarrollada con el framework Django, como parte de la Evaluación N°2 del curso Programación Backend de Inacap
La aplicación tiene como objetivo ayudar al Colegio Andes del Sur a gestionar su inventario de equipos tecnológicos (como notebooks, proyectores, impresoras, etc.), 
reemplazando el uso de planillas por una solución digital más eficiente y segura.

Funcionalidades:
 - Registro de equipos tecnológicos con información detallada.
  Consulta y administración de los equipos desde el panel de Django Admin.
  Clasificación por categoría, estado, ubicación y fecha de ingreso.
  Interfaz administrativa personalizada para facilitar la gestión.


Tecnologías Utilizadas:
 - Python 3
 - Django
 - SQLite (puede ser reemplazado por MySQL)
 - Git & GitHub

el como ejecutar la pagina es sencillo:
- paso n°1:
    -clone el repositorio usando "git clone (el enlace que se puede copiar)" en la terminal y
    cuando lo tenga copiado en el visual estudio active el entorno virtual usando "venv\Scripts\activate"
    para luego usar "cd inventario_escolar"
- paso n°2:
    -utilice el comando "pip install -r requirements.txt" en la terminal
- paso n°3:
    -ahora tiene que realizar migraciones utilizando los siguientes comando en la terminal
    "python manage.py makemigrations" y si no se presentan errores use "python manage.py migrate"
- paso n°4:
    -ahora debe crear un usuario usando "python manage.py createsuperuser" donde en la terminal
    le pediran que registre su nombre, su correo y una contraseña(debe haber letras y numeros y siempre
    ser mas de 8 digitos)
- paso n°5:
    -con todo listo solo debe usar el siguiente comando "python manage.py runserver" le mostrara un
    url al cual debe darle click usando "ctrl + click izquierdo" abriendole una pestaña en el navegador donde
    barra de busqueda al url agrege "/admind" lo cual lo llevara a la web donde se crearan los equipos y listo 
