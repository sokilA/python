import socket
import threading
import sys
import pickle


class Cliente():
    def __init__(self, host="localhost", port=7000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))
        msg_recv = threading.Thread(target=self.msg_recv)
        msg_recv.daemon = True
        msg_recv.start()


def __init__(self, host="localhost", port=7000):
    while True:
        msg = input('-> ')
        if msg != 'salir':
            self.send_msg(msg)
        else:
            self.sock.close()
            sys.exit()


def msg_recv(self):
    while True:
        try:
            data = self.sock.recv(1028)
            if data:
                data = pickle.loads(data)
                print(data)
        except:
            pass


def send_msg(self, msg):
    try:
        self.sock.send(pickle.dumps(msg))
    except:
        print('error')


class Servidor():
    def __init__(self, host="localhost", port=7000):
        self.clientes = []

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)

        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)

        acepter.daemon = True
        acepter.start()

        procesar.daemon = True
        procesar.start()


def __init__(self, host="localhost", port=7000):
    try:
        while True:
            msg = input('-> ')
            if msg == 'salir':
                break
        self.sock.close()
        sys.exit()

    except:
        self.sock.close()
        sys.exit()


def msg_to_all(self, msg, cliente):
    for c in self.clientes:
        try:
            if c != cliente:
                c.send(msg)
        except:
            self.clientes.remove(c)


def aceptarCon(self):
    print("aceptarCon iniciado")
    while True:
        try:
            conn, addr = self.sock.accept()
            conn.setblocking(False)
            self.clientes.append(conn)
        except:
            pass


def procesarCon(self):
    print("procesarCon iniciado")
    while True:
        if len(self.clientes) > 0:
            for c in self.clientes:
                try:
                    data = c.recv(1024)
                    if data:
                        self.msg_to_all(data, c)
                except:
                    pass
