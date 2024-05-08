data_medicos = r'C:\Users\VICTUS\Desktop\UdeA\Tercer semestre\Informática\Tercer_parcial\Taller_monitor\Datos\medicos.csv'
data_pacientes = r'C:\Users\VICTUS\Desktop\UdeA\Tercer semestre\Informática\Tercer_parcial\Taller_monitor\Datos\pacientes.json'
data_resultados = r'C:\Users\VICTUS\Desktop\UdeA\Tercer semestre\Informática\Tercer_parcial\Taller_monitor\Datos\resultados.txt'


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

            print(modified_dict_pacientes)

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

        

            




# contenido_medicos = read_csv(data_medicos)
# if contenido_medicos is not None:
#     print(contenido_medicos)

# contenido_pacientes = read_json(data_pacientes)
# if contenido_pacientes is not None:
#     dict_pacientes = {}
# for i,value in enumerate(contenido_pacientes):
#     dict_pacientes[i] = value  #diccionario de los pacientes

read_txt(data_resultados)


