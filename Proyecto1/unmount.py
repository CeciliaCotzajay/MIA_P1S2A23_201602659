from singleton import singleton
import singleton

class unmount:

    def __init__(self):
        self.idm = "" #string

    def make_unmount(self):
        #SI EL PARAMETRO NO ESTA VACIO
        if(self.idm != ""):
            #METODO VERIFICA LA EXISTENCIA DE IDMOUNT Y ELIMINA
            if(singleton.objL.list_Mounts):
                est = 0
                n = 0
                for m in singleton.objL.list_Mounts:
                    #VALIDA QUE NO ESTE EN LA LISTA
                    if(m.idmount == self.idm):
                        est = 1
                        singleton.objL.list_Mounts.pop(n)
                        self.recorrer()
                        print(">>>>Particion desmontada exitosamente!>>>>")
                        print("*****************************************************************************")
                        break
                    n += 1
                if(est == 0):
                    print(">>>>Esta Particion No esta montada, Id no existe.>>>>")
                    print("*****************************************************************************")
            else:
                print(">>>>Esta Particion No esta montada, Id no existe.>>>>")
                print("*****************************************************************************")
        else:
            print(">>>>Error: parámetro obligatorio: id>>>>")
            print("*****************************************************************************")
 
    def recorrer(self):
        if(singleton.objL.list_Mounts):
            for m in singleton.objL.list_Mounts:
                print(m.idmount,end="-->")
            print("")
        else:
            print("sin ids mount")
    