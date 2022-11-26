class Singleton:

    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton Exists Already!")
        else:
            Singleton.__instance = self

# s1 = Singleton.getInstance()
# print(s1)
# s1.x = 5
# s2 = Singleton.getInstance()
# print(s2)
# print(s2.x)
