class mkdisk:
    position = 0

    def __init__(self, size,path,fit, unit):
        self.size = size #int
        self.path = path #string
        self.fit = fit   #string 2
        self.unit = unit #char

    def make_mkdisk(self):
        #colocar la creacion del disco o el archivo binario
        with open("disco"+str(self.tamano)+".bin", "wb") as file:
            size_megabyte = 1024 * 1024
            for i in range(0,self.tamano):
                file.write(b'\x00' * size_megabyte)
            file.close()
        print("Se creo disco"+str(self.tamano)+" exitosamente!")
        self.inicializar_MBR()

    def inicializar_MBR(self):
        with open("disco"+str(self.tamano)+".bin", "rb+") as file:
            file.seek(self.position)
            texto = f"{self.tamano}\n{self.fecha_creacion}\n{self.signature}\n"
            file.write(texto.encode('utf-8'))
            self.position = self.position+len(texto)
            file.close()
        print("MBR inicializado correctamente!")

    def leerMBR(self):
        with open("disco"+str(self.tamano)+".bin", "rb+") as file:
            objeto_recuperado = file.read().decode('utf-8')
            atributos = objeto_recuperado.split("\n")
            tam = int(atributos[0])
            #tiempo = atributos[1]
            sig = int(atributos[2])
            print("Tipo: ",tam)
            #print("Id: ",prof.id_profesor)
            print("sig: ",sig)