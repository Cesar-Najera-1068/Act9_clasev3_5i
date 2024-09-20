print("Actividad 9, Clase Humana.")
print("Cesar Najera Matricula: 2230805128 1068")
# ZONA DE CLASES (CLASS)

class Humano1068:
    # ZONA DE ATRIBUTOS DENTRO DE LA CLASE
    edad=0
    genero=""
    fechanacimiento=""
    nacionalidad=""
    colordepiel=""
    colordeojos=""



    # ZONA DE FUNCIONES DENTRO DE LA CLASE
    def correr1068(self,n):
        print(f"{n} esta corriendo ufff....")

    def leyendo1068(self,n):
        print(f"{n} esta leyendo, esta cosechando conocimiento")

    def tomando1068(self,n):
        print(f"{n} esta tomando agua, siempre hidratado asi es")

    def caminando1068(self,n):
        print(f"{n} esta caminando bien agusto")

    def hablando1068(self,n):
        print(f"{n} esta hablando sobre un chisme que se entero")

    def escuchando1068(self,n):
        print(f"{n} esta escuchando musica, esta pensando cosas")


#ZONA DE CREACION DE OBJETOS
Cesar=Humano1068()
Rodolfo=Humano1068()


    #ZONA DE USANDO OBJETOS
print("Resultados para Cesar: ")
print("Sus atributos son: ")
Cesar.edad=17
Cesar.genero="Masculino"
Cesar.fechanacimiento="24 de enero de 2007"
Cesar.nacionalidad="Mexicana"
Cesar.colordepiel="No prefiere decirlo"
Cesar.colordeojos="Cafe oscuro"
print(f"Edad: {Cesar.edad}")
print(f"Genero: {Cesar.genero}")
print(f"Fecha de nacimiento: {Cesar.fechanacimiento}")
print(f"Nacionalidad: {Cesar.nacionalidad}")
print(f"Color de piel: {Cesar.colordepiel}")
print(f"Color de ojos: {Cesar.colordeojos}")
print("------------------------------------")
print("Que cosas puede hacer: ")
Cesar.correr1068("Cesar")
Cesar.leyendo1068("Cesar")
Cesar.tomando1068("Cesar")
Cesar.caminando1068("Cesar")
Cesar.hablando1068("Cesar")
Cesar.escuchando1068("Cesar")
print("-------------------------------------")
print("Resultados para Rodolfo: ")
Rodolfo.edad=16
Rodolfo.genero="Masculino"
Rodolfo.fechanacimiento="22 de Octubre del 2007"
Rodolfo.nacionalidad="Mexicano"
Rodolfo.colordepiel="Blanco"
Rodolfo.colordeojos="Cafe oscuro"
print(f"Edad: {Rodolfo.edad}")
print(f"Genero: {Rodolfo.genero}")
print(f"Fecha de nacimiento: {Rodolfo.fechanacimiento}")
print(f"Nacionalidad: {Rodolfo.nacionalidad}")
print(f"Color de piel: {Rodolfo.colordepiel}")
print(f"Color de ojos: {Rodolfo.colordeojos}")
print("------------------------------------")
print("Que cosas puede hacer: ")
Rodolfo.correr1068("Rodolfo")
Cesar.leyendo1068("Rodolfo")
Cesar.tomando1068("Rodolfo")
Cesar.caminando1068("Rodolfo")
Cesar.hablando1068("Rodolfo")
Cesar.escuchando1068("Rodolfo")
print("-------------------------------------")

