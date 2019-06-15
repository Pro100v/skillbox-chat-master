"""
Работа с TCP протоколами Twisted, базовой сервер
"""
from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol):
    def connectionMade(self):
        print("New client connected!")

    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
reactor.run()
