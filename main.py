from funtions import *
import os

ruta_carpeta = r'C:\Users\rseba\OneDrive\Escritorio\UNIVERSIDAD DE ANTIOQUIA\SEMESTRE 3\Informatica 1\Parcial 4\Taller_3-1\Datos' #direccion de la carpeta datos que con tiene los medicos, pacientes y resultados

for nombre_archivo in os.listdir(ruta_carpeta):
    ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)

    if ruta_archivo.endswith('.csv'):
        print(f'Procesando archivo CSV: {ruta_archivo}')
        dict_medicos = read_csv(ruta_archivo)

    elif ruta_archivo.endswith('.txt'):
        print(f'Procesando archivo TXT: {ruta_archivo}')
        dict_resultados = read_txt(ruta_archivo)


    elif ruta_archivo.endswith('.json'):
        print(f'Procesando archivo JSON: {ruta_archivo}')
        dict_pacientes = read_json(ruta_archivo)


"""print(dict_resultados)
print(dict_pacientes)
print(dict_medicos)
"""
Pac= input("Ingrese la cédula del paciente: ")

info_paciente = info_(dict_pacientes, Pac)
socio = int(info_paciente[3])
info_medi = info_medico(dict_medicos,socio)
print(info_medi)
print(info_paciente)

# print(dict_resultados)