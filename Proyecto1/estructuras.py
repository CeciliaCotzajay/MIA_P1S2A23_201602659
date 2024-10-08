from abc import ABC, abstractmethod

#*****************************************ABSTRACTA********************************************
class Objeto(ABC):
    @abstractmethod
    def get_bytes(self):
        pass
    @abstractmethod
    def set_bytes(self, bytes):
        pass    
    @abstractmethod
    def get_size(self):
        pass

#*****************************************MBR**************************************************
class MBR(Objeto):

    def __init__(self, size, date, signature, fit): #125
        self.size = size # int (4 bytes)
        self.date = date # double (8 bytes)
        self.signature = signature # int (4 bytes)
        self.fit = fit # char (1 byte)
        self.partitions = [] #27bytes por cada una, 108 total
        self.partitions.append(Partition('n',' ',' ',0,0,"                "))
        self.partitions.append(Partition('n',' ',' ',0,0,"                "))
        self.partitions.append(Partition('n',' ',' ',0,0,"                "))
        self.partitions.append(Partition('n',' ',' ',0,0,"                "))

    def get_bytes(self):
        bytes = bytearray()
        bytes += self.size.to_bytes(4, byteorder='big')
        bytes += self.date.to_bytes(8, byteorder='big')
        bytes += self.signature.to_bytes(4, byteorder='big')
        bytes += self.fit.encode('utf-8')
        #print(len(bytes))
        for partition in self.partitions:
            bytes += partition.get_bytes()
            #print(len(bytes))
        return bytes

    def set_bytes(self, bytes):
        #print(len(bytes))
        self.size = int.from_bytes(bytes[0:4], byteorder='big')
        self.date = int.from_bytes(bytes[4:12], byteorder='big')
        self.signature = int.from_bytes(bytes[12:16], byteorder='big')
        self.fit = bytes[16:17].decode('utf-8')
        self.partitions = [] #108,27
        ini =17
        fin =ini+27
        for i in range(0,4):
            temp = Partition(' ',' ',' ',0,0,"                ")
            temp.set_bytes(bytes[ini:fin])
            self.partitions.append(temp)
            ini=fin
            fin+=27


    def get_size(self):
        size = 0
        size += 4
        size += 8
        size += 4
        size += 1
        for partition in self.partitions:
            size += partition.get_size()
        return size
            
    
#*****************************************PARTITION********************************************
class Partition(Objeto):

    def __init__(self, status, type, fit, start, s, name):# 27
        self.status = status #char (1 byte) ; activa o no activa, 's','n','m',e'
        self.type = type #char (1 byte)     ; p,e,l
        self.fit = fit #char (1 byte)       ; f,b,w
        self.start = start #int (4 bytes)   ; byte donde inicia
        self.s = s #int (4 bytes)           ; tamanio bytes
        self.name = name #char (16 bytes)   ; nombre

    def get_bytes(self):
        bytes = bytearray()
        bytes += self.status.encode('utf-8')
        bytes += self.type.encode('utf-8')
        bytes += self.fit.encode('utf-8')
        bytes += self.start.to_bytes(4, byteorder='big')
        bytes += self.s.to_bytes(4, byteorder='big')
        bytes += self.name.encode('utf-8')
        return bytes

    def set_bytes(self, bytes):
        self.status = bytes[0:1].decode('utf-8')
        self.type = bytes[1:2].decode('utf-8')
        self.fit = bytes[2:3].decode('utf-8')
        self.start = int.from_bytes(bytes[3:7], byteorder='big')
        self.s = int.from_bytes(bytes[7:11], byteorder='big')
        self.name = bytes[11:27].decode('utf-8')

    def get_size(self):
        size = 0
        size += 1
        size += 1
        size += 1
        size += 4
        size += 4
        size += 16
        return size
    
#*****************************************PARTITION********************************************

class EBR(Objeto):

    def __init__(self,status,fit,start,s,nextB,name):#30
        self.status = status # char (1 byte)    ; activa o no activa, 's','n','m',e'
        self.fit = fit # char (1 byte)          ; b,f,w
        self.start = start # int (4 bytes)      ; byte donde inicia
        self.s = s # int (4 bytes)              ; tamanio bytes
        self.nextB = nextB # int (4 bytes)      ; byte donde inicia el siguiente EBR
        self.name = name #char (16 bytes)       ; nombre

    def get_bytes(self):
        bytes = bytearray()
        bytes += self.status.encode('utf-8')
        bytes += self.fit.encode('utf-8')
        bytes += self.start.to_bytes(4, byteorder='big')
        bytes += self.s.to_bytes(4, byteorder='big')
        bytes += self.nextB.to_bytes(4, byteorder='big')
        bytes += self.name.encode('utf-8')
        #print(len(bytes))
        return bytes

    def set_bytes(self, bytes):
        #print(len(bytes))
        self.status = bytes[0:1].decode('utf-8')
        self.fit = bytes[1:2].decode('utf-8')
        self.start = int.from_bytes(bytes[2:6], byteorder='big')
        self.s = int.from_bytes(bytes[6:10], byteorder='big')
        self.nextB = int.from_bytes(bytes[10:14], byteorder='big')
        self.name = bytes[14:30].decode('utf-8')


    def get_size(self):
        size = 0
        size += 1
        size += 1
        size += 4
        size += 4
        size += 4
        size += 16
        return size