from datetime import datetime
import os
import time
from PIL import Image
from PIL import ImageDraw 
import pandas as pd
import imgkit
from estructuras import EBR, MBR
import singleton

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
                print("*****************************************************************************")
        else:
            print(">>>>Error: parámetros obligatorios: name, path e id>>>>")
            print("*****************************************************************************")

    def make_Rmbr(self, directorio):
        print("repote mbr".upper())
        #CREA EL PATH
        self.verificarDirectorio()
        # CREA DIRECTORIO EN CASO NO EXISTA
        directorio = os.path.split(self.path)
        os.makedirs(directorio[0], exist_ok=True)
        #OBTIENE EL PATH DEL DISCO POR MEDIO DEL ID, OBTIENE EL MBR
        path_Disco = self.obtener_path()
        mbr = self.obtener_mbr(path_Disco)
        fechaInt = mbr.date
        fechaStr = self.castear_fecha(fechaInt)
        #OBTIENE LA DATA DEL MBR
        color = "Purple"
        dic_data = {'REPORTE MBR':[], 'non':[]}
        dic_data["REPORTE MBR"].append('mbr_tamano')
        dic_data["REPORTE MBR"].append('mbr_fecha_creacion')
        dic_data["REPORTE MBR"].append('mbr_disk_signature')
        dic_data["non"].append(str(mbr.size))
        dic_data["non"].append(str(fechaStr))
        dic_data["non"].append(str(mbr.signature))
        #OBTIENE LA DATA DE LAS PARTICIONES
        self.data_partitionsMBR(dic_data,mbr,path_Disco)
        #LLAMAR METODO TABLA PASARLE EL DICCIONARIO Y EL COLOR
        self.reporte_tabla(dic_data,color)
        print(">>>>Reporte MBR generado exitosamente!>>>>")
        print("*****************************************************************************")
        
    def make_Rdisk(self, directorio):
        print("reporte disk".upper())
        #CREA EL PATH
        self.verificarDirectorio()
        # CREA DIRECTORIO EN CASO NO EXISTA
        directorio = os.path.split(self.path)
        os.makedirs(directorio[0], exist_ok=True)
        #OBTIENE EL PATH DEL DISCO POR MEDIO DEL ID, OBTIENE EL MBR
        path_Disco = self.obtener_path()
        directorio2 = os.path.split(path_Disco)
        mbr = self.obtener_mbr(path_Disco)
        #RECORRER PARTICIONES 
        data = self.data_partitionsDisk(mbr,path_Disco)
        name_disk = directorio2[1]
        #CREAR SINTAXIS GRAPHVIZ DE LA DATA
        self.graphviz_disk(name_disk,data)
        print(">>>>Reporte DISK generado exitosamente!>>>>")
        print("*****************************************************************************")
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

#**********************************************************************************************
#***********************************METODOS_SECUNDARIOS****************************************
#**********************************************************************************************
    def reporte_tabla(self,data,color):
        # ESQUEMA DEL DOCUMENTO
        layout ="""        
        <html><head>
        <style>
        .dataframe {
            font-family: "Liberation Sans", Arial, helvetica, sans-serif;
            color: """+color+""";
            border-collapse: collapse;
            border: 1px solid grey;
        }
        .dataframe thead {
            background-color: """+color+""";
            color: white;
        }
        .dataframe th, td {
            padding: 5pt;
        }
        .dataframe td {
            padding: 5pt;
            background-color: #d4e3ec;
        }
        .center-table {
        margin: 0 auto;
        }
        </style>
        </head>
        <body style="background-color: black;">
        <center>
        <table>
          %s    <!--  Aqui se inserta la tabla -->
        </table>
        </center>
        </body>
        </html>"""

        #CONVIERTE LA DATA EN DICCIONARIO
        #t =  {'column1':["AA","BBBB","CCC","DDDDD"],'column2':[143.40,144.60,153.40,92.50],'column3':[144.21,142.60,155.65,92.77]}
        dt = data
        df = pd.DataFrame(data=dt)
        cuadro = layout % df.to_html(index=False,justify='center')
        #CREA ARCHIVO TIPO PNG O JPG Y PEGA LA TABLA
        imgkit.from_string(cuadro, self.path, {"xvfb": ""})
        img = Image.new('RGB', (800, 1000), color = '#000080')
        draw = ImageDraw.Draw(img)
        img_tabla = Image.open(self.path)
        img.paste(img_tabla, (50, 40), img_tabla)

    def obtener_path(self):
        path_en = ""
        if(singleton.objL.list_Mounts):
            for m in singleton.objL.list_Mounts:
                if(m.idmount == self.ids):
                    path_en = m.path
        return path_en
    
    def obtener_mbr(self,pathDisco):
        mbr = MBR(0,0,0,' ')
        bytes = mbr.get_bytes()
        mbr_aux = MBR(0,0,0,' ')
        with open(pathDisco, "rb+") as file:
            bytes_obtenidos = file.read(len(bytes))
            mbr_aux.set_bytes(bytes_obtenidos)
        return mbr_aux
    
    def castear_fecha(self,fechaInt):
        fechaStr = ""
        fechaInt = int(time.time())
        fecha = datetime.fromtimestamp(fechaInt)
        fechaStr = fecha.strftime("%d/%m/%y %H:%M")
        return fechaStr
    
    def verificarDirectorio(self):
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
                print(">Creando directorios")
                list_dir.insert(2,"cecic")
                #print("insertado, corregido")
                list_dir.remove(list_dir[0])
                for l in list_dir:
                    palabra = palabra +"/"+ l
                self.path = palabra
        #print(self.path)

    def data_partitionsMBR(self,dic_data, mbr, pathDisco):
        for part in mbr.partitions:
            dic_data["REPORTE MBR"].append('PARTICION')
            dic_data["non"].append("VALUES")
            #PRIMARIA O EXTENDIDA
            dic_data["REPORTE MBR"].append('part_status')
            dic_data["REPORTE MBR"].append('part_type')
            dic_data["REPORTE MBR"].append('part_fit')
            dic_data["REPORTE MBR"].append('part_start')
            dic_data["REPORTE MBR"].append('part_size')
            dic_data["REPORTE MBR"].append('part_name')
            dic_data["non"].append(part.status)
            dic_data["non"].append(part.type)
            dic_data["non"].append(part.fit)
            dic_data["non"].append(str(part.start))
            dic_data["non"].append(str(part.s))
            dic_data["non"].append(part.name)
            #RECORRER LOGICAS SI ES EXTENDIDA
            if(part.type == "e"):
                ebr_act = EBR('n',' ',0,0,0,"                ")
                bytes_act = ebr_act.get_bytes()
                with open(pathDisco, "rb+") as file:
                    #PRIMER EBR
                    buscar = True
                    file.seek(part.start)
                    while(buscar):
                        dic_data["REPORTE MBR"].append('LOGICA')
                        dic_data["non"].append("VALUES")
                        bytes_obtenidos = file.read(len(bytes_act))
                        ebr_act.set_bytes(bytes_obtenidos)
                        dic_data["REPORTE MBR"].append('part_status')
                        dic_data["REPORTE MBR"].append('part_next')
                        dic_data["REPORTE MBR"].append('part_fit')
                        dic_data["REPORTE MBR"].append('part_start')
                        dic_data["REPORTE MBR"].append('part_size')
                        dic_data["REPORTE MBR"].append('part_name')
                        dic_data["non"].append(ebr_act.status)
                        dic_data["non"].append(str(ebr_act.nextB))
                        dic_data["non"].append(ebr_act.fit)
                        dic_data["non"].append(str(ebr_act.start))
                        dic_data["non"].append(str(ebr_act.s))
                        dic_data["non"].append(ebr_act.name)
                        #SALE DEL BUCLE SI ES EL ULTIMO
                        if(ebr_act.status == 'n'):
                            buscar = False
                        #ACTUALIZA EL PUNTERO
                        else:
                            position_ultimo = int(ebr_act.nextB)
                            file.seek(position_ultimo)

    def graphviz_disk(self,name_disk,data):
        esquema = """
                digraph D {
                subgraph cluster_1 {
                label =  \""""+name_disk+"""\"
                color=blue;

                node [fontname="Arial",style=filled];
                node_A [shape=record    label="MBR"""+data+"""\"];
                }    
                }
            """
        print(esquema)

    def data_partitionsDisk(self,mbr,pathDisco):
        data = """"""
        for part in mbr.partitions:
            if((part.status == "n") or(part.status == "e")):
                data += """|LIBRE"""
            #SI ES PRIMARIA
            elif(part.type == "p"):
                data += """|PRIMARIA"""
            #RECORRER LOGICAS SI ES EXTENDIDA
            elif(part.type == "e"):
                data += """|{EXTENDIDA|{"""
                ebr_act = EBR('n',' ',0,0,0,"                ")
                bytes_act = ebr_act.get_bytes()
                with open(pathDisco, "rb+") as file:
                    #PRIMER EBR
                    buscar = True
                    file.seek(part.start)
                    while(buscar):
                        bytes_obtenidos = file.read(len(bytes_act))
                        ebr_act.set_bytes(bytes_obtenidos)
                        data += """EBR|LOGICA"""
                        #SALE DEL BUCLE SI ES EL ULTIMO
                        if(ebr_act.status == 'n'):
                            buscar = False
                            data += """}}"""
                        #ACTUALIZA EL PUNTERO
                        else:
                            position_ultimo = int(ebr_act.nextB)
                            file.seek(position_ultimo)
                            data += """|"""
        return data

 