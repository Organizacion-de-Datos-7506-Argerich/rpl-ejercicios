<span style="background:#FFCC99;padding:2px"> <b>Hint:</b> Si tenemos una lista podemos transforma en set con set(la_lista)</span>

La Agencia Nacional de Estadísticas de Buenos Aires recolecta información de nacimientos cuando los padres registran a sus hijos en el registro civil a partir de una encuesta. Esa información se encuentra disponible para su análisis en un csv con el siguiente formato (dia_nacimiento, mes_nacimiento, anio_nacimiento, peso_al_nacer, longitud_al_nacer, id_hospital, tipo_parto), donde el tipo de parto 1 es natural y 2 es cesárea. 
Por otro lado la agencia cuenta con información histórica de los hospitales en otro csv con siguiente formato (id_hospital, dirección, promedio_nacimientos_mensual). 

Se pide usar Pandas para: 
1. Calcular la cantidad de nacimientos para cada uno de los hospitales para el mes de Octubre de 2017 e indicar aquellos hospitales que superan el promedio de nacimientos mensuales. 
2. Comparando el mes de Octubre de 2017 indicar si se incremento el % de cesáreas con respecto a ese mes del año 2016 en un dataframe con columnas (id_hospital, se_incremento).
