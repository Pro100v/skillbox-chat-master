from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

import datetime

class Client(Protocol):
    ip: str = None
    login: str = None
    factory: 'Chat'

    def __init__(self, factory):
        """
        Инициализация фабрики клиента
        :param factory:
        """
        self.factory = factory

    def connectionMade(self):
        """
        Обработчик подключения нового клиента
        """
        self.ip = self.transport.getHost().host
        self.factory.clients.append(self)

        print(f"Client connected: {self.ip}")

        self.transport.write("Welcome to the chat v0.1\n".encode())

    def dataReceived(self, data: bytes):
        """
        Обработчик нового сообщения от клиента
        :param data:
        """
        message = data.decode().replace('\n', '')

        if self.login is not None:
            # server_message = f"{self.login}: {message}"
            server_message = Msg(message, self.login)

            self.factory.notify_all_users(server_message)
            self.factory.chat_history.append(server_message)

            print(server_message)
        else:
            if message.startswith("login:"):
                self.login = message.replace("login:", "")

                if self.factory.user_exists(self.login):
                    notification = f"User with name '{self.login}' allready exists."
                    self.rejectUser(notification)
                else:
                    notification = f"WOW New user connected: {self.login}\n"
                    notification += '\n'.join(map(str,self.factory.chat_history[-10:]))
                    self.factory.notify_all_users(notification)

                print(notification)
            else:
                print("Error: Invalid client login")

    def connectionLost(self, reason=None):
        """
        Обработчик отключения клиента
        :param reason:
        """
        self.factory.clients.remove(self)
        print(f"Client disconnected: {self.ip}")

    def rejectUser(self, reason=""):
        """
        Обработчик отказа в регистрации

        :type reason: object
        :return:
        """
        notification = f"Access denied. {reason}\n"
        self.transport.write(notification.encode())
        self.connectionLost()


class Msg():
    message: str
    who: str
    time: str

    def __init__(self, message, who):
        self.message = message
        self.who = who
        self.time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f"{self.who} ({str(self.time)}): {self.message}\n"

class Chat(Factory):
    clients: list
    chat_history: list

    def __init__(self):
        """
        Инициализация сервера
        """
        self.clients = []
        print("*" * 10, "\nStart server \nCompleted [OK]")

        """
        По причине не работы ввода/вывода заглушка
        """
        self.chat_history = [Msg('_Message_' * i,'User'+str(i)) for i in range(10)]

    def startFactory(self):
        """
        Запуск процесса ожидания новых клиентов
        :return:
        """
        print("\n\nStart listening for the clients...")

    def buildProtocol(self, addr):
        """
        Инициализация нового клиента
        :param addr:
        :return:

        передать новому клиенту историю чата
        """
        return Client(self)

    def notify_all_users(self, data: str):
        """
        Отправка сообщений всем текущим пользователям
        :param data:
        :return:
        """
        for user in self.clients:
            user.transport.write(f"{data}\n".encode())

    def user_exists(self, name):
        # res = False
        # for user in self.clients[:-1]:
        #       res = user.login == name
        # return res
        return name in [user.login for user in self.clients[:-1]]


if __name__ == '__main__':
    reactor.listenTCP(7410, Chat())
    reactor.run()
