from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore
PORT = 5002


class ChatSession(async_chat):
    def __init__(self, sock):
        async_chat.__init__(self, sock)
        self.set_terminator(b"\r\n")
        self.data = []

    def collect_incoming_data(self, data):
        """
        从套接字中读取一些文本后调用此方法
        :param data:
        :return:
        """
        print(' reading text')
        self.data.append(data.decode('utf-8'))

    def found_terminator(self):
        line = ''.join(self.data)
        print('end message')
        self.data = []
        #使用line做些事情
        print(line)


class ChatServer(dispatcher):
    def __init__(self, port):
        dispatcher.__init__(self)
        print(111111)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        print(222222)
        self.set_reuse_addr()
        print(333333)
        self.bind(('',port))
        print(444444)
        self.listen(5)
        print(555555)
        self.sessions = []

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(conn))
        print('Welcome')


if __name__ == r'__main__':
    s = ChatServer(PORT)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print('9999')