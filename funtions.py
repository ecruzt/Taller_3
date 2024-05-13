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
            for row in medi:
                contenido_medicos[int(row['cedula'])]= {'nombre': row['nombre'], 'codigo': row['codigo']}
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
            for i in paciente_list:
                dict_pacientes[int(i["cedula"])] = {'nombre': i['nombre'], 'edad': i['edad'], 'medico_asignado': i['medico_asignado']}            
            return dict_pacientes
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
        for i in rsepa:
            elementos = i.split(",")
            dict_resultados[int(elementos[0])] = {elementos[1]: elementos[2], elementos[3]: elementos[4]}
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
    for i in dict.keys():
        if i == cedula:
            return(dict[i])

def modicarNombre(pacientes, nombreant):
    
    for i in range(len(pacientes)) :
        if pacientes[i][0] == nombreant:
            return(pacientes[i])
        
def info_medico(dict_medicos, asignado):
    cedula_medicos = list(dict_medicos.keys())
    for i in cedula_medicos:
        if dict_medicos[i]["codigo"] == asignado:
            return dict_medicos[i]
    


def Asociar(cedula, dict_pacientes, dict_resultados, dict_medicos):
    info_paciente = looking_for_cedula(dict_pacientes, cedula) 
    info_resultados = looking_for_cedula(dict_resultados, cedula)
    enfermedades = list(info_resultados.keys())
    socio = info_paciente['medico_asignado']
    info_medi = info_medico(dict_medicos,socio)
    asociation =f'''El paciente {info_paciente['nombre']} está asignado al médico {info_medi['nombre']} los resultados de sus examenes son:
{info_resultados[enfermedades[0]]} para {enfermedades[0]} y {info_resultados[enfermedades[1]]} para {enfermedades[1]}'''
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
        Nombre: {paciente['nombre']}
        Edad: {paciente['edad']}
        Médico asignado: {paciente['medico_asignado']}""")
        
        while True:
            dato_a_eliminar = readUserInput(f"¿Qué dato desea eliminar del paciente {paciente['nombre']}?\n1. Nombre\n2. Edad\n3. Médico asignado\n ", int)
            
            if dato_a_eliminar == 1:
                paciente['nombre'] = ''
                break
            elif dato_a_eliminar == 2:
                paciente['edad'] = ''
                break
            elif dato_a_eliminar == 3:
                paciente['medico_asignado'] = ''
                break
            else:
                print("Entrada no válida.")
        
        print("Dato eliminado correctamente.")
    else:
        print("No se encontró ningún paciente con la cédula proporcionada.")

# Función para eliminar datos de un medico

def eliminar_datos_medico(dict_medico, cedula):
    medico = looking_for_cedula(dict_medico, cedula)
    if medico:
        print(f"""Datos del medico encontrado:
        Nombre: {medico['nombre']}
        Código: {medico['codigo']}""")
        
        while True:
            dato_a_eliminar = readUserInput(f"¿Qué dato desea eliminar del médico {medico['nombre']}?\n1. Nombre\n2. Código\n ", int)
            
            if dato_a_eliminar == 1:
                medico['nombre'] = ''
                break
            elif dato_a_eliminar == 2:
                medico['edad'] = ''
                break
            else:
                print("Entrada no válida.")
        
        print("Dato eliminado correctamente.")
    else:
        print("No se encontró ningún paciente con la cédula proporcionada.")

# Función para eliminar resultados de un paciente

def eliminar_datos_resultados(dict_pacientes, cedula):
    paciente = looking_for_cedula(dict_pacientes, cedula)
    enfermedades = list(paciente.keys())

    if paciente:
        print(f"""Datos del paciente encontrado:
        Enfermedades: {enfermedades}
        Estado: {paciente[enfermedades[0]]} para {enfermedades[0]} y {paciente[enfermedades[1]]} para {enfermedades[1]}
        """)
        
        while True:
            dato_a_eliminar = readUserInput(f"¿Cuál estado de los enfermedad desea eliminar?\n1. {enfermedades[0]}\n2. {enfermedades[1]}\n ", int)
            
            if dato_a_eliminar == 1:
                paciente[enfermedades[0]] = ''
                break
            elif dato_a_eliminar == 2:
                paciente[enfermedades[1]] = ''
                break

            else:
                print("Entrada no válida.")
        
        print("Dato eliminado correctamente.")
    else:
        print("No se encontró ningún paciente con la cédula proporcionada.")


