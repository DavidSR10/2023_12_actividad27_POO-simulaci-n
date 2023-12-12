"""
Crear estas clases
Define los atributos, métodos, constructores... que consideres
necesarios.

cursos:id,nombre, creditos, añosdeestudio
alumno:id, nombre, email
matricula:idmatricula, fechamatricula, idalumno, idcurso

Necesitamos.
mostrar la ficha del curso
mostrar la ficha de alumno
alumno1 se matricula en un curso
alumno2 se matricula en dos cursos
mostrar los datos de matrículo
reto*:método que muestra las mátriculas realizadas en mi centro

"""
from termcolor import colored

class Curso:
    def __init__(self, id_curso, nombre, creditos, anos_de_estudio):
        self.id_curso = id_curso
        self.nombre = nombre
        self.creditos = creditos
        self.anos_de_estudio = anos_de_estudio

    def __str__(self):
        return colored(f"Curso {self.id_curso}: {self.nombre} ({self.creditos} créditos, {self.anos_de_estudio} años de estudio)", 'blue')


class Alumno:
    COLORS = ['green', 'yellow']  # Colores para cada Alumno

    def __init__(self, id_alumno, nombre, email):
        self.id_alumno = id_alumno
        self.nombre = nombre
        self.email = email

    def __str__(self):
        color = self.COLORS[self.id_alumno - 1]
        return colored(f"Alumno {self.id_alumno}: {self.nombre} ({self.email})", color)


class Matricula:
    matriculas_realizadas = []

    def __init__(self, id_matricula, fecha_matricula, id_alumno, id_curso):
        self.id_matricula = id_matricula
        self.fecha_matricula = fecha_matricula
        self.id_alumno = id_alumno
        self.id_curso = id_curso
        Matricula.matriculas_realizadas.append(self)

    def __str__(self):
        return colored(f"Matrícula {self.id_matricula} - Fecha: {self.fecha_matricula}, Alumno: {self.id_alumno}, Curso: {self.id_curso}", 'yellow')

    @classmethod
    def mostrar_matriculas_realizadas(cls):
        print(colored("\n--- Matrículas realizadas en el centro ---", 'magenta'))
        for matricula in cls.matriculas_realizadas:
            print(matricula)


# Crear instancias de Curso
curso1 = Curso(1, "Matemáticas", 4, 2)
curso2 = Curso(2, "Historia", 3, 2)

# Crear instancias de Alumno
alumno1 = Alumno(1, "Juan Pérez", "juan@email.com")
alumno2 = Alumno(2, "María Gómez", "maria@email.com")

# Mostrar ficha de curso y alumno con colores
print(curso1)
print(curso2)

print(alumno1)
print(alumno2)

# Matricular a los alumnos
matricula1 = Matricula(1, "2023-01-01", alumno1.id_alumno, curso1.id_curso)
matricula2 = Matricula(2, "2023-01-02", alumno2.id_alumno, curso1.id_curso)
matricula3 = Matricula(3, "2023-01-03", alumno2.id_alumno, curso2.id_curso)

# Mostrar datos de matrícula con colores
print(matricula1)
print(matricula2)
print(matricula3)

# Mostrar matrículas realizadas con colores
Matricula.mostrar_matriculas_realizadas()
