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
    
    #Pac= input("Ingrese la cédula del paciente: ")
    for i in range(len(pacientes)) :
        if pacientes[i][0] == cedula:
            return(pacientes[i])
        
def info_medico(dict_medicos,key,):

    c=dict_medicos[key]
    return c
    #""" for i in range(len(pacientes)) :
        #if pacientes[i][0] == pac:
           # return(pacientes[i])"""

    



