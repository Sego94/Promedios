#Sacar promedio
def promedio (mate, literatura, fisica):
    return (mate+literatura+fisica)/3

#Imprimir datos
def datos_del_alumno(nombre, apellido, prom):
    print('El alumno '+nombre+' '+apellido+' tiene como promedio '+str(prom))

#Ver aprobación del alumno
def estado_aprobacion(prom):
    if prom >=6:
        print('El alumno aprobó')
        if prom >=9:
            print('Alumno destacado')
    elif prom >=4:
        print('A recuperatorio')
    else:
        print('Insuficiente')


nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
mate = int(input('Ingrese nota de matemáticas: '))
literatura = int(input('Ingrese nota de literatura: '))
fisica = int(input('Ingrese nota de fisica: '))

prom = promedio (mate, literatura, fisica)
datos_del_alumno(nombre, apellido, prom)
estado_aprobacion(prom)
