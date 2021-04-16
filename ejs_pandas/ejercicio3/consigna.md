# Ejercicio 3

Dado un dataframe de la forma:

| codigo_producto | codigo_fabricante | mes | ventas_mensuales |
| :---------: | :---------: | :---------: | :---------: |
| 1 |
| 2 |
| 3 |
| ... |

Genere los siguientes dataframes, conteniendo:

### A. Promedio por producto con el siguiente formato

| codigo_producto | promedio_ventas |
| :---------: | :---------: |
| 1 | ...
| 2 | ... 
| ... | ...

### B. Mínimo, Máximo y Promedio de ventas por producto con el formato:

| codigo_producto | minimo\_ventas\_mensual | maximo\_ventas\_mensual | promedio_ventas_mensual |
| :---------: | :---------: | :---------: | :---------: | 
| 1 | ... |...|...|
| 2 | ... |...|...|
| ... | ... |...|...|

### C. Mínimo, Máximo y Promedio de ventas por producto con el formato:

| codigo_producto | agregado | valor | 
| :---------: | :---------: | :---------: |
| 1 | minimo\_ventas\_mensual | ...  | 
| | maximo\_ventas\_mensual | ...
| | promedio\_ventas\_mensual | ...
| ... | minimo\_ventas\_mensual | ...
| | maximo\_ventas\_mensual | ...
| | promedio\_ventas\_mensual | ...

Donde hay un doble índice (pueden usar la función del ejercicio B).

### D. Mínimo, Máximo y Promedio de ventas por producto con el formato:

| | codigo_producto1 | codigo_producto2 | codigo_producto3 | ... |
| :---------: | :---------: | :---------: | :---------: | :---------: | 
| **minimo\_ventas\_mensual** | ... |...|...|...
| **maximo\_ventas\_mensual** | ... |...|...|...
| **promedio\_ventas\_mensual** | ... |...|...|...

Donde los índices son 'minimo\_ventas\_mensual', 'maximo\_ventas\_mensual' y 'promedio\_ventas\_mensual' (pueden usar funciones de ejercicios previos).

### E. Qué productos son provistos por los distintos fabricantes, indicando True/False con el siguiente formato:

| | codigo_fabricante1 | codigo_fabricante2 | codigo_fabricante3 | ... |
| :---------: | :---------: | :---------: | :---------: | :---------: | 
| **codigo_producto1** | ... |...|...|...
| **codigo_producto2** | ... |...|...|...
| **codigo_producto3** | ... |...|...|...
| **...** | ... |...|...|...

Donde el índice es el código de producto correspondiente.