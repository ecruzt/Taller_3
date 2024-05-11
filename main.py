from funtions import *
import os

#direccion de la carpeta datos que contiene los medicos, pacientes y resultados
path_raul = r'C:\Users\rseba\OneDrive\Escritorio\UNIVERSIDAD DE ANTIOQUIA\SEMESTRE 3\Informatica 1\Parcial 4\Taller_3-1\Datos'
path_emanuel = r"C:\Users\VICTUS\Desktop\UdeA\Tercer semestre\Informática\Tercer_parcial\Taller_3\Datos"
ruta_carpeta = path_emanuel

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

# print(dict_resultados)
# print(dict_pacientes)
# print(dict_medicos)

# dict_medicos = {0: ('101', 'Juan Pérez', '1'), 1: ('102', 'María García', '2'), 2: ('103', 'Carlos López', '3'), 3: ('104', 'Laura Martínez', '4'), 4: ('105', 'Ana Ruiz', '5')}
# dict_pacientes = {
#     0: ['1234567890', 'Pedro Pérez', 40, '1'],
#     1: ['2345678901', 'María López', 35, '2'],
#     2: ['3456789012', 'Juan Martínez', 50, '3'],
#     3: ['4567890123', 'Ana García', 28, '4'],
#     4: ['5678901234', 'Luisa Rodríguez', 45, '5']
# }
# # dict_resultados = {
#     0: ['1234567890', 'Gripa', 'Positivo', 'Fiebre', 'Positivo'],
#     1: ['2345678901', 'Gripa', 'Negativo', 'Fiebre', 'Negativo'],
#     2: ['3456789012', 'Gripa', 'Positivo', 'Fiebre', 'Positivo'],
#     3: ['4567890123', 'Gripa', 'Negativo', 'Fiebre', 'Positivo'],
#     4: ['5678901234', 'Gripa', 'Positivo', 'Fiebre', 'Negativo']
# }


while True:
    menu1 ='''
================================= Menú ==============================
1. Ver el médico asociado a un paciente, con sus respectivos resultados
2. Modificar informacion del paciente'''
    print(menu1)

    try:
        responsemenu1 = readUserInput('Ingrese la opcion deseada: ', int)

        if responsemenu1 == 1:
            cedula = readUserInput("Ingrese la cédula del paciente: ", str)
            conexion = Asociar(cedula, dict_pacientes, dict_resultados, dict_medicos)
            print(conexion)

        elif responsemenu1 == 2:
            menu2 ='''
============ Menú =============
1. Actualizar datos para un paciente 
2. Agregar datos para un paciente
3. Eliminar datos de un paciente'''
            print(menu2)
            try:
                responsemenu2 = readUserInput('Ingrese la opcion deseada: ', int)
                if responsemenu2 == 1:
                    continue

                elif responsemenu2 == 2:
                    continue
                
                elif responsemenu2 == 3:
                    cedula_a_eliminar = readUserInput("Ingrese la cédula del paciente que desea editar: ", str)
                    eliminar_datos_paciente(dict_pacientes, cedula_a_eliminar)
                    print("Diccionario de pacientes actualizado:")
                    print(dict_pacientes)
                else:
                    print('Ingre una opción valida')
            except TypeError:
                print('Ingre una opción valida')

        else:
            print('Ingre una opción valida')

    except TypeError:
        print('Ingre una opción valida')








        
    

