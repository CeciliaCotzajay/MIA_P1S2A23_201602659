class fdisk:

    def __init__(self):
        self.size = 0
        self.path = ""
        self.name = ""
        self.unit = ''
        self.type = ''
        self.fit = ""
        self.delete = ""
        self.add = 0 #puede ser postivivo o negativo


    def make_fdisk(self):
        print("haciendo fdisk")
        #debe obtener el disco a traves del path o el nombre
        #del disco para hacer la respectiva insercion(modificacion de MBR)
        # OJO LO QUE SE modifica es el mbr y se crea el disco pero no se donde se guarda
        #SI LOS PARAMETROS OBLIGATORIOS NO ESTAN VACIOS
        if(self.size != 0 and self.path != "" and self.name != ""):
            #SI EL TAMAÑO DE LA PARTICION ES MAYOR A 0
            if(self.size > 0):
                # VALIDACION DE FIT
                if(self.fit == ""):
                    self.fit = "ff"#FF
                if(self.fit == "bf" or self.fit == "ff" or self.fit == "wf"):
                    #VALIDACION DE UNIT
                    kb = 0
                    if(self.unit == "b"):
                        kb = self.size
                    elif(self.unit == "k"):
                        kb = 1024
                    elif(self.unit == "m"):
                        kb = 1024 * 1024
                    elif(self.unit == ""):
                        kb = 1024 * 1024 #m
                        self.unit = "m"
                    else:
                        print(">>>>Error: unit debe ser 'B', 'K' o 'M'..>>>>")
                        print("**********************************************************")
                    if(kb != 0):
                        # VALIDACION DE TYPE
                        if(self.type == ""):
                            self.type = "p"#P
                        if(self.type == "p" or self.type == "e" or self.type == "l"):
                            # VERIFICAR EXISTENCIA DE PATH
                            if(self.verificarDirectorio()):
                                # VERIFICAR NO EXISTENCIA DE NOMBRE DE PARTICION
                                """with open(self.path, "rb+") as file:
                                    f
                                    file.close()"""
                                #self.inicializar_MBR()
                                print("size: " + str(self.size))
                                print("path: " + self.path)
                                print("name: " + self.name)
                                print("unit: " + str(self.unit))
                                print(">>>>Particion creada exitosamente!>>>>")
                                print("**********************************************************")
                            else:
                                print(">>>>Error: No se encontró el disco>>>>")
                                print("**********************************************************")
                        else:
                            print(">>>>Error: type debe ser 'P' o 'E' o 'L'..>>>>")
                            print("**********************************************************")
                else:
                    print(">>>>Error: fit debe ser 'BF' o 'FF' o 'WF'..>>>>")
                    print("**********************************************************")
            else:
                print(">>>>Error: La partición no puede tener tamaño: " + self.size + ">>>>")
                print("**********************************************************")
        
        else:
            print(">>>>Error: parámetros obligatorios: size, path y name>>>>")
            print("**********************************************************")
        
    def verificarDirectorio(self):
        directorio = self.path.replace("\"","")
        self.path = directorio
        try:
            with open(self.path, "rb+") as file:
                file.close()
                return True
        except:
            return False