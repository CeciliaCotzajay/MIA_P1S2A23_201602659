
import os
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import pandas as pd
import imgkit

class m(object):

    def __init__(self):
        #self.presentar()
        #self.crear_rep2()
        #self.bytesss()
        self.devolver_kb()
        self.path = ""

    def presentar(self):
        #
        """timestamp = int(time.time())
        print(timestamp)
        palabra = """
        ##
        path0 = input("Esperando comando:  ").lower()
        self.path = path0.replace(" ","")
        #
        """
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
        print(self.path)"""
        #
        directorio = os.path.split(self.path)
        print("directorio: " + directorio[0])
        print("nombre.ext: : " + directorio[1])
        ##


   
    def crear_rep1(self):
        dt =  {'column1':["AA","BBBB","CCC","DDDDD"],'column2':[143.40,144.60,153.40,92.50],'column3':[144.21,142.60,155.65,92.77]}

        cuadro = pd.DataFrame(data=dt)
        cuadro = cuadro.to_string(index= False,justify = 'center',col_space=12)


        img = Image.new('RGB', (800, 300), color = '#000080')#color(letra, fondo)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("LiberationMono-Regular",30)
        draw.multiline_text((50, 40),cuadro,(255,255,255),font=font, align='center')
        img.save('image.jpg')


    def crear_rep2(self):
        # Esquema del "documento" que vamos a crear con la tabla
        layout ="""        
        <html><head>
        <style>
        .dataframe {
            font-family: "Liberation Sans", Arial, helvetica, sans-serif;
            color: white;
            border-collapse: collapse;
            border: 1px solid grey;
        }
        .dataframe thead {
            background-color: #006080;
        }
        .dataframe th, td {
            padding: 5pt;
        }
        .center-table {
        margin: 0 auto;
        }
        </style>
        </head>
        <body>
        <table class="center-table">
          %s    <!--  Aqui se inserta la tabla -->
        </table>
        </body>
        </html>"""

        dt =  {'column1':["AA","BBBB","CCC","DDDDD"],'column2':[143.40,144.60,153.40,92.50],'column3':[144.21,142.60,155.65,92.77]}
        df = pd.DataFrame(data=dt)

        cuadro = layout % df.to_html(index=False,justify='center')

        # Guardar en un fichero png la imagen de la tabla anterior
        imgkit.from_string(cuadro, "tabla.png", {"xvfb": "", "transparent": ""})

        # Leer el fichero y pegarlo encima de nuestra imagen
        
        img = Image.new('RGB', (800, 300), color = '#000080')
        draw = ImageDraw.Draw(img)
        img_tabla = Image.open("tabla.png")
        img.paste(img_tabla, (50, 40), img_tabla)

    def bytesss(self):
        n=18
        fit = "A" * n  # Crear una cadena compuesta de n caracteres "A"
        encoded_fit = fit.encode('utf-8')  # Codificar la cadena en UTF-8
        size_in_bytes = len(encoded_fit)  # Obtener el tamaño en bytes

        print(f"Número de caracteres en 'fit': {n}")
        print(f"Tamaño en bytes de 'fit' codificado en UTF-8: {size_in_bytes} bytes")

        if(len(fit)<16):
            dif = 16-len(fit)
            for i in range(0,dif):
                fit = fit + " "
        if(len(fit)>16):
            new_fit = ""
            for i in range(0,16):
                new_fit = new_fit + fit[i]
            fit = new_fit
        print(fit, "tam: ",str(len(fit)))

    def devolver_kb(self):
        dif = 5242880
        letra = ''
        m = 1024*1024
        k = 1024
        print(str(dif//m))
        print(str(dif//k))
        entero_m = dif//m
        entero_k = dif//k
        if(entero_k == 0 and entero_m != 0):
            print('m')
        elif(entero_m == 0 and entero_k != 0):
            print('k')
        elif(entero_m != 0 and entero_k != 0):
            if(entero_m<entero_k):
                print('m')
            else:
                print('k')
        else:
            print('b')




obj = m()