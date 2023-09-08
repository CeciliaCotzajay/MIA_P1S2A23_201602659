import time
import random
from estructuras import MBR
import os

class mkdisk:

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
                        self.inicializar_MBR(kb)
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
            if(list_dir[2] == "user"):
                list_dir[2] = "cecic"
                list_dir.remove(list_dir[0])
                for l in list_dir:
                    palabra = palabra +"/"+ l
                self.path = palabra
        list_dir = self.path.split('/')
        if(list_dir[1]  == "home"):
            if(list_dir[2] != "cecic"):
                print(">Creando directorios")
                list_dir.insert(2,"cecic")
                #print("insertado, corregido")
                list_dir.remove(list_dir[0])
                for l in list_dir:
                    palabra = palabra +"/"+ l
                self.path = palabra
        #print(self.path)


    def inicializar_MBR(self,kb):
        date = self.obtener_time()
        sign = random.randint(0,100)
        nuevofit = self.fit[0]
        nuevo_size = self.size*kb
        with open(self.path, "rb+") as file:
            mbr = MBR(nuevo_size,date,sign,nuevofit)
            bytes = mbr.get_bytes()
            #print(bytes)
            #print(len(bytes))
            file.write(bytes)
        print("MBR inicializado correctamente!")
    
    def obtener_time(self):
        timeA = int(time.time())
        return timeA

    