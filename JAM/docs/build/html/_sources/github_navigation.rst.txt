====================================
Navegación en GitHub
====================================

GitHub es una plataforma de control de versiones donde los proyectos se organizan en repositorios. A continuación, te mostramos cómo explorar un repositorio de manera eficiente.


**Estructura de un Repositorio**

Un repositorio de GitHub generalmente tiene la siguiente estructura:

- **README.md**: Archivo de bienvenida con una descripción del proyecto.
- **docs/**: Carpeta con la documentación del proyecto (incluir archivos `.rst`).
- **Agriculture/**: Código fuente del modelo de `Agricultura`.
- **Energy/**: Código fuente del modelo de `Energía`.
- **IPPU/**: Código fuente del modelo de Procesos Industriales y Uso de Productos `IPPU`.
- **UTCUTS/**: Código fuente del modelo de Uso del Suelo y Cambio de Uso del Suelo `USCUS`.
- **Waste/**: Código fuente del modelo de `Residuos`.
- **Data/**: Carperta con archivos de datos de entrada de los diferentes modelos sectoriales.
- **requirements.txt**: Dependencias del proyecto (para poder ejecutar la simulación, son librerías de Python).
- **.github/**: Configuraciones para CI/CD, plantillas de issues y PRs (únicamente disponible en la PC cuando se clona el repositorio).





**Cómo Explorar Archivos en GitHub**


1. **Usar la Barra de Búsqueda**
   - En la página del repositorio, usa la barra de búsqueda para encontrar archivos o directorios específicos.

2. **Ver el Historial de Cambios**
   - Cada archivo tiene un historial de cambios accesible desde la pestaña "History" o en la opción `# Commits`, bajo el botón verde ``<> Code``.

3. **Descargar el Código**
   - Puedes descargar el repositorio en formato `.zip` presionando clic izquierdo el botón verde ``<> Code`` y después clic izquierdo en la opción ``Download ZIP``.
   También se puede clonar con el siguiente comando por medio de `Git Bash`:
   git clone https://github.com/clg-admin/ECU_NDC.git