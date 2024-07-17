import csv
import math
with open('empleados.csv', 'r') as archivo:
    lineas = archivo.readlines()[1:]

lista = []
for linea in lineas:
    elementos = linea.strip().split(",")
    elementos[5] = elementos[5].strip()
    lista.append(elementos)

def listar_primeros20():
    for i, empleado in enumerate(lista[:20]):
        print(f"{i + 1}. {empleado}")
def listar():
    for i, empleado in enumerate(lista):
        print(f"{i + 1}. {empleado}") 

def actualizar():
    print("Actualizar apellido de un empleado")
    id_actualizar = input("Ingresa el ID del empleado que quieres actualizar: ")
    nuevo_apellido = input("Ingresa el nuevo apellido: ")

    for empleado in lista:
        if empleado[0] == id_actualizar:
            empleado[2] = nuevo_apellido
            print("Apellido actualizado con éxito.")
            break
    else:
        print("Empleado no encontrado.")

    with open('empleados.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["EMPLOYEE_ID","FIRST_NAME","LAST_NAME","EMAIL","SALARY","DEPARTMENT_NAME","STREET_ADDRESS","CITY,STATE_PROVINCE"])
        writer.writerows(lista)

def calcular_media_geometrica_sueldos():
    if not lista:
        print('No hay empleados en la lista.')
        return

    sueldos = [float(empleado[4]) for empleado in lista]

    # Calcular la media geométrica
    producto_sueldos = math.prod(sueldos)
    media_geometrica = producto_sueldos ** (1.0 / len(sueldos))

    print(f"Media geométrica de los sueldos: {media_geometrica:.2f}")

def registrar():
    print("Registrar nuevo empleado")
    id_nuevo = input("Ingresa el ID del nuevo empleado: ")
    nombre_nuevo = input("Ingresa el nombre del nuevo empleado: ")
    apellido_nuevo = input("Ingresa el apellido del nuevo empleado: ")
    email_nuevo = input("Ingresa el email del nuevo empleado: ")
    salario_nuevo = input("Ingresa el salario del nuevo empleado: ")
    departamento_nuevo = input("Ingresa el departamento del nuevo empleado: ")
    direccion_nuevo = input("Ingresa la dirección del nuevo empleado: ")
    ciudad_nuevo = input("Ingresa la ciudad del nuevo empleado: ")
    estado_nuevo = input("Ingresa el estado del nuevo empleado: ")

    nuevo_empleado = [id_nuevo, nombre_nuevo, apellido_nuevo, email_nuevo, salario_nuevo, departamento_nuevo, direccion_nuevo, ciudad_nuevo, estado_nuevo]
    lista.append(nuevo_empleado)


    with open('empleados.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["EMPLOYEE_ID","FIRST_NAME","LAST_NAME","EMAIL","SALARY","DEPARTMENT_NAME","STREET_ADDRESS","CITY,STATE_PROVINCE"])  
        writer.writerows(lista)

    print("Empleado registrado con éxito.")

def buscar():
    print("Buscar por ID")
    id_buscar = input("Ingresa el ID que buscas: ")
    for empleado in lista:
        if empleado[0] == id_buscar:
            print("Empleado encontrado:")
            print(f"ID: {empleado[0]}")
            print(f"Nombre: {empleado[1]}")
            print(f"Apellido: {empleado[2]}")
            print(f"Email: {empleado[3]}")
            print(f"Salario: {empleado[4]}")
            print(f"Departamento: {empleado[5]}")
            print(f"Direcion: {empleado[6]}")
            print(f"Ciudad: {empleado[7]}")
            print(f"Estado: {empleado[8]}")

            return
    print("Empleado no encontrado")

def menu():
    menu='''
    1. Registrar un Empleado
    2. Listar los 20 primeros Empleados
    3. Listar Todos los Empleados
    4. Modificar el Apellido
    5. Eliminar el Empleado
    6. Listar el Nombre completo del Empleado que más Gana
    7. Calcular Sueldo Líquido
    8. Calcular Promedio de sueldos
    9. Media geometrica
    10. Salir del programa

    '''
    print(menu)

def salario_maximo():
    if not lista:
        print('No hay empleados en la lista.')
        return

    max_salary = max(float(empleado[4]) for empleado in lista)
    max_salary_employees = [empleado for empleado in lista if float(empleado[4]) == max_salary]

    if max_salary_employees:
        
        with open('steven.King.txt', 'w') as archivo:
            for empleado in max_salary_employees:
                full_name = ' '.join([empleado[1], empleado[2]])
                archivo.write(f'{full_name}: {max_salary:.2f}\n')
        print(f'El salario máximo es de: {full_name} con un monto de:  {max_salary:.2f}')
        print('El salario máximo se ha guardado en el archivo salario_maximo.txt.')
    else:
        print('No se encontró un salario máximo.')
        
def calcular_sueldo_liquido():
    print("Sueldo Líquido de los Empleados:")
    print("====================================================================================")
    print("| Nombre Empleado | Sueldo Base | Descuento Salud | Descuento AFP | Sueldo Líquido |")
    print("====================================================================================")

    with open('sueldos_liquidos.csv', 'w', newline='') as sueldos:
        writer = csv.writer(sueldos)
        writer.writerow(["Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for empleado in lista:
            sueldo_base = float(empleado[4])
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
            nombre_empleado = f"{empleado[1]} {empleado[2]}"

            print(f"| {nombre_empleado:20} | {sueldo_base:10.2f} | {descuento_salud:10.2f} | {descuento_afp:10.2f} | {sueldo_liquido:10.2f} |")
            writer.writerow([nombre_empleado, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])

    print("=====================================================================================")

def eliminar():
    id_a_eliminar = int(input('Ingrese el ID de la persona a eliminar: '))
    encontrado = False
    for i, empleado in enumerate(lista):
        if int(empleado[0]) == id_a_eliminar:
            del lista[i]
            encontrado = True
            break
    if encontrado:
        print('Persona eliminada con éxito.')

        with open('empleados.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["EMPLOYEE_ID","FIRST_NAME","LAST_NAME","EMAIL","SALARY","DEPARTMENT_NAME","STREET_ADDRESS","CITY,STATE_PROVINCE"])
            writer.writerows(lista)
    else:
        print('ID no encontrado.')

def calcular_promedio_sueldos():
    if not lista:
        print('No hay empleados en la lista.')
        return

    sueldos = [float(empleado[4]) for empleado in lista]
    promedio_sueldo = sum(sueldos) / len(sueldos)

    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)

    max_sueldo_employees = [empleado for empleado in lista if float(empleado[4]) == max_sueldo]
    min_sueldo_employees = [empleado for empleado in lista if float(empleado[4]) == min_sueldo]

    print(f"Sueldo más alto: {max_sueldo_employees[0][1]} {max_sueldo_employees[0][2]} con un monto de: {max_sueldo:.2f}")
    print(f"Sueldo más bajo: {min_sueldo_employees[0][1]} {min_sueldo_employees[0][2]} con un monto de: {min_sueldo:.2f}")
    print(f"Sueldo promedio: {promedio_sueldo:.2f}")

while True:
    menu()
    op = int(input("Ingrese Una opcion: "))
    try:
        if op == 1:
            registrar()
            continue
        if op == 2:
            listar_primeros20()
            continue
        if op == 3:
            listar()
            continue
        if op == 4:
            actualizar()
            continue
        if op == 5:
            eliminar()
            continue
        if op == 6:
            salario_maximo()
            continue
        if op == 7:
            calcular_sueldo_liquido()
        if op == 8:
            calcular_promedio_sueldos()
        if op == 9:
            calcular_media_geometrica_sueldos()
        if op == 10:
            break
    except ValueError:
        op = int(input("Ingrese Una opcion Valida: "))

