### Trabajo Práctico N2 - Importación y Agrupación de Datos de Provincias y Localidades Argentinas

Este repositorio contiene el código Python para el Trabajo Práctico N2, el cual consiste en un programa que lee un archivo CSV con información sobre las provincias argentinas y sus respectivas localidades, importa estos datos a una base de datos MariaDB utilizando XAMPP, y luego agrupa y exporta las localidades por provincia en archivos CSV separados.

### Funcionalidades Principales:

1. **Lectura del CSV:**
   - El programa lee correctamente el archivo CSV de las provincias argentinas con sus localidades.

2. **Creación de Tabla en la Base de Datos:**
   - Se asegura que se crea una tabla en la base de datos con las columnas adecuadas y que los datos se inserten correctamente.

3. **Manipulación de Datos:**
   - Se manipulan los datos una vez que están en la base de datos, especialmente la agrupación por provincia.

4. **Exportación a CSV:**
   - Se crean archivos CSV correctamente, uno por provincia, que contienen la lista de localidades correspondientes. Además, al final de cada archivo CSV se incluye la cantidad de localidades correspondientes a esa provincia.

5. **Uso de motor de base de datos:**
   - Se utiliza el motor de base de datos MariaDB que viene incorporado en el paquete XAMPP.

6. **Eficiencia del Código:**
   - Se evalúa la eficiencia del código en términos de velocidad de ejecución y uso de recursos.

7. **Manejo de Errores:**
   - Se manejan posibles errores durante la lectura del archivo, inserción en la base de datos, exportación a CSV, etc.

8. **Documentación y Claridad del Código:**
   - El código está bien documentado y es claro para entender la lógica de programación utilizada.

### Requisito Indispensable:

- El programa tiene la capacidad de crear la tabla de base de datos cada vez que se ejecuta el script, es decir, si existe, debe ser eliminada y recreada.

### Presentación del Trabajo Práctico:

- Este trabajo práctico está presentado en un repositorio de GitHub público para su posterior revisión y evaluación.

### Instrucciones de Uso:

1. Clonar el repositorio.
2. Instalar XAMPP y asegurarse de que el servidor MariaDB/MySQL esté en funcionamiento.
3. Ejecutar el script Python para importar y agrupar los datos de provincias y localidades.

### Estructura del Repositorio:

- **`main.py`:** El script principal que contiene el código Python para importar y agrupar los datos.
- **`localidades.csv`:** El archivo CSV que contiene la información sobre las provincias argentinas y sus localidades.
- **`README.md`:** Este archivo README que proporciona información sobre el trabajo práctico.

### Autor:

Facundo Ríos
### Fecha de Creación:

09/04/2024
### Licencia:
