alumnos = {}
cantidad = int(input("Introducir la cantidad de alumnos"))
for a in range(cantidad):
    alumno = input("Nombre del alumno")
    while alumno in alumnos:
        print("Alumno ya existe")
        alumno = input("Nombre del alumno")
    notas = []
    nota = int(input("Nota del alumno"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Nota del alumno"))
    alumnos[alumno] = notas.copy()
for alumno, notas in alumnos.items():
    print("La nota media obtenida es " % (alumno, sum(notas)/len(notas)))