import os
import json
import csv

# Crear la carpeta 'datos' si no existe
if not os.path.exists('datos'):
    os.makedirs('datos')

# Leer datos de pacientes desde JSON
with open('pacientes.json', 'r',encoding='utf8') as file:
    pacientes = json.load(file)

m=0
# Leer datos de médicos desde CSV
with open('medicos.csv', 'r',encoding='utf8') as file:
    medicos = csv.reader(file)
    
        
# Leer resultados desde TXT
with open('resultados.txt', 'r',encoding='utf8') as file:
    resultados = [line.strip() for line in file]
    
            
    


# Funciónes para buscar pacientes , medicos y examenes por cédula
def buscar_paciente(cedula):
    for paciente in pacientes:
        ced=paciente['cedula']
        if ced.startswith(cedula):
            nombre=paciente['nombre']
            cedula1=paciente['cedula']
            edad=paciente['edad']
            med=paciente['medico_asignado']
            return (nombre,cedula1,edad,med)
        else:
            print('El paciente que ingresaste no existe')


def buscar_medico(cedula):
        file= open('medicos.csv', 'r',encoding='utf8',errors='replace') 
        contenido= csv.reader(file)
        m=0
        for i in contenido:
            m=m+1
            if m==1:
                continue
            name=i[1]
            ced=i[0]
            codigo=i[2]
        if ced.startswith(cedula):
            return (ced,name,codigo)
        
            
def buscar_examenes(cedula):
        for x in resultados:
            x=x.split('^')
            ce=x[0]
            sin=x[1]
            res=x[2]
            sin2=x[3]
            res2=x[4]
            if ce.startswith==cedula:
                return (ce,sin,res,sin2,res2)



# Función para actualizar datos de un paciente, medico y examene

def actualizar_paciente(cedula, datos_actualizados):
    paciente = buscar_paciente(cedula)
    with open('resultados_final.txt','w',encoding='utf8') as file:
        for resultado in resultados:
            file.write(resultado+'\n')
    
def actualizar_medicos(cedula, datos_actualizados):
    medicos = buscar_medico(cedula)
    if medicos:
        medicos.update(datos_actualizados)
def actualizar_examenes(cedula, datos_actualizados):
    resultados= buscar_examenes(cedula)
    
    resultados.update(datos_actualizados)

# Función para eliminar un paciente
def eliminar_paciente(cedula):
    paciente = buscar_paciente(cedula)
    if paciente:
        pacientes.remove(paciente)
def eliminar_medico(cedula):
    medicos = buscar_medico(cedula)
    if medicos:
        medicos.remove()
def eliminar_examen(cedula):
    paciente = buscar_examenes(cedula)
    if paciente:
        pacientes.remove(paciente)

# Función para añadir un nuevo paciente
def añadir_paciente(nuevo_paciente):
    if buscar_paciente(nuevo_paciente['cedula']):
        print('Error: La cedula ya existe')
    else:
        pacientes.append(nuevo_paciente)
def añadir_paciente(nuevo_paciente):
    if buscar_paciente(nuevo_paciente['cedula']):
        print('Error: La cedula ya existe')
    else:
        pacientes.append(nuevo_paciente)
def añadir_paciente(nuevo_paciente):
    if buscar_paciente(nuevo_paciente['cedula']):
        print('Error: La cedula ya existe')
    else:
        pacientes.append(nuevo_paciente)

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
        zac=buscar_paciente(cedula)
        tac=buscar_examenes(cedula)
        mac=buscar_medico(cedula)
        with open('output.txt','w',encoding='utf8') as file:
            p=f'|Datos Generales||{zac[0]}|{zac[1]}|{zac[3]}|{mac[1]}|Resultado prueba de gripe y fiebre|Fiebre|{tac[4]}|Gripe||{tac[2]}|||||||\n'
            file.write(p)
        print(f'|Datos Generales||{zac[0]}|{zac[1]}|{zac[3]}|{mac[1]}|Resultado prueba de gripe y fiebre|Fiebre|{tac[4]}|Gripe||{tac[2]}|||||||\n')
        continue
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
                                nuevpo =(input("Ingrese los datos del nuevo paciente en formato JSON:"))
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
                                nuevpo =(input("Ingrese los datos del nuevo paciente en formato JSON:"))
                                añadir_paciente(nuevpo)
                                print('La informacion se ha guardado correctamente')
                            elif f=='2':
                                cedula = input("Ingrese la cédula del paciente: ")
                                eliminar_paciente(cedula)
                                print('La informacion se ha guardado correctamente')
                            elif f=='3':
                                cedula = input("Ingrese la cédula del paciente: ")
                                datos_actualizados = json.loads(input("Ingrese los datos actualizados del paciente en formato JSON: "))
                                actualizar_paciente(cedula, datos_actualizados)
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