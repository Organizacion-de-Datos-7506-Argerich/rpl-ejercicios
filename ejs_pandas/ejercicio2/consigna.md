<span style="background:#FFCC99;padding:2px"> <b>Hint:</b> Probar usar la función .to_list() para series de pandas para pasar los valores de una Serie de Pandas a una lista de Python.</span>

# Ejercicio 2

Se tiene un registro de transacciones bancarias, de la forma (nro de transacción, tipo de transacción, cuenta origen, cuenta destino, fecha, hora, monto). 

Se pide resolver en Pandas:
* Validar que todas las transacciones cuenten con un tipo de transacción.
* Validar que para las transacciones del tipo 'Transferencia', exista siempre tanto cuenta origen como cuenta destino.
* Verificar que todas las transacciones del tipo 'Transferencia', 'Deposito' y 'Extraccion' cuenten con montos distintos de cero.
* Indicar cuáles fueron las 10 transacciones de mayor monto.
* Indicar cuál es el tipo de transacción que registra mayor monto promedio.
* Indicar cuáles son las 5 cuentas involucradas en la mayor cantidad de transacciones.
* Indicar cuáles son las 5 cuentas con mayor monto involucrado en alguna transacción.
* Para el tipo de transacción con mayor cantidad de monto promedio, indicar cuales son las 5 cuentas con más transacciones.
