import os
import json
import csv

# Crear la carpeta 'datos' si no existe
if not os.path.exists('datos'):
    os.makedirs('datos')

# Leer datos de pacientes desde JSON
with open('pacientes.json', 'r',) as file:
    pacientes = json.load(file)
    for i in pacientes: 
        nombre=i['nombre']
        cedula=i['cedula']
        edad=i['edad']
        med=i['medico_asignado']

# Leer datos de médicos desde CSV
with open('medicos.csv', 'r',) as file:
    medicos = csv.reader(file)

# Leer resultados desde TXT
with open('resultados.txt', 'r') as file:
    resultados = [line.strip() for line in file]

# Funciónes para buscar pacientes , medicos y examenes por cédula
def buscar_paciente(cedula):
    for paciente in pacientes:
        ced=paciente['cedula']
        if ced.startswith(cedula):
            return paciente
    return None
def buscar_medico(cedula):
    for medico in medicos:
        ced=medico['cedula']
        if ced.startswith(cedula):
            return medicos
    return None

# Función para actualizar datos de un paciente, medico y examene.
def actualizar_paciente(cedula, datos_actualizados):
    paciente = buscar_paciente(cedula)
    if paciente:
        paciente.update(datos_actualizados)

def actualizar_medicos(cedula, datos_actualizados):
    medicos = buscar_medico(cedula)
    if medicos:
        medicos.update(datos_actualizados)

# Función para eliminar un paciente
def eliminar_paciente(cedula):
    paciente = buscar_paciente(cedula)
    if paciente:
        pacientes.remove(paciente)
def eliminar_medico(cedula):
    medicos = buscar_medico(cedula)
    if medicos:
        medicos.remove(medicos)


# Función para añadir un nuevo paciente
def añadir_paciente(nuevo_paciente):
    if buscar_paciente(nuevo_paciente['cedula']):
        print('Error: La cedula ya existe')
    else:
        pacientes.append(nuevo_paciente)
def añadir_medico(nuevo_medico):
    if buscar_medico(nuevo_medico['cedula']):
        print('Error: La cedula ya existe')
    else:
        pacientes.append(nuevo_medico)


# Función para exportar los datos a archivos
def exportar_datos():
    with open('datos/pacientes_final.json', 'w') as file:
        json.dump(pacientes, file)
    with open('datos/medicos_final.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(medicos)
    with open('datos/resultados_final.txt', 'w') as file:
        for resultado in resultados:
            file.write(resultado + '\n')


# Menú de usuario
while True:
    a= input('''
1.Buscar pacientes.  
2.Opciones de Informacion. 
3.Salir
> ''')
    if a == '1':
        cedula = input("Ingrese la cédula del paciente: ")
        print(buscar_paciente(cedula))
    elif a == '2':
        while True:
            b=input('''
1.Descargar archivos
2.Ajustar informacion.
3.salir
>''')
            if b=='1':
                exportar_datos()
            elif b=='2':
                while True:
                    c=input('''
Ajustar:
1.Pacientes
2.Examenes
3.Medicos
4.Salir
>''')
                    if c=='1':
                        while True:
                            d=input('''
1.Añadir
2.Eliminar.
3.Actualizar
4.Salir
>''')
                            if d=='1':
                                nuevo_paciente =(input("Ingrese los datos del nuevo paciente en formato JSON:"))
                                añadir_paciente(nuevo_paciente)
                                print('La informacion se ha guardado correctamente')
                            elif d=='2':
                                cedula = input("Ingrese la cédula del paciente: ")
                                eliminar_paciente(cedula)
                                print('La informacion se ha guardado correctamente')
                            elif d=='3':
                                cedula = input("Ingrese la cédula del paciente: ")
                                datos_actualizados = json.loads(input("Ingrese los datos actualizados del paciente en formato JSON: "))
                                actualizar_paciente(cedula, datos_actualizados)
                            elif d=='4':
                                break
                            else:
                                print('El numero que ingresaste es incorrecto intenta nuevamente')
                    elif c=='2':
                        while True:
                            e=input('''
1.Añadir
2.Eliminar.
3.Actualizar
4.Salir
>''')
                            if e=='1':
                                nuevpo =(input("Ingrese los datos del nuevo paciente:"))
                                añadir_paciente(nuevpo)
                                print('La informacion se ha guardado correctamente')
                            elif e=='2':
                                cedula = input("Ingrese la cédula del medico: ")
                                eliminar_paciente(cedula)
                                print('La informacion se ha guardado correctamente')
                            elif e=='3':
                                cedula = input("Ingrese la cédula del paciente: ")
                                datos_actualizados = json.loads(input("Ingrese los datos actualizados del paciente en formato JSON: "))
                                actualizar_paciente(cedula, datos_actualizados)
                            elif e=='4':
                                break
                            else:
                                print('El numero que ingresaste es incorrecto intenta nuevamente')
                    elif c=='3':
                        while True:
                            f=input('''
1.Añadir
2.Eliminar.
3.Actualizar
4.Salir
>''')
                            if f=='1':
                                nuevom=(input("Ingrese los datos del nuevo paciente en formato JSON:"))
                                añadir_paciente(nuevom)
                                print('La informacion se ha guardado correctamente')
                            elif f=='2':
                                cedula = input("Ingrese la cédula del paciente: ")
                                eliminar_medico(cedula)
                                print('La informacion se ha guardado correctamente')
                            elif f=='3':
                                cedula = input("Ingrese la cédula del paciente: ")
                                datos_actualizados = csv.reader(input("Ingrese los datos actualizados del medico: "))
                                actualizar_medicos(cedula, datos_actualizados)
                            elif f=='4':
                                break
                            else:
                                print('El numero que ingresaste es incorrecto intenta nuevamente')
                    elif c=='4':
                        break    
                    else: 
                        print('El numero que ingresaste es incorrecto intente nuevamente')
            elif b=='3':
                break    
            else: 
                print('El numero que ingresaste es incorrecto intente nuevamente')
    elif a=='3':
        break    
    else: 
        print('El numero que ingresaste es incorrecto intente nuevamente')


#falata que los caracteres se lean bien, que no pida los datos tipo json, no se que hace lo de nuevo paciente, falta las validaciones, cuando el archivo datos se crea que lo muestre bonito, falta hacer lo del codigo del doctor y eso.