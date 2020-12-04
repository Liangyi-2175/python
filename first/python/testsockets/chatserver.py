import re
from asyncore import dispatcher
from asynchat import async_chat
import asyncore
PORT = 5006
NAME = 'TestChat'


class EndSession(Exception):
    pass

class CommandHandler:
    """
    类似于标准库中cmd.Cmd的简单命令
    """
    def unknown(self, session, cmd):
        '响应未知命令'
        session.push(b'Unknown command:'+cmd.encode()+b'\r\n')

    def handle(self, session, line):
        '处理从指定会话收到的行'
        #strip() 去除首尾空格
        if not line.strip():
            return
        if not self.is_space(line):
            session.push(b'Please enter \r\n')
            return
        parts = line.split(' ', 1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
            # print(f'line:{line}')
        except IndentationError:
            line = ''
        #尝试查找处理程序
        meth = getattr(self, 'do_' + cmd, None)
        print(f'meth is {meth}')
        try:
            #假设它是可以调用的：
            meth(session,line)
        except TypeError:
            #假如是不可以调用的，就响应未知命令
            self.unknown(session, cmd)

    def is_space(self,line):
        """判断是否包含空格"""
        if re.search(r"\s", line):
            print('t')
            return True
        else:
            print('f')
            return False
class Room(CommandHandler):
    """
    可能包含一个或多个用户(会话)的通用环境，它负责基本的命令处理和广播
    """
    def __init__(self, server):
        self.server = server
        self.sessions = []

    def add(self, session):
        '有会话(用户)进入聊天室'
        self.sessions.append(session)

    def remove(self, session):
        '有会话(用户)离开聊天室'
        self.sessions.remove(session)

    def broadcast(self,line):
        '将一行内容发送给聊天室内的所有会话(用户)'
        for session in self.sessions:
            session.push(line.encode())

    def do_logout(self, session, line):
        '响应命令logout'
        raise EndSession


class LoginRoom(Room):
    """
    为刚连接的用户准备聊天室
    """
    def add(self, session):
        Room.add(self,session)
        #用户进入时，向他/她发出问候：
        self.broadcast('Welcome to'+ self.server.name +'\r\n')

    def unknown(self, session, cmd):
        #除login和logout外的所有命令都会导致系统显示提示消息：
        session.push(b'Please enter a name\r\n')

    def do_login(self, session, line):
        name = line.strip()
        #确保用户输入了用户名：
        if not name:
            session.push(b'Please enter a name\r\n')
        # 确保用户名未被占用：
        elif name in self.server.users:
            session.push(b'The name' +name.encode()+ b'is taken.\r\n')
            session.push(b'Please try again.\r\n')
        else:
            #用户名没有问题，因此将储存到会话中并将用户移到主聊天室
            session.name = name
            session.enter(self.server.main_room)


class ChatRoom(Room):
    """
    为多个用户相互聊天准备的聊天室
    """
    def add(self, session):
        #告诉所有人有新用户进入：
        self.broadcast(session.name + ' has entered the room.\r\n')
        self.server.users[session.name] = session
        Room.add(self, session)

    def remove(self, session):
        Room.remove(self, session)
        #告诉所有人有用户离开：
        self.broadcast(session.name + 'has left the room.\r\n')

    def do_say(self, session, line):
        self.broadcast(session.name+ ':' + line + '\r\n')

    def do_look(self, session , line):
        """
        处理命令look，这个命令用户查看聊天室里面都有谁
        """
        session.push(b'The following are logged in : \r\n')
        for other in self.sessions:
            session.push(other.name.encode() + b'\r\n')

    def do_who(self, session, line):
        """
        处理命令who，这个命令用户查看谁已经登陆
        """
        session.push(b'The following are logged in : \r\n')
        for name in self.server.users:
            session.push(name.encode()+b'\r\n')


class LogoutRoom(Room):
    """
    为单个用户准备聊天室，仅用于将用户从服务器中删除
    """
    def add(self, session):
        try:
            # print(f'users len is:{len(self.server.users)}')
            del self.server.users[session.name]
        except KeyError:
            pass


class ChatSession(async_chat):
    """
    单个会话，负责与单个用户通讯
    """
    def __init__(self, server, sock):
        super(ChatSession, self).__init__(sock)
        # super().__init__(sock)
        # async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator(b"\r\n")
        self.data = []
        self.name = None
        #所有会话最初都位于loginRoom中:
        self.enter(LoginRoom(server))

    def enter(self, room):
        #自己从当前聊天室离开，并进入下一个聊天室
        try:
            cur = self.room
            # for x in cur:
            #     print(f'cur{x}')
        except AttributeError: pass
        else: cur.remove(self)
        self.room = room
        room.add(self)

    def collect_incoming_data(self, data):
        """
        从套接字中读取一些文本后调用此方法
        :param data:
        :return:
        """

        self.data.append(data.decode())
        # print(f'data is {self.data}')

    def found_terminator(self):
        """
        在文本中读取到结束符时调用此方法，这里结束符为换行符
        :return:
        """
        line = ''.join(self.data)
        # print(f'found_terminator line is: {line}')
        self.data = []
        try:
            self.room.handle(self, line)
        except EndSession:
            self.handle_close()

    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))


class ChatServer(dispatcher):
        """
        只有一个聊天室的聊天服务器
        """
        def __init__(self, port, name):
            super().__init__()
            self.create_socket()
            self.set_reuse_addr()
            self.bind(('', port))
            self.listen(5)
            self.name = name
            self.users = {}
            self.main_room = ChatRoom(self)

        def handle_accept(self):
            # 客户端套接字 conn
            conn, addr = self.accept()
            ChatSession(self, conn)


if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print()