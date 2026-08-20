# Deber 8 - P3 Mejora Analítica

## Descripción

Este proyecto desarrolla un programa en Python para analizar registros de mantenimientos realizados a diferentes equipos de una institución.

El programa permite cargar archivos CSV, validar y limpiar los datos, detectar registros inválidos, calcular indicadores y generar gráficos para facilitar el análisis de la información.

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab

## Funcionamiento

El programa realiza las siguientes actividades:

1. Lee los archivos `mantenimientos.csv` y `mantenimientos_con_errores.csv`.
2. Verifica que los archivos existan y puedan ser interpretados.
3. Detecta errores en los registros.
4. Elimina los registros que no cumplen las condiciones establecidas.
5. Calcula estadísticas utilizando NumPy.
6. Analiza los datos utilizando Pandas.
7. Genera dos gráficos con Matplotlib.
8. Exporta los resultados en archivos CSV.

## Validaciones realizadas

Se validan:

- Códigos vacíos.
- Códigos duplicados.
- Fechas inválidas.
- Costos no numéricos o negativos.
- Duraciones no numéricas o menores o iguales a cero.
- Satisfacción fuera del rango de 1 a 5.
- Estados no permitidos.
- Equipos no contemplados.
- Áreas vacías.

## Uso de las herramientas

### Pandas
Se utilizó para leer los archivos CSV, crear y limpiar DataFrames, realizar agrupaciones y exportar los resultados.

### NumPy
Se utilizó para calcular la media, mediana y percentil 75 de los costos, además de clasificar los costos mediante `np.where()`.

### Matplotlib
Se utilizó para generar:
- Costo total de mantenimientos por área.
- Cantidad de mantenimientos por tipo.

## Ciclos y validaciones

Se utilizó un ciclo `for` para recorrer las diferentes reglas de validación. También se utilizaron estructuras `if/else` para tomar decisiones según las condiciones encontradas.

El programa utiliza `try/except` para controlar errores como archivos inexistentes, archivos vacíos y problemas en la lectura del CSV.

## Archivos generados

El programa genera:

- `mantenimientos_limpios.csv`: contiene los registros que superaron las validaciones.
- `resumen_por_area.csv`: contiene un resumen de los mantenimientos y costos agrupados por área.

## Ejecución

El programa puede ejecutarse en Google Colab o Jupyter Notebook.

Para ejecutarlo:

1. Abrir el archivo `.ipynb`.
2. Subir `mantenimientos.csv` y `mantenimientos_con_errores.csv`.
3. Ejecutar las celdas en orden.
4. Revisar los resultados, indicadores y gráficos.
5. Verificar los archivos CSV generados.

## Conclusión

La solución permite identificar y controlar errores en los datos de mantenimiento antes de realizar el análisis. De esta manera se obtienen resultados más confiables y se facilita la interpretación de los costos y cantidad de mantenimientos realizados.