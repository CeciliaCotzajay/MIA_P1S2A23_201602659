from estructuras import MBR
from estructuras import Partition

class fdisk:
    aux_s = 0

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
                        #AJUSTO EL SIZE
                        self.size = self.size * kb
                        # VALIDACION DE TYPE
                        if(self.type == ""):
                            self.type = "p"#P
                        if(self.type == "p" or self.type == "e" or self.type == "l"):
                            # VERIFICAR EXISTENCIA DE PATH
                            if(self.verificarDirectorio()):
                                mbr = self.obtener_mbr()
                                # VERIFICAR NO EXISTENCIA DE NOMBRE DE PARTICION
                                if(self.buscar_particion(self.name,mbr)):
                                    print(">>>>Ya existe una partición con ese nombre>>>>")
                                    print("**********************************************************")
                                else:
                                    #INSERTO SOLO CON FIRST-FIT
                                        part_position = self.first_fit(mbr)
                                        if(mbr.partitions[part_position].status == 'n'):
                                            #INSERTA LA PARTICION
                                            if(self.type == 'p'):  #PRIMARIA
                                                self.insertar_P_E(part_position,mbr)
                                                print(">>>>Particion Primaria creada exitosamente!>>>>")
                                                print("**********************************************************")
                                            if(self.type == 'e'):  #EXTENDIDA
                                                if(self.buscar_extendida(mbr)):
                                                    print(">>>>Ya existe una Particion extendida en el disco>>>>")
                                                    print("**********************************************************")
                                                else:
                                                    self.insertar_P_E(part_position,mbr)
                                                    print(">>>>Particion Extendida creada exitosamente!>>>>")
                                                    print("**********************************************************")
                                        else:
                                            print(">>>>Ya no hay espacio disponible>>>>")
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
        
    def obtener_mbr(self):
        mbr = MBR(0,0,0,' ')
        bytes = mbr.get_bytes()
        mbr_aux = MBR(0,0,0,' ')
        with open(self.path, "rb+") as file:
            bytes_obtenidos = file.read(len(bytes))
            mbr_aux.set_bytes(bytes_obtenidos)
            #print(bytes_obtenidos)
            #print(len(bytes_obtenidos))
        return mbr_aux
    
    def buscar_particion(self, nombre, mbr):
        for part in mbr.partitions:
            if(part.name == nombre):
                return True
        return False
    
    def first_fit(self, mbr):
        self.aux_s = 126
        part_position = 0
        for part in mbr.partitions:
            if(part.status == 'n'):
                break
            else:
                self.aux_s = self.aux_s + part.s
            part_position+=1
        return part_position
    
    def buscar_extendida(self, mbr):
        for part in mbr.partitions:
            if(part.type == 'e'):
                return True
        return False
    
    def insertar_P_E(self,part_position,mbr):
        #AJUSTAR_CADENAS
        self.name = self.ajustar_cadena(16,self.name)
        self.fit = self.ajustar_cadena(1,self.fit)
        #CREA PARTICION     
        par_set = Partition('s',self.type,self.fit,self.aux_s,self.size,self.name)
        mbr.partitions[part_position] = par_set
        with open(self.path, "rb+") as file:
            bytes = mbr.get_bytes()
            #print(bytes)
            #print(len(bytes))
            file.write(bytes)

    def ajustar_cadena(self,tam,cadena):
        if(len(cadena)<tam):
            dif = tam-len(cadena)
            for i in range(0,dif):
                cadena = cadena + " "
        if(len(cadena)>tam):
            new_cadena = ""
            for i in range(0,tam):
                new_cadena = new_cadena + cadena[i]
            cadena = new_cadena
        #print(cadena, "tam: ",str(len(cadena)))
        return cadena
