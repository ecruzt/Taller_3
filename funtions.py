def readUserInput(output, dataType):
    while True:
        user_input = input(output)
        try: 
            result = dataType(user_input)
            break
        except ValueError:
            print(f"Error: '{user_input}' no es un valor válido para {dataType.__name__}. Por favor, intenta de nuevo.")
    return result

def read_csv(archivo):
    import csv
    try:
        with open(archivo, 'r') as medicos:
            medi = csv.DictReader(medicos)
            contenido_medicos = {}
            for i, row in enumerate(medi):
                contenido_medicos[i]=(row['cedula'], row['nombre'], row['codigo'])
        return contenido_medicos
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        return None
    except KeyError as e:
        print(f"La clave {e} no se encontró en el archivo.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

def read_json(archivo):
    import json
    try:
        with open(archivo, 'r', encoding='utf8') as pacientes:
            paciente_list = json.load(pacientes)
            dict_pacientes = {}
            for i,value in enumerate(paciente_list):
                dict_pacientes[i] = list(value.values())
            modified_dict_pacientes = {}
            for key, value in dict_pacientes.items():
                modified_value = [value[1], value[0], *value[2:]]
                modified_dict_pacientes[key] = modified_value
            return modified_dict_pacientes
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"El archivo {archivo} no es un archivo JSON válido.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
    
def read_txt(archivo):
    try:
        with open(archivo, 'r') as resultados:
            resultado = resultados.read()
        sineso = resultado.replace("^", ",")
        rsepa = sineso.split("\n")
        dict_resultados = {}
        for i, value in enumerate(rsepa):
            dict_resultados[i] = value.split(',')
        return dict_resultados
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
    
#primer argumento diccionario ya sea de pacientes ó resultados
# segundo argumento cedula a buscar

def looking_for_cedula(dict, cedula):
    for i in range(len(dict)):
        if dict[i][0] == cedula:
            return(dict[i])

def modicarNombre(pacientes, nombreant):
    
    for i in range(len(pacientes)) :
        if pacientes[i][0] == nombreant:
            return(pacientes[i])
        
def info_medico(dict_medicos,key,):

    c=dict_medicos[key]
    return c


def Asociar(cedula, dict_pacientes, dict_resultados, dict_medicos):
    info_paciente = looking_for_cedula(dict_pacientes, cedula) 
    info_resultados = looking_for_cedula(dict_resultados, cedula)
    socio = int(info_paciente[3])
    info_medi = info_medico(dict_medicos,socio)
    asociation = f'El paciente {info_paciente[1]} está asignado al médico {info_medi[1]} los resultados de sus examenes son:\n{info_resultados[2]} para {info_resultados[1]} y {info_resultados[4]} para {info_resultados[3]}'
    return asociation

# def actualizar_paciente(dict_pacientes):
#     import json
#     try:
        
#             menuPacientes = '''
#             1. Modificar nombre
#             2. Modificar edad
#             3. Modificar medico asignado
#             '''
#             while True:
#                 print(menuPacientes)
#                 reponsemenupacientes = readUserInput('Ingrese opción deseada: ', int)
#                 if reponsemenupacientes == 1:
#                     nombreant= readUserInput("Ingrese nombre que desea cambiar: ", str)
#                     keynombreant=modicarNombre(paciente_list,nombreant)
#                     nombrenuevo= readUserInput("Ingrese nombre nuevo: ", str)
#                     keynombreant[0].replace(nombrenuevo)




                    
    
    
    
#     except FileNotFoundError:
#         print(f"El archivo {archivo} no se encontró.")
#         return None
#     except json.JSONDecodeError:
#         print(f"El archivo {archivo} no es un archivo JSON válido.")
#         return None
#     except Exception as e:
#         print(f"Ocurrió un error: {e}")
#         return None



# Función para eliminar datos de un paciente

def eliminar_datos_paciente(dict_pacientes, cedula):
    paciente = looking_for_cedula(dict_pacientes, cedula)
    if paciente:
        print(f"""Datos del paciente encontrado:
        Cédula: {paciente[0]}
        Nombre: {paciente[1]}
        Edad: {paciente[2]}
        Médico asignado: {paciente[3]}""")
        
        while True:
            dato_a_eliminar = readUserInput(f"¿Qué dato desea eliminar del paciente {paciente[1]}?\n1. Nombre\n2. Edad\n3. Médico asignado\n ", int)
            
            if dato_a_eliminar == 1:
                paciente[1] = None
                break
            elif dato_a_eliminar == 2:
                paciente[2] = None
                break
            elif dato_a_eliminar == 3:
                paciente[3] = None
                break
            else:
                print("Entrada no válida.")
        
        print("Dato eliminado correctamente.")
    else:
        print("No se encontró ningún paciente con la cédula proporcionada.")




