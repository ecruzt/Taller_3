from funtions import *
import os

#dirección de la carpeta datos que contiene los medicos, pacientes y resultados
path_andres = r""
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

while True:
    menu1 ='''
  _________________________________________________________________________
||__________________________________Menú___________________________________||
|| 1. Ver el médico asociado a un paciente, con sus respectivos resultados ||
|| 2. Modificar informacion de los paciente                                ||
|| 3. Modificar informacion de los medicos                                 ||
|| 4. Modificar examenes medicos                                           ||
|| 5. Exportar información                                                 ||
|| 6. Buscador de pacientes                                                ||
|| 7. Salir                                                                ||
||_________________________________________________________________________||
'''
    print(menu1)

    try:
        responsemenu1 = readUserInput('Ingrese la opcion deseada: ', int)

        if responsemenu1 == 1:
            print(Asociar(dict_pacientes, dict_resultados, dict_medicos))

        elif responsemenu1 == 2:
            while True:
                menu2 ='''
                ============ Menú =============
                1. Actualizar datos para un paciente 
                2. Agregar datos para un paciente
                3. Eliminar datos de un paciente
                4. Añadir un paciente
                5. Volver al menú principal
                '''

                print(menu2)
                try:
                    responsemenu2 = readUserInput('Ingrese la opcion deseada: ', int)
                    if responsemenu2 == 5:
                        break
                    elif responsemenu2 in [1, 2, 3, 4]:
                        if responsemenu2 == 1:
                            actualizar_paciente(dict_pacientes, dict_medicos)
                            print("Pacientes actualizado:")
                            print(dict_pacientes)
                            break
                        elif responsemenu2 == 2:
                            agregar_info_paciente(dict_pacientes)
                            print("Pacientes actualizado:")
                            print(dict_pacientes)
                            break
                        elif responsemenu2 == 3:
                            eliminar_datos_paciente(dict_pacientes)
                            print("Pacientes actualizado:")
                            print(dict_pacientes)
                            break
                        elif responsemenu2 == 4:
                            agregar_nuevo_paciente(dict_pacientes, dict_medicos, dict_resultados)
                            print(dict_pacientes)
                            break
                    else:
                        print('Ingrese una opción valida')
                except ValueError:
                    print('Ingrese una opción valida')

        elif responsemenu1 == 3:
            while True:
                menu3 ='''
                ============ Menú =============
                1. Actualizar datos para un médico
                2. Agregar datos para un médico
                3. Eliminar datos de un médico
                4. Añadir médico
                5. Volver al menú principal
                '''

                print(menu3)
                try:
                    responsemenu3 = readUserInput('Ingrese la opción deseada: ', int)
                    if responsemenu3 == 5:
                        break
                    elif responsemenu3 in [1, 2, 3, 4]:
                        if responsemenu3 == 1:
                            actualizar_medico(dict_medicos)
                            print("Información de los médicos actualizada:")
                            print(dict_medicos)
                            break
                        elif responsemenu3 == 2:
                            agregar_info_Medico(dict_medicos)
                            print("Información de los médicos actualizada:")
                            print(dict_medicos)
                            break
                        elif responsemenu3 == 3:
                            eliminar_datos_medico(dict_medicos)
                            print("Información de los médicos actualizada:")
                            print(dict_medicos)
                            break
                        elif responsemenu3 == 4:
                            agregar_nuevo_doctor(dict_medicos)
                            print("Información de los médicos actualizada:")
                            print(dict_medicos)
                    else:
                        print('Ingrese una opción valida')
                except ValueError:
                    print('Ingrese una opción valida')

        elif responsemenu1 == 4:
            while True:
                menu4 ='''
                ============ Menú =============
                1. Actualizar resultados medicos para un paciente
                2. Agregar resultados medicos para un paciente
                3. Eliminar resultados medicos para un paciente
                4. Volver al menú principal
                '''

                print(menu4)
                try:
                    responsemenu4 = readUserInput('Ingrese la opcion deseada: ', int)
                    if responsemenu4 == 4:
                        break
                    elif responsemenu4 in [1, 2, 3]:
                        if responsemenu4 == 1:
                            actualizar_resultados(dict_resultados)
                            print("Resultados actualizados:")
                            print(dict_resultados)
                            break
                        elif responsemenu4 == 2:
                            agregar_info_Resultado(dict_resultados)
                            print("Resultados actualizados:")
                            print(dict_resultados)
                            break
                        elif responsemenu4 == 3:
                            eliminar_datos_resultados(dict_resultados)
                            print("Resultados actualizados:")
                            print(dict_resultados)
                            break
                    else:
                        print('Ingrese una opción valida')
                except ValueError:
                    print('Ingrese una opción valida')

        elif responsemenu1 == 5:
            while True:
                menu5 ='''
                ============ Menú =============
                1. Exportar en formato .txt
                2. Exportar en formato .csv
                3. Exportar en formato .json
                4. Volver al menú principal
                '''

                print(menu5)
                try:
                    responsemenu5 = readUserInput('Ingrese la opcion deseada: ', int)
                    if responsemenu5 == 4:
                        break
                    elif responsemenu5 in [1, 2, 3]:
                        if responsemenu5 == 1:
                            exportar_en_txt(dict_medicos, dict_pacientes, dict_resultados)
                            exportacion_exitosa()
                            break
                        elif responsemenu5 == 2:
                            exportar_en_csv(dict_medicos, dict_pacientes, dict_resultados)
                            exportacion_exitosa()
                            break
                        elif responsemenu5 == 3:
                            exportar_en_json(dict_medicos, dict_pacientes, dict_resultados)
                            exportacion_exitosa()
                            break
                    else:
                        print('Ingrese una opción valida')
                except ValueError:
                    print('Ingrese una opción valida')

        elif responsemenu1 == 6:
            buscar_paciente(dict_pacientes)

        elif responsemenu1 == 7:
            byebye()
            break
        else:
            print('Ingre una opción valida')

    except TypeError:
        print('Ingre una opción valida')
