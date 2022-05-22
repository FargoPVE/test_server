import telnetlib

HOST = '127.0.0.1'
with telnetlib.Telnet(HOST, port=8888, timeout=5) as tn:
    command = input("Введите данные: ") + '\r\n'
    tn.write(command.encode('utf-8'))
    ret1 = tn.read_eager()
    print(tn.read_all().decode('utf-8'))
