# Taller 3. Implementación de algoritmos en Python
## Estudiante 1: Emanuel Cruz
## Estudiante 2: Raul Molina
## Grupo 4 Informática 1


Se requiere un sistema de información para un hospital. Dicho sistema requiere ser capaz de importar información de:

- Pacientes que se encuentra en archivos de tipo JSON.

- Resultados de pruebas que se encuentran en archivos tipo TXT.

- Médicos que se encuentran en archivos de tipo CSV.

La información podrá relacionarse entre sí, de manera que los resultados tendrán un código que los relacione con el paciente y los pacientes tendrán un código que los relacione con su médico.

La información deberá ser extraída de una carpeta que se deberá llamar “datos” con una única opción, de manera que el programa sea capaz de leer con una única opción todos los tipos de archivos (JSON y CSV) y será almacenada en el código en la forma de diccionarios (35%)

La información podrá ser actualizada, eliminada y además podrán añadirse información extra (10%), la información finalmente podrá ser extraída en 3 archivos separados para pacientes resultados y médicos en la respectiva forma utilizando un único JSON, TXT y CSV para toda la información de Paciente, Resultados y Médicos disponibles (35%).

Finalmente, el programa deberá ser capaz de buscar los pacientes filtrando por su cédula, de manera que si por ejemplo busca 1001 encontrará a todos los pacientes cuya cédula comienza por 1001 aunque los siguientes números sean totalmente diferentes entre sí. (10%)

El programa debe contener un menú que queda a decisión del estudiante como realizarlo (5%)

El programa debe tener manejo de errores y no debe permitir que el usuario ingrese una cédula dos veces (5%)

Si el código por cualquier razón que no haya sido mal uso del código por parte del calificador tiene errores al correr, se deducirá un 0.5 de la nota, así que intenten verificar sus códigos antes de enviarlo, mejor un código que funcione sin errores e incompleto que “completo” pero con muchos errores.
