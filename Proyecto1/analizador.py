from mkdisk import mkdisk
from rmdisk import rmdisk
from fdisk import fdisk
from rep import rep
from mount import mount
from unmount import unmount
from mkfs import mkfs

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
                print(">>>>Error: parámetro no aceptado en 'mkdisk': "+valor.upper()+">>>>")
                print("*****************************************************************************")
         #SE CREA EL DISCO
        disco.make_mkdisk()

    def analizar_rmdisk(self, parametros):
        parametros.remove(parametros[0])
        #INICIALIZA EL DISCRO
        disco = rmdisk() 
        for p in parametros:
             #SE OBTIENE EL TIPO Y EL PARAMETRO ACTUAL
            param = p.split('=')
            tipo = param[0]
            valor = param[1]
             #VERIFICA CUAL PARAMETRO ES PARA INICIALIZAR EL OBTJETO (LOS PARAMETROS YA VIENEN EN LOWERCASE)
            if (tipo == "path"):
                disco.path = valor 
            else:
                print(">>>>Error: parámetro no aceptado en 'rmdisk': "+valor.upper()+">>>>")
                print("*****************************************************************************")
         #SE CREA EL DISCO
        disco.make_rmdisk()

    def analizar_fdisk(self, parametros):
        parametros.remove(parametros[0])
        #INICIALIZA LA PARTICION
        particion = fdisk() 
        try:
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
                    particion.add = int(valor)
                else:
                    print(">>>>Error: parámetro no aceptado en 'fdisk': "+valor.upper()+">>>>")
                    print("*****************************************************************************")
        except:
            print(">>>>Error: Recuperandose..>>>>")
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
                print(">>>>Error: parámetro no aceptado en 'rep': "+valor.upper()+">>>>")
                print("*****************************************************************************")
         #SE CREA EL REPORTE
        reporte.make_rep()

    def analizar_mount(self, parametros):
        parametros.remove(parametros[0])
        #INICIALIZA
        mo = mount()
        #IMPRIME LOS IDS SI NO VIENEN PARAMETROS
        if(parametros):
            for p in parametros:
                #SE OBTIENE EL TIPO Y EL PARAMETRO ACTUAL
                param = p.split('=')
                tipo = param[0]
                valor = param[1]
                #VERIFICA CUAL PARAMETRO ES PARA INICIALIZAR EL OBTJETO (LOS PARAMETROS YA VIENEN EN LOWERCASE)
                if (tipo == "path"):
                    mo.path = valor 
                elif (tipo == "name"):
                    mo.name = valor 
                else:
                    print(">>>>Error: parámetro no aceptado en 'mount': "+valor.upper()+">>>>")
                    print("*****************************************************************************")
            #SE CREA EL MOUNT
            mo.make_mount()
        else:
            #RECORRE EL MOUNT
            mo.recorrer()
            print("*****************************************************************************")

    def analizar_unmount(self, parametros):
        parametros.remove(parametros[0])
        #INICIALIZA EL DISCRO
        mo = unmount() 
        for p in parametros:
             #SE OBTIENE EL TIPO Y EL PARAMETRO ACTUAL
            param = p.split('=')
            tipo = param[0]
            valor = param[1]
             #VERIFICA CUAL PARAMETRO ES PARA INICIALIZAR EL OBTJETO (LOS PARAMETROS YA VIENEN EN LOWERCASE)
            if (tipo == "id"):
                mo.idm = valor 
            else:
                print(">>>>Error: parámetro no aceptado en 'unmount': "+valor.upper()+">>>>")
                print("*****************************************************************************")
         #SE CREA EL DISCO
        mo.make_unmount()
    
    def analizar_pause(self):
        response = str(input("PAUSE [c]:  ")).lower()
        if(response == 'c'):
            print("", end='')
        else:
            self.analizar_pause()

    def analizar_mkfs(self, parametros):
        parametros.remove(parametros[0])
        #INICIA
        mk = mkfs() 
        for p in parametros:
             #SE OBTIENE EL TIPO Y EL PARAMETRO ACTUAL
            param = p.split('=')
            tipo = param[0]
            valor = param[1]
             #VERIFICA CUAL PARAMETRO ES PARA INICIALIZAR EL OBTJETO (LOS PARAMETROS YA VIENEN EN LOWERCASE)
            if (tipo == "id"):
                mk.ids = valor
            elif (tipo == "type"):
                mk.type = valor 
            elif (tipo == "fs"):
                mk.fs = valor 
            else:
                print(">>>>Error: parámetro no aceptado en 'mkfs': "+valor.upper()+">>>>")
                print("*****************************************************************************")
         #SE CREA 
        mk.make_mkfs()

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
            self.analizar_rmdisk(comandos)
        elif (token == "fdisk"):
            print("comando fdisk".upper())
            self.analizar_fdisk(comandos)
        elif (token == "rep"):
            print("comando rep".upper())
            self.analizar_rep(comandos)
        elif (token == "mount"):
            print("comando mount".upper())
            self.analizar_mount(comandos)
        elif (token == "unmount"):
            print("comando unmount".upper())
            self.analizar_unmount(comandos)
        elif (token == "pause"):
            self.analizar_pause()
        elif (token == "mkfs"):
            print("comando mkfs".upper())
            self.analizar_mkfs(comandos)
        elif (token == ""):
            print("", end='')
        else:
            if(token[0]=="#"):
                print("",end="")
            else:
                print(">>>>Error: comando no aceptado.."+token.upper()+">>>>")
                print("*****************************************************************************")