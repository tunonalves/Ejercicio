class Atleta():
    
    __lstAtleta = []

    __dni = 0
    __nombre = ""
    __apellido = ""
    __altura = 0.0
    __peso = 0.0
    __telefono = ""

#Construct

    def __init__(self,DNI,Nombre,Apellido,Altura,Peso,Telefono):
        self.__dni = DNI
        self.__nombre = Nombre
        self.__apellido = Apellido
        self.__altura = Altura
        self.__peso = Peso
        self.__telefono = Telefono
#GET

    def __getIMC(self):
        IMC = (self.__peso / self.__altura ** 2)
        if (IMC < 18,5):
            return "Peso Inferior" 
        elif (IMC > 19) and (IMC < 24,9):
            return "Peso Normal"
        elif (IMC > 25) and (IMC > 29,9):
            return "Sobrepeso"
        elif (IMC > 30) and (IMC > 34,9):
            return "Obesidad"
        elif (IMC > 35):
            return "Obesidad Extrema"
    
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDNI(self):
        return self.__dni
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
    def getTelefono(self):
        return self.__telefono
    def getIMC(self):
        return self.__getIMC()

    def getDatos(self):
        return f"\n\n DNI: {self.getDNI()} \n Nombre: {self.getNombre()} \n Apellido: {self.getApellido()} \n Altura: {self.getAltura()} \n Peso: {self.getPeso()} \n Telefono: {self.getTelefono()} \n Indice de Masa Corporal: {self.__getIMC()} \n"

# SET
    def setDNI(self,DNI):
        self.__dni = DNI
    def setNombre(self,Nombre):
        self.__nombre = Nombre
    def setApellido(self,Apellido):
        self.__apellido = Apellido
    def setAltura(self,Altura):
        self.__altura = Altura
    def setPeso(self,Peso):
        self.__peso = Peso
    def setTelefono(self,Telefono):
        self.__telefono = Telefono

    def setRegistroAtleta(self):
        atletas = (self.getDNI(),self.getNombre(),self.getApellido(),self.getAltura(),self.getPeso(),self.getTelefono())
        self.__lstAtleta.append(atletas)
    def getListaAtleta(self):
        return self.__lstAtleta