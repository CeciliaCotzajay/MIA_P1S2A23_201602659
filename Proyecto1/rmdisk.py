from os import remove
import os

class rmdisk:

    def __init__(self):
        self.path = "" #string

    def make_rmdisk(self):
        #SI EL PARAMETRO NO ESTA VACIO
        if(self.path != ""):
            # VERIFICAR EXISTENCIA DE PATH
            if(self.verificarDirectorio()):
                #CONFIRMAR ELIMINACION
                self.confirmar_eliminacion()
            else:
                print(">>>>Error: No se encontró el disco>>>>")
                print("*****************************************************************************")
        else:
            print(">>>>Error: parámetro obligatorio: path>>>>")
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

    def confirmar_eliminacion(self):
        response = str(input("Alerta!!, se necesita confirmación para eliminar disco [s/n]: "+"\n")).lower()
        if(response == 's'):
            os.remove(self.path)
            print(">>>>Disco eliminado exitosamente!>>>>")
            print("*****************************************************************************")
        elif(response == 'n'):
            print(">>>>Eliminación del disco cancelada>>>>")
            print("*****************************************************************************")
        else:
            self.confirmar_eliminacion()