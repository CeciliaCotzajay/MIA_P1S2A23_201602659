class singleton(object):
    # lista de mount 
    list_Mounts = []
    __instance = None

    # SINGLETON
    def __new__(cls):
        if singleton.__instance is None:
            singleton._instance = object.__new__(cls)
        return cls._instance
    


objL = singleton()