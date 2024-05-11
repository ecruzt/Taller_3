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

def info_(pacientes, cedula):
    
    for i in range(len(pacientes)) :
        if pacientes[i][0] == cedula:
            return(pacientes[i])

def modicarNombre(pacientes, nombreant):
    
    for i in range(len(pacientes)) :
        if pacientes[i][0] == nombreant:
            return(pacientes[i])
        
def info_medico(dict_medicos,key,):

    c=dict_medicos[key]
    return c


def Asociar(cedula, dict_pacientes, dict_resultados, dict_medicos):
    info_paciente = info_(dict_pacientes, cedula) 
    info_resultados = info_(dict_resultados, cedula)
    socio = int(info_paciente[3])
    info_medi = info_medico(dict_medicos,socio)
    asociation = f'El paciente {info_paciente[1]} está asignado al médico {info_medi[1]} los resultados de sus examenes son:\n{info_resultados[2]} para {info_resultados[1]} y {info_resultados[4]} para {info_resultados[3]}'
    return asociation

def actualizar_paciente(archivo):
    import json
    try:
        with open(archivo, 'w', encoding='utf8') as pacientes:
            paciente_list = json.load(pacientes)
            menuPacientes = '''
            1. Modificar nombre
            2. Modificar edad
            3. Modificar medico asignado
            '''
            while True:
                print(menuPacientes)
                reponsemenupacientes = readUserInput('Ingrese opción deseada: ', int)
                if reponsemenupacientes == 1:
                    nombreant= readUserInput("Ingrese nombre que desea cambiar: ", str)
                    keynombreant=modicarNombre(paciente_list,nombreant)
                    nombrenuevo= readUserInput("Ingrese nombre nuevo: ", str)
                    keynombreant[0].replace(nombrenuevo)




                    
    
    
    
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"El archivo {archivo} no es un archivo JSON válido.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None


