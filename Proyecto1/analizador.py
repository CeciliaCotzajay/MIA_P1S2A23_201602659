from mkdisk import mkdisk

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
                print("**********************************************************")
         #SE CREA EL DISCO
        disco.make_mkdisk()


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
            #self.analizar_rep()
        elif (token == "rep"):
            print("comando rep".upper())
            #self.analizar_rep()
        elif (token == ""):
            print("", end='')
        else:
            if(token[0]=="#"):
                print("",end="")
            else:
                print(">>>>Error: comando no aceptado.."+token.upper()+">>>>")
                print("**********************************************************")