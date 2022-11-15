class Patient():
    ##Atributos##
    name_patient=''         ##nombre paciente
    last_name=''            ##Apellido
    date_of_birthday=''     ##fecha de Nacimiento
    run=''                  ##RUN
    address=''              ##direccion  
    bloody_group=''         ##grupo sanguineo
    medical_history=''      ##historial medico
    ##Fin atributos##

    ##metodos##
    def __init__(self,name,last,birthday,run,address,bloody_group,past):
        self.name_patient=name
        self.last_name=last
        self.date_of_birthday=birthday
        self.run=run
        self.address=address
        self.bloody_group=bloody_group
        self.medical_history=past

    def imprimir(self):
        print(self.name_patient)
        print(self.last_name)
        print(self.date_of_birthday)
        print(self.run)
        print(self.address)
        print(self.bloody_group)
        print(self.medical_history)
    ##Fin Metodos##

print("Ingrese los Datos del Paciente: ")
name = input("Nombre: ")
last = input("Apellido: ")
birthday = input("Fecha de Nacimiento: ")
run = input("Run: ")
address = input("Domicilio: ")
bloody_group = input("Grupo sanguineo: ")
past = input("Enfermedad prescrita: ")
