class Utils:
    @staticmethod
    def lookup(name, lst, func):
        for x in lst.sym:
            if name == func(x):
                return x
        return None

