import datetime


class a1():
    clients: list
    login: str


    def __init__(self, size:int = 0):
        self.clients = []
        if size >= 0:
            self.clients = list(range(size+1))



class col_a1():
    c_a1: list

    def __init__(self):
        self.c_a1 = []
        for i in range(10):
            a = a1(i)
            a.login = f'login{i}'
            self.c_a1.append(a)

    def __str__(self):
        s_output = ""
        for a in self.c_a1:
            s_output += f"Login:{a.login} List:{a.clients}\n"

        return str(s_output)


class Msg():
    message: str
    who: str
    time: str

    def __init__(self, message, who, time=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        self.message = message
        self.who = who
        self.time = str(time)

    def __str__(self):
        return f"{self.who} ({str(self.time)}): {self.message}\n"


c = col_a1()
print(len(c.c_a1))
print(c)

l = 'login10'

print(l in [x.login for x in c.c_a1])

m = Msg('Hello', 'John')

chat = [Msg('_Message_' * i,'User'+str(i)) for i in range(10)]

print('\n'.join(map(str,chat)))


