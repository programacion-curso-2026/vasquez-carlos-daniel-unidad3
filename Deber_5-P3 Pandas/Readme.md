¡QUÉ ES PANDAS?
Pandas es una librería de Python utilizada para organizar, manipular y analizar datos.

¿PARA QUÉ SIRVE?
Sirve para trabajar con tablas de datos, realizar cálculos, filtrar información y analizar datos.

¿CÓMO SE UTILIZA?
Se importa utilizando: import pandas as pd

EJEMPLO 1
  Producto  Cantidad  Precio
0   Aceite        10     8.5
1   Filtro        15    12.0
2    Bujía        20     4.5
3  Batería         5    90.0

Total por producto:
  Producto  Cantidad  Precio  Total
0   Aceite        10     8.5   85.0
1   Filtro        15    12.0  180.0
2    Bujía        20     4.5   90.0
3  Batería         5    90.0  450.0

Ventas totales: 805.0

INFORMACIÓN DE VEHÍCULOS
       Marca    Modelo  Precio
0     Toyota   Corolla   23100
1  Chevrolet      Aveo   18000
2        Kia  Sportage   29000
3    Hyundai    Tucson   32000
4      Mazda         3   25000

Precio promedio:
25420.0

Vehículos con precio menor a $25000:
       Marca   Modelo  Precio
0     Toyota  Corolla   23100
1  Chevrolet     Aveo   18000