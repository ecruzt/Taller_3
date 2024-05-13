from funtions import *
import os

#direccion de la carpeta datos que contiene los medicos, pacientes y resultados
path_raul = r'C:\Users\rseba\OneDrive\Escritorio\UNIVERSIDAD DE ANTIOQUIA\SEMESTRE 3\Informatica 1\Parcial 4\Taller_3-1\Datos'
path_emanuel = r"C:\Users\VICTUS\Desktop\UdeA\Tercer semestre\Informática\Tercer_parcial\Taller_3\Datos"
ruta_carpeta = path_raul


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

# dict_medicos = {
#                 101: {'nombre': 'Juan Pérez', 'codigo': '1'},
#                 102: {'nombre': 'María García', 'codigo': '2'},
#                 103: {'nombre': 'Carlos López', 'codigo': '3'}, 
#                 104: {'nombre': 'Laura Martínez', 'codigo': '4'},
#                 105: {'nombre': 'Ana Ruiz', 'codigo': '5'}}

# dict_pacientes = {
#                   1234567890: {'nombre': 'Pedro Pérez', 'edad': 40, 'medico_asignado': '1'},
#                   2345678901: {'nombre': 'María López', 'edad': 35, 'medico_asignado': '2'}, 
#                   3456789012: {'nombre': 'Juan Martínez', 'edad': 50, 'medico_asignado': '3'}, 
#                   4567890123: {'nombre': 'Ana García', 'edad': 28, 'medico_asignado': '4'}, 
#                   5678901234: {'nombre': 'Luisa Rodríguez', 'edad': 45, 'medico_asignado': '5'}}

# dict_resultados = {
#                    1234567890: {'Gripa': 'Positivo', 'Fiebre': 'Positivo'}, 
#                    2345678901: {'Gripa': 'Negativo', 'Fiebre': 'Negativo'}, 
#                    3456789012: {'Gripa': 'Positivo', 'Fiebre': 'Positivo'}, 
#                    4567890123: {'Gripa': 'Negativo', 'Fiebre': 'Positivo'}, 
#                    5678901234: {'Gripa': 'Positivo', 'Fiebre': 'Negativo'}}


while True:
    menu1 ='''
================================= Menú ==============================
1. Ver el médico asociado a un paciente, con sus respectivos resultados
2. Modificar informacion del paciente
3. Modificar informacion de los medicos
4. Modificar examenes medicos
5. Exportar informacion
6. Buscador de pacientes
7. Salir
'''
    print(menu1)

    try:
        responsemenu1 = readUserInput('Ingrese la opcion deseada: ', int)

        if responsemenu1 == 1:
            cedula = readUserInput("Ingrese la cédula del paciente: ", int)
            conexion = Asociar(cedula, dict_pacientes, dict_resultados, dict_medicos)
            print(conexion)

        elif responsemenu1 == 2:
            menu2 ='''
============ Menú =============
1. Actualizar datos para un paciente 
2. Agregar datos para un paciente
3. Eliminar datos de un paciente
'''
            print(menu2)
            try:
                responsemenu2 = readUserInput('Ingrese la opcion deseada: ', int)
                if responsemenu2 == 1:
                    actualizar_paciente(dict_pacientes)
                    continue

                elif responsemenu2 == 2:
                    agregar_info_paciente(dict_pacientes)
                    continue
                
                elif responsemenu2 == 3:
                    cedula_a_eliminar = readUserInput("Ingrese la cédula del paciente que desea editar: ", int)
                    eliminar_datos_paciente(dict_pacientes, cedula_a_eliminar)
                    print("Diccionario de pacientes actualizado:")
                    print(dict_pacientes)
                
                else:
                    print('Ingre una opción valida')
            except TypeError:
                print('Ingre una opción valida')

        elif responsemenu1 == 3:
            menu3 ='''
============ Menú =============
1. Actualizar datos para un medico
2. Agregar datos para un medico
3. Eliminar datos de un medico
'''
            print(menu3)
            try:
                responsemenu3 = readUserInput('Ingrese la opcion deseada: ', int)
                if responsemenu3 == 1:
                    actualizar_medico(dict_medicos)
                    continue

                elif responsemenu3 == 2:
                    agregar_info_Medico(dict_medicos)
                    continue
                
                elif responsemenu3 == 3:
                    cedula_a_eliminar = readUserInput("Ingrese la cédula del medico que desea editar: ", int)
                    eliminar_datos_medico(dict_medicos, cedula_a_eliminar)
                    print("Diccionario de medicos actualizado:")
                    print(dict_medicos)
                
                else:
                    print('Ingre una opción valida')

            except TypeError:
                print('Ingre una opción valida')

        elif responsemenu1 == 4:
            menu4 ='''
============ Menú =============
1. Actualizar resultados medicos para un paciente
2. Agregar resultados medicos para un paciente
3. Eliminar resultados medicos para un paciente
'''
            print(menu4)
            try:
                responsemenu4 = readUserInput('Ingrese la opcion deseada: ', int)
                if responsemenu4 == 1:
                    actualizar_resultados(dict_resultados)
                    continue

                elif responsemenu4 == 2:
                    agregar_info_Resultado(dict_resultados)
                    continue
                
                elif responsemenu4 == 3:
                    cedula_a_eliminar = readUserInput("Ingrese la cédula del paciente que desea editar: ", int)
                    eliminar_datos_resultados(dict_resultados, cedula_a_eliminar)
                    print("Diccionario de resultados actualizado:")
                    print(dict_resultados)
                
                else:
                    print('Ingre una opción valida')

            except TypeError:
                print('Ingre una opción valida')

        elif responsemenu1 == 5:
            menu5 ='''
============ Menú =============
1. Exportar en formato .txt
2. Exportar en formato .csv
3. Exportar en formato .json
'''
            print(menu5)
            try:
                responsemenu5 = readUserInput('Ingrese la opcion deseada: ', int)
                if responsemenu5 == 1:
                    exportar_en_txt(dict_medicos, dict_pacientes, dict_resultados)
                    exportacion_exitosa()

                elif responsemenu5 == 2:
                    exportar_en_csv(dict_medicos, dict_pacientes, dict_resultados)
                    exportacion_exitosa()

                elif responsemenu4 == 3:
                    continue
                
                else:
                    print('Ingre una opción valida')

            except TypeError:
                print('Ingre una opción valida')



        elif responsemenu1 == 6:
            continue




        elif responsemenu1 == 7:
            byebye()
            break
        else:
            print('Ingre una opción valida')

    except TypeError:
        print('Ingre una opción valida')








        
    

