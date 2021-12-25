from display import RossumDisplay

import socket

from configuration import I2C_PINS, DISPLAY_RESOLUTION


def parse_url_parameter(content, parameter):
    try:
        text = content.split("\r\n")[0].split("GET")[-1].split("HTTP")[0].split("{}=".format(parameter))[-1].strip()
    except IndexError:
        return None
    return text.replace("+", " ")


def process_request(connection):
    content = str(conn.recv(1024))
    text = parse_url_parameter(content, "text")
    print(text)
    display.show_text(text, y=20)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: application/json\n')
    conn.send('Connection: close\n\n')
    conn.send('{"status": "ok"}')
    conn.close()


if __name__ == "__main__":
    display = RossumDisplay(I2C_PINS["sda"], I2C_PINS["scl"], DISPLAY_RESOLUTION)
    display.show_text("running")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        process_request(conn)
