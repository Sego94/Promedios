#TRABAJO DE CLASE 1: Programa de promedios.

#Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
#Se pide imprimir el nombre, el apellido y el promedio.
#Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". Caso contrario, si tiene menos de 4 puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
#En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".


#Con esta función se imprime el nombre y apellido y se calcula el promedio de las notas:
def notas_materias():
    nombre = input('Ingresa el Nombre: ')
    apellido = input('Ingresa el Apellido: ')
    nota_1 = int(input('Introduce Nota de Matemáticas: '))
    nota_2 = int(input('Introduce Nota de Literatura: '))
    nota_3 = int(input('Introduce Nota de Física: '))
    notas = nota_1+nota_2+nota_3
    materias = len(['nota_1', 'nota_2', 'nota_3'])
    print (nombre, apellido)
    return notas/materias
    

nota_media = notas_materias()

# Se imprime el resultado del promedio de las notas
if nota_media > 6:
    print('Nota media: {0:.2f}'.format(nota_media) + ' Aprobado')
    if nota_media >= 9:
      print('Alumno destacado')
elif nota_media < 4:
    print('Nota media: {0:.2f}'.format(nota_media) + ' Insuficiente')
else:
    print('Nota media: {0:.2f}'.format(nota_media) + ' A recuperatorio')
    


    