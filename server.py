import socketserver
import re


class EchoTCPServer(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip().decode('utf-8')
        try:
            data = re.split(r'[:. ]', data.replace('[CR]', ''))
            time = ':'.join(data[2:5])
            if int(data[0][0:2]) == 00:
                r = f'спортсмен, нагрудный номер {data[0]} прошел отсечку {data[1]} в {time}.{data[5][0]}'
                print(r)
                self.request.sendall(r.encode('utf-8'))
                with open('file_log.txt', 'a') as file:
                    file.write(r + '\n')
                    file.close()

            else:
                f = f'спортсмен, нагрудный номер {data[0]} прошел отсечку {data[1]} в {time}.{data[5]}'
                with open('file_log.txt', 'a') as file:
                    file.write(f + '\n')
                    file.close()
        except AttributeError:
            print('Неподходящий формат данных')


if __name__ == '__main__':
    with socketserver.TCPServer(('', 8888), EchoTCPServer) as server:
        server.serve_forever()
