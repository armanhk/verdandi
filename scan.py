import socket
import re
import time

def get_data(ip, port):
    result = ''

    s = socket.socket()
    s.connect((ip, port))

    s.send('GET / HTTP/1.1\r\nHost:localhost\r\n\r\n'.encode())
    response = ''
    
    while True:
        data = s.recv(1024)
        if not data:
            break
        else:
            response += data.decode('utf-8')
        
    p = re.compile('H.*\r\n.*\r\n.*\r\n.*\r\n.*\r\n\r\n')
    result = p.sub('', response)
    time.sleep(1)
    s.close()

    return result

def do_sum_mafs(result, operator, r_val):
    if operator == 'add':
        return result + r_val
    elif operator == 'subtract':
        return result - r_val
    elif operator == 'multiply':
        return result * r_val
    elif operator == 'divide':
        return result / r_val

if __name__ == "__main__":
    result = 0
    target_ip = input('Enter target ip: ')
    terminus = 9675
    port = 1337

    while (port != terminus):
        try:
            print(port)
            s = get_data(target_ip, port).strip()
            payload = s.split(' ')
            result = do_sum_mafs(result, payload[0], int(payload[1]))
            port = int(payload[2])
        except:
            continue

    s = get_data(target_ip, terminus).strip()
    payload = s.split(' ')
    result = do_sum_mafs(result, payload[0], int(payload[1]))
    print(result)