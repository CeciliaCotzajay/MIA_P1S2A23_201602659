from estructuras import *

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
                        print("*****************************************************************************")
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
                                    print("*****************************************************************************")
                                else:
                                    #INSERTO SOLO CON FIRST-FIT
                                    if(self.type == 'p' or self.type == 'e'):
                                        part_position = self.first_fit(mbr)
                                        if(mbr.partitions[part_position].status == 'n'):
                                            if(self.type == 'p'):  #PRIMARIA
                                                self.insertar_P_E(part_position,mbr)
                                                print(">>>>Particion Primaria creada exitosamente!>>>>")
                                                print("*****************************************************************************")
                                            if(self.type == 'e'):  #EXTENDIDA
                                                if(self.buscar_extendida(mbr)):
                                                    print(">>>>Ya existe una Particion extendida en el disco>>>>")
                                                    print("*****************************************************************************")
                                                else:
                                                    self.insertar_P_E(part_position,mbr)
                                                    #INSERTAR EBR
                                                    print(">>>>Particion Extendida creada exitosamente!>>>>")
                                                    print("*****************************************************************************")
                                        else:
                                            print(">>>>Ya no hay espacio disponible>>>>")
                                            print("*****************************************************************************")

                                    if(self.type == 'l'):  #LOGICA
                                        if(self.buscar_extendida(mbr)):
                                            self.insertar_logica(mbr)
                                            print(">>>>Particion Logica creada exitosamente!>>>>")
                                            print("*****************************************************************************")

                                        else:
                                            print(">>>>No existe una Particion extendida en el disco>>>>")
                                            print("*****************************************************************************")
                            else:
                                print(">>>>Error: No se encontró el disco>>>>")
                                print("*****************************************************************************")
                        else:
                            print(">>>>Error: type debe ser 'P' o 'E' o 'L'..>>>>")
                            print("*****************************************************************************")
                else:
                    print(">>>>Error: fit debe ser 'BF' o 'FF' o 'WF'..>>>>")
                    print("*****************************************************************************")
            else:
                print(">>>>Error: La partición no puede tener tamaño: " + self.size + ">>>>")
                print("*****************************************************************************")
        
        else:
            print(">>>>Error: parámetros obligatorios: size, path y name>>>>")
            print("*****************************************************************************")
        
    def verificarDirectorio(self):
        self.arreglar_Directorio()
        try:
            with open(self.path, "rb+") as file:
                file.close()
                return True
        except:
            return False
    
    def arreglar_Directorio(self):
        palabra = ""
        directorio = self.path.replace("\"","")
        self.path = directorio
        list_dir = directorio.split('/')
        if(list_dir[1]  != "home"):
            list_dir.insert(1,"home")
            list_dir.remove(list_dir[0])
            for l in list_dir:
                palabra = palabra +"/"+ l
            self.path = palabra
            palabra = ""
        if(list_dir[1]  == "home"):
            if(list_dir[2] == "user"):
                list_dir[2] = "cecic"
                list_dir.remove(list_dir[0])
                for l in list_dir:
                    palabra = palabra +"/"+ l
                self.path = palabra
                palabra = ""
        list_dir = self.path.split('/')
        if(list_dir[1]  == "home"):
            if(list_dir[2] != "cecic"):
                list_dir.insert(2,"cecic")
                list_dir.remove(list_dir[0])
                for l in list_dir:
                    palabra = palabra +"/"+ l
                self.path = palabra
        
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
        self.name = self.name.replace("\"","")
        self.name = self.ajustar_cadena(16,self.name)
        self.fit = self.ajustar_cadena(1,self.fit)
        #CREA PARTICION
        par_set = Partition('s',self.type,self.fit,self.aux_s,self.size,self.name)
        mbr.partitions[part_position] = par_set
        with open(self.path, "rb+") as file:
            bytes = mbr.get_bytes()
            file.write(bytes)
            # SOLO SI ES EXTENDIDA
            if(self.type == 'e'):
                #CREA PRIMER EBR
                ebr = EBR('n',' ',self.aux_s,0,0,"                ")
                bytes_ebr = ebr.get_bytes()
                file.seek(self.aux_s)
                file.write(bytes_ebr)
        

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
        return cadena
    
    def first_fit_logica(self, mbr):
        p = Partition('n',' ',' ',0,0,"                ")
        for part in mbr.partitions:
            if(part.type == 'e'):
                p = part
        return p
    
    def modificar_EBR(self,ebr,fit):
        #AJUSTAR_CADENAS
        self.name = self.name.replace("\"","")
        self.name = self.ajustar_cadena(16,self.name)
        self.fit = self.ajustar_cadena(1,self.fit)
        ebr.status = 's'
        ebr.fit = fit
        ebr.s = self.size
        ebr.nextB = ebr.start + ebr.s
        ebr.name = self.name
        return ebr
    
    def insertar_logica(self,mbr):
        p_e = self.first_fit_logica(mbr)
        ebr_act = EBR('n',' ',0,0,0,"                ")
        bytes_act = ebr_act.get_bytes()
        with open(self.path, "rb+") as file:
            #PRIMER EBR
            file.seek(p_e.start)
            bytes_obtenidos = file.read(len(bytes_act))
            ebr_act.set_bytes(bytes_obtenidos)
            if(ebr_act.status == 'n'):
                #MODIFICO PRIMER EBR
                #COLOCO LA POSICION DEL PUNTERO EN POSITION, SI LO PONGO DIRECTO NO FUNCIONA, LE DA ANSIEDAD
                position = int(p_e.start)
                ebr_act = self.modificar_EBR(ebr_act,p_e.fit)
                bytes_ebr_act = ebr_act.get_bytes()
                file.seek(position)
                file.write(bytes_ebr_act)
                #CREO EBR SIGUIENTE (ULTIMO)
                #COLOCO LA POSICION DEL PUNTERO EN POSITION_ULTIMO, SI LO PONGO DIRECTO NO FUNCIONA, LE DA ANSIEDAD
                position_ultimo = int(ebr_act.nextB)
                nue_ebr = EBR('n',' ',ebr_act.nextB,0,0,"                ")
                bytes_nue_ebr = nue_ebr.get_bytes()
                file.seek(position_ultimo)
                file.write(bytes_nue_ebr)
            else:
                buscar = True
                pos = ebr_act.nextB
                ebr_rec = EBR('n',' ',0,0,0,"                ")
                bytes_ebr_rec = ebr_rec.get_bytes()
                while(buscar):
                    file.seek(pos)
                    bytes_rec = file.read(len(bytes_ebr_rec))
                    ebr_rec.set_bytes(bytes_rec)
                    if(ebr_rec.status == 'n'):
                        #MODIFICO EBR ACTUAL
                        #COLOCO LA POSICION DEL PUNTERO EN POSITION, SI LO PONGO DIRECTO NO FUNCIONA, LE DA ANSIEDAD
                        position = int(ebr_rec.start)
                        ebr_rec = self.modificar_EBR(ebr_rec,p_e.fit)
                        bytes_ebr_rec2 = ebr_rec.get_bytes()
                        file.seek(position)
                        file.write(bytes_ebr_rec2)
                        #CREO EBR SIGUIENTE (ULTIMO)
                        #COLOCO LA POSICION DEL PUNTERO EN POSITION_ULTIMO, SI LO PONGO DIRECTO NO FUNCIONA, LE DA ANSIEDAD
                        position_ultimo = int(ebr_rec.nextB)
                        nue_ebr = EBR('n',' ',ebr_rec.nextB,0,0,"                ")
                        bytes_nue_ebr = nue_ebr.get_bytes()
                        file.seek(position_ultimo)
                        file.write(bytes_nue_ebr)
                        buscar = False
                    else:
                        pos = ebr_rec.nextB