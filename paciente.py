class Patient():
    ##Atributos##
    name_patient=''         ##nombre paciente
    last_name=''            ##Apellido
    date_of_birthday=''     ##fecha de Nacimiento
    run=''                  ##RUN
    address=''              ##direccion  
    bloody_group=''         ##grupo sanguineo
    medical_history=''      ##historial medico
    phone=''                ##telefono o celular
    allergy=''              ##alergia
    detected=''             ##detectada
    allergic=''             ##alergico
    affiction=''            ##enfermedad
    ##Fin atributos##

    ##metodos##
    def __init__(self,name,last,birthday,run,address,bloody_group,phone,allergy,allergic,past,detected,affiction):
        self.name_patient=name
        self.last_name=last
        self.date_of_birthday=birthday
        self.run=run
        self.address=address
        self.bloody_group=bloody_group
        self.allergy=allergy
        self.allergic=allergic
        self.phone=phone
        self.medical_history=past
        self.detected=detected
        self.affiction=affiction

    def imprimir(self):
        print(self.name_patient)
        print(self.last_name)
        print(self.date_of_birthday)
        print(self.run)
        print(self.address)
        print(self.bloody_group)
        print(self.allergy)
        print(self.phone)
        print(self.medical_history)
        print(self.detected)
        print(self.affiction)
    ##Fin Metodos##

print("Ingrese los Datos del Paciente: ")
name = input("Nombre: ")
last = input("Apellido: ")
birthday = input("Fecha de Nacimiento: ")
run = input("Run (No punto ni guión): ")
address = input("Domicilio: ")
bloody_group = input("Grupo sanguineo: ")
phone = input("Ingrese su numero de telefono o celular: ")
allergy = input("¿Tiene alguna alergía (Si o No)?: ")
if allergy=="Si" or allergy=="si":
    allergic = input("¿A que tiene alergía?: ")
    past = input("Enfermedad prescrita (Si o No): ")
    if past=="si" or past=="Si":
        affiction = input("¿Que enfermedad Tiene?: ")
        detected = input("¿Desde hace cuanto? (expresar en meses): ")
        print("Ficha de: ")
        a=Patient(name,last,birthday,run,address,bloody_group,allergy,allergic,phone,past,affiction,detected)
        a.imprimir()
    else:
        print("Ficha de: ")
        a=Patient(name,last,birthday,run,address,bloody_group,allergy,allergic,phone,past)
        a.imprimir()
else:
    past = input("Enfermedad prescrita (Si o No): ")
    if past=="si" or past=="Si":
        affiction = input("¿Que enfermedad Tiene?: ")
        detected = input("¿Desde hace cuanto? (expresar en meses): ")
        print("Ficha de: ")
        a=Patient(name,last,birthday,run,address,bloody_group,allergy,phone,past,affiction,detected)
        a.imprimir()
    else:
        print("Ficha de: ")
        a=Patient(name,last,birthday,run,address,bloody_group,phone,allergy="No",allergic="No",past="No",affiction="No",detected="No")
        a.imprimir()
