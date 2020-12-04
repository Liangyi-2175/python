from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5001
NAME = 'TestChat'

class ChatSession(async_chat):
    """
    一个负责处理服务器和单个用户间连接的类
    """
    def __init__(self, server, sock):
        #标准的设置任务
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator(b"\r\n")
        self.data = []
        #问候用户
        self.push(b'Welcome to' + self.server.name.encode() +b'\r\n')

    def collect_incoming_data(self, data):
        #从套接字中读取一些文本后调用此方法
        print('in collect_incoming_data')
        self.data.append(data.decode())

    def found_terminator(self):
        """
        如果遇到结束符号，就意味着读取了一整行，因此将这行内容广播给每个人
        :return:
        """
        line = ''.join(self.data)
        self.data = []
        print('in found_terminator')
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)

class ChatServer(dispatcher):
    """
    一个接受连接并创建会话的类，它还负责向这些会话广播
    """
    def __init__(self, port, name):
        super().__init__()
        print(1111)
        #标准的设置任务：
        self.create_socket()
        print(2222)
        self.set_reuse_addr()
        print(3333)
        self.bind(('', port))
        print(4444)
        self.listen(5)
        self.name = name
        self.sessions = []

    def disconnect(self, session):
        """
        删除会话列表中的会话
        :param session:
        :return:
        """
        self.sessions.remove(session)
        print(3333)

    def broadcast(self, line):
        """
        给聊天室中所有用户推送消息
        :param line:
        :return:
        """
        for session in self.sessions:
            session.push(line.encode() +b'hello'+ b'\r\n')

    def handle_accept(self):

        conn, addr =self.accept()
        self.sessions.append(ChatSession(self, conn))


if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print()