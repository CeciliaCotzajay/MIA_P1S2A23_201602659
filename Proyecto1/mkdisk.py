import os

class mkdisk:
    position = 0

    def __init__(self):
        self.size = 0 #int
        self.path = "" #string
        self.fit = ""   #string 2
        self.unit = '' #char

    def make_mkdisk(self):
        #SI LOS PARAMETROS OBLIGATORIOS NO ESTAN VACIOS
        if(self.size != 0 and self.path != ""):
            #SI EL TAMAÑO DEL DISCO ES MAYOR A 0
            if(self.size > 0):
                # VALIDACION DE FIT
                if(self.fit == ""):
                    self.fit = "ff"#FF
                    self.fit = "ff"
                if(self.fit == "bf" or self.fit == "ff" or self.fit == "wf"):
                    #VALIDACION DE UNIT
                    kb = 0
                    if(self.unit == "k"):
                        kb = 1024
                    elif(self.unit == "m"):
                        kb = 1024 * 1024
                    elif(self.unit == ""):
                        kb = 1024 * 1024 #m
                        self.unit = "m"
                    else:
                        print(">>>>Error: unit debe ser 'K' o 'M'..>>>>")
                        print("**********************************************************")
                    if(kb != 0):
                        # EXTRAIGO DIRECTORIO PARA VER SI EXISTE
                        self.verificarDirectorio()
                        # CREA DIRECTORIO EN CASO NO EXISTA
                        directorio = os.path.split(self.path)
                        os.makedirs(directorio[0], exist_ok=True)
                        # CREO EL DISCO CON TODAS LAS VALIDACIONES
                        with open(self.path, "wb") as file:
                            for i in range(0,self.size):
                                file.write(b'\x00' * kb)
                            file.close()
                        #self.inicializar_MBR()
                        print("size: " + str(self.size))
                        print("path: " + self.path)
                        print("fit: " + self.fit)
                        print("unit: " + str(self.unit))
                        print(">>>>Disco creado exitosamente!>>>>")
                        print("**********************************************************")
                else:
                    print(">>>>Error: fit debe ser 'BF' o 'FF' o 'WF'..>>>>")
                    print("**********************************************************")
            else:
                print(">>>>Error: El disco no puede tener tamaño: " + self.size + ">>>>")
                print("**********************************************************")
        
        else:
            print(">>>>Error: parámetros obligatorios: size y path>>>>")
            print("**********************************************************")
            
    def verificarDirectorio(self):
        palabra = ""
        directorio = self.path.replace("\"","")
        list_dir = directorio.split('/')
        if(list_dir[1]  == "home"):
            if(list_dir[2] != "cecic"):
                print(">Creando directorios")
                list_dir.insert(2,"cecic")
                #print("insertado, corregido")
                list_dir.remove(list_dir[0])
                for l in list_dir:
                    palabra = palabra +"/"+ l
                self.path = palabra


    """def inicializar_MBR(self):
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
            print("sig: ",sig)"""