import os


class rep:

    def __init__(self):
        self.name = ""
        self.path = ""
        self.ids = ""
        self.ruta = ""

    def make_rep(self):
        #SI LOS PARAMETROS OBLIGATORIOS NO ESTAN VACIOS
        if(self.name != "" and self.path != "" and self.ids != ""):
            # EXTRAIGO DIRECTORIO PARA VER SI EXISTE
            self.verificarDirectorio()
            # CREA DIRECTORIO EN CASO NO EXISTA
            directorio = os.path.split(self.path)
            os.makedirs(directorio[0], exist_ok=True)
            # CREO EL REPORTE SEGUN SU NAME
            if (self.name == "mbr"):
                self.make_Rmbr(directorio)
            elif (self.name == "disk"):
                self.make_Rdisk(directorio)
            elif (self.name == "inode"):
                self.make_Rinode(directorio)
            elif (self.name == "journaling"):
                self.make_Rjournaling(directorio)
            elif (self.name == "block"):
                self.make_Rblock(directorio)
            elif (self.name == "bm_inode"):
                self.make_RbmInode(directorio)
            elif (self.name == "bm_block"):
                self.make_Rbmblock(directorio)
            elif (self.name == "tree"):
                self.make_Rtree(directorio)
            elif (self.name == "sb"):
                self.make_Rsb(directorio)
            elif (self.name == "file"):
                self.make_Rfile(directorio)
            elif (self.name == "ls"):
                self.make_Rls(directorio)
            else:
                print(">>>>Error: nombre no aceptado en 'rep'.."+self.name.upper()+">>>>")
                print("**********************************************************")
        else:
            print(">>>>Error: parámetros obligatorios: name, path e id>>>>")
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
        print(self.path)


    def make_Rmbr(self, directorio):
        print("repote mbr".upper())
        dir = directorio[0]
        nom = directorio[1]
        with open(self.path, "wb") as file:
            for i in range(0,self.size):
                file.write(b'\x00' * kb)
            print("unit: " + str(self.unit))
            print(">>>>Reporte MBR generado exitosamente!>>>>")
            print("**********************************************************")
        
    
    def make_Rdisk(self, directorio):
        print("reporte disk".upper())
    
    def make_Rinode(self, directorio):
        print("reporte inode".upper())
    
    def make_Rblock(self, directorio):
        print("reporte block".upper())

    def make_RbmInode(self, directorio):
        print("reporte bm_inode".upper())

    def make_Rbmblock(self, directorio):
        print("reporte bm_block".upper())
    
    def make_Rtree(self, directorio):
        print("reporte tree".upper())

    def make_Rsb(self, directorio):
        print("reporte sb".upper())

    def make_Rfile(self, directorio):
        print("reporte file".upper())

    def make_Rls(self, directorio):
        print("reporte disk".upper())

    def make_Rjournaling(self, directorio):
        print("reporte ls".upper())
