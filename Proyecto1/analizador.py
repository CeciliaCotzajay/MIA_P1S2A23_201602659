from mkdisk import mkdisk
from fdisk import fdisk
from rep import rep

class analizador:

    def analizar_mkdisk(self, parametros):
        parametros.remove(parametros[0])
        #INICIALIZA EL DISCRO
        disco = mkdisk() 
        for p in parametros:
             #SE OBTIENE EL TIPO Y EL PARAMETRO ACTUAL
            param = p.split('=')
            tipo = param[0]
            valor = param[1]
             #VERIFICA CUAL PARAMETRO ES PARA INICIALIZAR EL OBTJETO (LOS PARAMETROS YA VIENEN EN LOWERCASE)
            if (tipo == "size"):
                disco.size = int(valor)
            elif (tipo == "path"):
                disco.path = valor 
            elif (tipo == "unit"):
                disco.unit = valor 
            elif (tipo == "fit"):
                disco.fit = valor 
            else:
                print(">>>>Error: parámetro no aceptado en 'mkdisk'.."+valor.upper()+">>>>")
                print("*****************************************************************************")
         #SE CREA EL DISCO
        disco.make_mkdisk()

    def analizar_fdisk(self, parametros):
        parametros.remove(parametros[0])
        #INICIALIZA LA PARTICION
        particion = fdisk() 
        for p in parametros:
             #SE OBTIENE EL TIPO Y EL PARAMETRO ACTUAL
            param = p.split('=')
            tipo = param[0]
            valor = param[1]
             #VERIFICA CUAL PARAMETRO ES PARA INICIALIZAR EL OBJETO (LOS PARAMETROS YA VIENEN EN LOWERCASE)
            if (tipo == "size"):
                particion.size = int(valor)
            elif (tipo == "path"):
                particion.path = valor 
            elif (tipo == "name"):
                particion.name = valor 
            elif (tipo == "unit"):
                particion.unit = valor
            elif (tipo == "type"):
                particion.type = valor
            elif (tipo == "fit"):
                particion.fit = valor 
            elif (tipo == "delete"):
                particion.delete = valor 
            elif (tipo == "add"):
                if(valor == ''):
                    valor = '0'
                    p = 'add=0'
                particion.add = int(valor)
            else:
                print(">>>>Error: parámetro no aceptado en 'fdisk'.."+valor.upper()+">>>>")
                print("*****************************************************************************")
         #SE CREA LA PARTICION
        particion.make_fdisk()

    def analizar_rep(self, parametros):
        parametros.remove(parametros[0])
        #INICIALIZA EL REPORTE
        reporte = rep() 
        for p in parametros:
             #SE OBTIENE EL TIPO Y EL PARAMETRO ACTUAL
            param = p.split('=')
            tipo = param[0]
            valor = param[1]
             #VERIFICA CUAL PARAMETRO ES PARA INICIALIZAR EL OBTJETO (LOS PARAMETROS YA VIENEN EN LOWERCASE)
            if (tipo == "name"):
                reporte.name = valor
            elif (tipo == "path"):
                reporte.path = valor 
            elif (tipo == "id"):
                reporte.ids = valor 
            elif (tipo == "ruta"):
                reporte.ruta = valor 
            else:
                print(">>>>Error: parámetro no aceptado en 'rep'.."+valor.upper()+">>>>")
                print("*****************************************************************************")
         #SE CREA EL REPORTE
        reporte.make_rep()

    def analizar(self, linea):
        nueva_linea = linea.replace(" ","")
        try:
            comandos = nueva_linea.split('-')
        except:
            print(linea)
        token = comandos[0]
        if (token == "execute"):
            print("comando execute".upper())
            #self.analizar_rep()
        elif (token == "mkdisk"):
            print("comando mkdisk".upper())
            self.analizar_mkdisk(comandos)
        elif (token == "rmdisk"):
            print("comando rmdisk".upper())
            #self.analizar_rep()
        elif (token == "fdisk"):
            print("comando fdisk".upper())
            self.analizar_fdisk(comandos)
        elif (token == "rep"):
            print("comando rep".upper())
            self.analizar_rep(comandos)
        elif (token == ""):
            print("", end='')
        else:
            if(token[0]=="#"):
                print("",end="")
            else:
                print(">>>>Error: comando no aceptado.."+token.upper()+">>>>")
                print("*****************************************************************************")