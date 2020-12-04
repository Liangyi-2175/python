from asyncore import dispatcher
import asyncore
import socket


class ChatServer(dispatcher):

    def handle_accept(self):
        conn, addr = self.accept()
        print(f'Connection attempt from addr[0]:{addr[0]}\n conn:{conn}')

    def handle_close(self):
        self.close()
        print('ssssssssssss')

if __name__ == '__main__':
    s = ChatServer()
    s.create_socket()
    # s.bind(('10.10.140.230', 5005))
    s.bind(('127.0.0.1', 5007))
    s.listen(5)
    asyncore.loop()