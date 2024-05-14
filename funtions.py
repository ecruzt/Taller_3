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

def validar_existencia(diccionario, cedula):
    cedulas = list(diccionario.keys())
    if cedula in cedulas:
        return True
    else:
        return False

#Funcion para validar la existencia de un paciente/médico/resultados con su respectiva cédula

def validar_cedula(ask_for_cedula, diccionario):
    cedula = ''
    while not validar_existencia(diccionario, cedula):
        try:
            cedula = readUserInput(ask_for_cedula, int)
            if not validar_existencia(diccionario, cedula):
                print("La cédula ingresada no existe. Por favor, ingrese una cédula válida.")
        except ValueError:
            print("Por favor, ingrese una cédula válida.")
    return cedula       
 
def info_medico(dict_medicos, asignado):
    cedula_medicos = list(dict_medicos.keys())
    for i in cedula_medicos:
        if dict_medicos[i]["codigo"] == asignado:
            return dict_medicos[i]

# Funcion que relaciona paciente, medicos, y resultados
    
def Asociar(dict_pacientes, dict_resultados, dict_medicos):
    cedula = validar_cedula("Ingrese la cédula del paciente: ", dict_pacientes)
    info_paciente = looking_for_cedula(dict_pacientes, cedula) 
    info_resultados = looking_for_cedula(dict_resultados, cedula)
    enfermedades = list(info_resultados.keys())
    socio = info_paciente['medico_asignado']
    info_medi = info_medico(dict_medicos,socio)
    asociation =f'''El paciente {info_paciente['nombre']} está asignado al médico {info_medi['nombre']} los resultados de sus examenes son:
{info_resultados[enfermedades[0]]} para {enfermedades[0]} y {info_resultados[enfermedades[1]]} para {enfermedades[1]}'''
    return asociation

#Funcion actualizar info paciente

def actualizar_paciente(dict_pacientes, dict_medicos):
    menuPacientes = '''
     1. Modificar nombre
     2. Modificar edad
     3. Modificar médico asignado
    '''
    while True:
        print(menuPacientes)
        try:
            responsemenupacientes = readUserInput('Ingrese opción deseada: ', int)
            if responsemenupacientes in [1, 2, 3]:
                if responsemenupacientes == 1:
                    cedula = validar_cedula("Ingrese la cédula del paciente al cual desea cambiar de nombre: ", dict_pacientes)
                    nombrenuevo = readUserInput("Ingrese nombre nuevo: ", str)
                    dict_pacientes[cedula]["nombre"] = nombrenuevo
                    break
                elif responsemenupacientes == 2:
                    cedula = validar_cedula("Ingrese la cédula del paciente actualizar edad: ", dict_pacientes)
                    edadnueva = readUserInput("Ingrese la edad actual: ", str)
                    dict_pacientes[cedula]["edad"] = edadnueva
                    break
                elif responsemenupacientes == 3:
                    cedula = validar_cedula("Ingrese la cédula del paciente para reasignarle un médico: ", dict_pacientes)
                    cedulas_medicos = list(dict_medicos.keys())
                    codigos = []
                    for i in cedulas_medicos:
                        codigos.append(dict_medicos[i]['codigo'])
                    mediconuevo = ''
                    while mediconuevo not in codigos:
                        try:
                            mediconuevo = readUserInput("Ingrese el código del médico deseado: ", str)
                            if mediconuevo not in codigos:
                                print(f'El médico de código {mediconuevo}, no existe, seleccione un codigo valido:\n{codigos}')
                        except ValueError:
                            print("Por favor, ingrese un código de médico válido.")
                    dict_pacientes[cedula]["medico_asignado"] = mediconuevo
                    break
                else:
                    print('Ingrese opción valida')
            else:
                print('Ingrese opción valida')
        except ValueError:
            print("Datos incorrectos")

# Función para obtener el nombre del médico asignado

def obtener_nombre_medico(dict_medicos, codigo_medico):
    for medico_id, datos_medico in dict_medicos.items():
        if datos_medico['codigo'] == codigo_medico:
            return datos_medico['nombre']
    return 'Médico no encontrado'

# Función para agregar un nuevo paciente

def agregar_nuevo_paciente(dict_pacientes, dict_medicos, dict_resultados):
    while True:
        cedula = readUserInput("Ingrese la cédula del nuevo paciente: ", int)
        if validar_existencia(dict_pacientes, cedula):
            print(f"Error: La cédula {cedula} ya existe. Por favor, ingrese una cédula diferente.")
        else:
            break

    nombre = input("Ingrese el nombre del nuevo paciente: ")
    edad = readUserInput("Ingrese la edad del nuevo paciente: ", int)

    print("Médicos disponibles:")
    for medico_id, datos_medico in dict_medicos.items():
        print(f"{datos_medico['codigo']}: {datos_medico['nombre']}")

    codigos_medicos = [datos_medico['codigo'] for datos_medico in dict_medicos.values()]
    while True:
        codigo_medico = input("Ingrese el código del médico asignado: ")
        if codigo_medico in codigos_medicos:
            break
        else:
            print("Error: Código de médico no válido. Por favor, ingrese un código de médico existente.")

    dict_pacientes[cedula] = {
        'nombre': nombre,
        'edad': edad,
        'medico_asignado': codigo_medico
    }

    enfermedades = {}
    while True:
        enfermedad = input("Ingrese el nombre de una enfermedad (o 'salir' para terminar): ")
        if enfermedad.lower() == 'salir':
            break
        resultado = readUserInput(f"Ingrese el resultado para {enfermedad} (Positivo/Negativo): ", str)
        while resultado.lower() not in ['positivo', 'negativo']:
            print("Error: El resultado debe ser 'Positivo' o 'Negativo'. Por favor, intenta de nuevo.")
            resultado = readUserInput(f"Ingrese el resultado para {enfermedad} (Positivo/Negativo): ", str)
        enfermedades[enfermedad] = resultado.capitalize()

    dict_resultados[cedula] = enfermedades

    print(f"Paciente {nombre} agregado con éxito.")

# Función para agregar un nuevo doctor

def agregar_nuevo_doctor(dict_medicos):
    while True:
        cedula = readUserInput("Ingrese la cédula del nuevo doctor: ", int)
        if validar_existencia(dict_medicos, cedula):
            print(f"Error: La cédula {cedula} ya existe. Por favor, ingrese una cédula diferente.")
        else:
            break

    while True:
        codigo = readUserInput("Ingrese el código del nuevo doctor: ", str)
        if codigo in [medico['codigo'] for medico in dict_medicos.values()]:
            print(f"Error: El código {codigo} ya está en uso. Por favor, ingrese un código único.")
        else:
            break

    nombre = input("Ingrese el nombre del nuevo doctor: ")

    dict_medicos[cedula] = {'nombre': nombre, 'codigo': codigo}

    print(f"Doctor {nombre} agregado con éxito.")

#Funcion agregar info paciente

def agregar_info_paciente(dict_pacientes):
    while True:
        try:
            cedula= validar_cedula("Ingrese cedula de paciente al que le desea añadir informacion: ", dict_pacientes)
            new_key= readUserInput("Qué dato desea ingresar?: ", str)
            new_value= input(f"Ingresa un valor para {new_key}: ")
            dict_pacientes[cedula][new_key] = new_value
            break
        except: 
            print("Valor incorrecto")

#Funcion actualizar info medico

def actualizar_medico(dict_medicos):              
     menuMedicos = '''
=========Menú======
1. Modificar nombre
2. Modificar código
              '''
     while True:
        try:
            print(menuMedicos)
            reponsemenuMedicos = readUserInput('Ingrese opción deseada: ', int)
            if reponsemenuMedicos == 1:
                cedula= validar_cedula("Ingrese cédula del médico al cual desea cambiar de nombre: ", dict_medicos)
                nombrenuevo= readUserInput("Ingrese nombre nuevo: ", str)
                dict_medicos[cedula]["nombre"] = nombrenuevo
                break
            if reponsemenuMedicos==2:
                cedula = validar_cedula("Ingrese cédula del médico al cual desea cambiar de código: ", dict_medicos)
                codigonuevo = readUserInput("Ingrese nombre nuevo: ", str)
                dict_medicos[cedula]["codigo"] = codigonuevo
                break
        except:
            print("Datos incorrectos")

#Funcion agregar info medico
def agregar_info_Medico(dict_medicos):
    while True:
        try:
            cedula = validar_cedula("Ingrese la cédula del medico al cual desea añadir informacion: ", dict_medicos)
            new_key = readUserInput("Qué informacion desea agregar: ", str)
            new_value = input(f"Ingrese un valor para {new_key}: ")
            dict_medicos[cedula][new_key] = new_value
            break
        except ValueError:
            print("Valor incorrecto")

#Funcion actualizar info resultados

def actualizar_resultados(dict_resultados):
    menuResultados = '''
     1. Modificar gripa
     2. Modificar fiebre
    '''
    while True:
        print(menuResultados)
        try:
            responsemenuResultados = readUserInput('Ingrese opción deseada: ', int)
            if responsemenuResultados in [1, 2]:
                cedula = validar_cedula("Ingrese cedula a la cual le desea cambiar el resultado: ", dict_resultados)
                if responsemenuResultados == 1:
                    gripanuevo = readUserInput("Ingrese el nuevo resultado para gripa: ", str)
                    dict_resultados[cedula]["gripa"] = gripanuevo
                    break
                elif responsemenuResultados == 2:
                    fiebrenuevo = readUserInput("Ingrese el nuevo resultado para fiebre: ", str)
                    dict_resultados[cedula]["fiebre"] = fiebrenuevo
                    break
            else:
                print('Ingrese opción valida')
        except ValueError:
            print("Datos incorrectos")
        
#Funcion agregar info medico

def agregar_info_Resultado(dict_resultados):
    while True:
        try:
            cedula = validar_cedula("Ingrese cédula del paciente al que le desea añadir información en sus resultados: ", dict_resultados)
            new_key = readUserInput("Qué dato desea ingresar?: ", str)
            new_value = input(f"Ingresa un valor para {new_key}: ")
            dict_resultados[cedula][new_key] = new_value
            break
        except ValueError:
            print("Valor incorrecto")

# Función para eliminar datos de un paciente

def eliminar_datos_paciente(dict_pacientes):
    cedula = validar_cedula("Ingrese la cédula del paciente que desea editar: ", dict_pacientes)
    paciente = looking_for_cedula(dict_pacientes, cedula)
    if paciente:
        print(f"""Datos del paciente encontrado:
        Nombre: {paciente['nombre']}
        Edad: {paciente['edad']}
        Médico asignado: {paciente['medico_asignado']}""")
        
        while True:
            try:
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
            except:
                print('Ingrese una opcion valida')
        
        print("Dato eliminado correctamente.")
    else:
        print("No se encontró ningún paciente con la cédula proporcionada.")

# Función para eliminar datos de un medico

def eliminar_datos_medico(dict_medico):
    cedula= validar_cedula("Ingrese la cédula del médico que desea editar: ", dict_medico)

    medico = looking_for_cedula(dict_medico, cedula)
    if medico:
        print(f"""Datos del medico encontrado:
        Nombre: {medico['nombre']}
        Código: {medico['codigo']}""")
        
        while True:
            try:
                dato_a_eliminar = readUserInput(f"¿Qué dato desea eliminar del médico {medico['nombre']}?\n1. Nombre\n2. Código\n ", int)
                
                if dato_a_eliminar == 1:
                    medico['nombre'] = ''
                    break
                elif dato_a_eliminar == 2:
                    medico['edad'] = ''
                    break
                else:
                    print("Entrada no válida.")
            except:
                print('Ingrese una opcion valida')
        print("Dato eliminado correctamente.")
    else:
        print("No se encontró ningún paciente con la cédula proporcionada.")

# Función para eliminar resultados de un paciente

def eliminar_datos_resultados(dict_pacientes):
    cedula = validar_cedula("Ingrese la cédula del paciente que desea editar: ", dict_pacientes)
    paciente = looking_for_cedula(dict_pacientes, cedula)
    enfermedades = list(paciente.keys())

    if paciente:
        print(f"""Datos del paciente encontrado:
        Enfermedades: {enfermedades}
        Estado: {paciente[enfermedades[0]]} para {enfermedades[0]} y {paciente[enfermedades[1]]} para {enfermedades[1]}
        """)
        
        while True:
            dato_a_eliminar = readUserInput(f"¿Cuál estado de enfermedad desea eliminar?\n1. {enfermedades[0]}\n2. {enfermedades[1]}\n ", int)
            
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

# funcion para exportar informacion en formato .txt

def exportar_en_txt(dict_medicos, dict_pacientes, dict_resultados):
    nombre_archivo = readUserInput('Ingrese un nombre para el archivo final: ', str)
    with open(f"{nombre_archivo}.txt", 'w', encoding='utf-8') as archivo:
        archivo.write('Médicos:\n')
        for medico_id, info_medico in dict_medicos.items():
            archivo.write(f"Cédula: {medico_id}")
            for key, value in info_medico.items():
                archivo.write(f", {key}: {value}")
            archivo.write('\n')

        archivo.write('\nPacientes:\n')
        for paciente_id, info_paciente in dict_pacientes.items():
            archivo.write(f"Cédula: {paciente_id}")
            for key, value in info_paciente.items():
                archivo.write(f", {key}: {value}")
            archivo.write('\n')

        archivo.write('\nResultados de Pruebas:\n')
        for paciente_id, resultados in dict_resultados.items():
            archivo.write(f"Cédula del Paciente: {paciente_id}\n")
            for prueba, resultado in resultados.items():
                archivo.write(f"{prueba}: {resultado}\n")
            archivo.write('\n')

# funcion para exportar informacion en formato .csv

def exportar_en_csv(dict_medicos, dict_pacientes, dict_resultados):
    import csv
    nombre_archivo = readUserInput('Ingrese un nombre para el archivo final: ', str)
    
    with open(f"{nombre_archivo}.csv", 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        
        primer_medico = list(dict_medicos.values())[0]
        claves_medico = list(primer_medico.keys())
        
        writer.writerow(["Médicos"])
        writer.writerow(["Cédula", *claves_medico])
        for medico_id, info_medico in dict_medicos.items():
            writer.writerow([medico_id, *info_medico.values()])
        
        writer.writerow([])
        
        primer_paciente = list(dict_pacientes.values())[0]
        claves_paciente = list(primer_paciente.keys())
        
        writer.writerow(["Pacientes"])
        writer.writerow(["Cédula", *claves_paciente])
        for paciente_id, info_paciente in dict_pacientes.items():
            writer.writerow([paciente_id, *info_paciente.values()])

        writer.writerow([])
        
        primer_resultado = list(dict_resultados.values())[0]
        claves_resultado = list(primer_resultado.keys())
        
        writer.writerow(["Resultados de Pruebas"])
        writer.writerow(["Cédula del Paciente", *claves_resultado])
        for paciente_id, resultados in dict_resultados.items():
            writer.writerow([paciente_id, *resultados.values()])

# funcion para exportar informacion en formato .json

def exportar_en_json(dict_medicos, dict_pacientes, dict_resultados):
    import json
    nombre_archivo = readUserInput('Ingrese un nombre para el archivo final: ', str)

    data = {
        "medicos": dict_medicos,
        "pacientes": dict_pacientes,
        "resultados": dict_resultados
    }
    with open(f'{nombre_archivo}.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

#Buscar paciente

def buscar_paciente(dict_pacientes):
    cadena= readUserInput("Ingrese las iniciales de la cédula del paciente: ", str)
    for i in (dict_pacientes.keys()):
        cedula = str(i)
        if cedula.startswith(cadena):
            print( f"La información del paciente de cédula: {cedula} es {dict_pacientes[i]}")
        else:
            print("No se encontrarón mas usuarios")

# adornos

def exportacion_exitosa():
    tamaño = 5
    for i in range(tamaño):
        if i == tamaño - 1:
            print("*" * (2 * i + 1) + " Informacion exportada con exito!")
        else:
            print("" * (tamaño - i - 1) + "*" * (2 * i + 1))
    for i in range(tamaño - 2, -1, -1):
        print("" * (tamaño - i - 1) + "*" * (2 * i + 1))

def byebye():
    tamaño = 7
    for i in range(tamaño):
        if i == tamaño - 1:
            print("*" * (2 * i + 1) + " Hasta pronto!")
        else:
            print("" * (tamaño - i - 1) + "*" * (2 * i + 1))
    for i in range(tamaño - 2, -1, -1):
        print("" * (tamaño - i - 1) + "*" * (2 * i + 1))


   



