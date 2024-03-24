import socket

#site ip adress bulma.
def whatip():
    print("url girin:")
    url=input()
    ip = socket.gethostbyname(url)
    print(ip)

#Tek portu tarama.
def scanoneport():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("İP adresini giriniz:")
    ip=input()
    print("taramak istedeğiniz portu giriniz:")
    port=int(input())
    try:
        server_socket.connect((ip, port))
        print(port,"açık")
    except(socket.timeout, socket.error):
        print(port,"kapalı")
    finally:
        print("İşlem tamamlandı.")

#Birden çok portu tarama.
def scanmultiport():
    print("İP adresini giriniz:")
    ip=input()
    print("taramak istedeğiniz port_a giriniz:")
    port_a=int(input())
    print("taramak istedeğiniz port_a giriniz:")
    port_b=int(input())


    for port in range(port_a,port_b+1):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.settimeout(1)
        try:
            server_socket.connect((ip,port))
            print(port,"açık")
        except(socket.timeout, socket.error):
            print(port,"kapalı")
        finally:
            server_socket.close()
            print("İşlem tamamlandı.")


#Tek portu dinleme.
def listenoneport():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("İP adresini giriniz:")
    ip=input()
    print("taramak dinlemek portu giriniz:")
    port=int(input())
    try:
        server_socket.bind((ip, port))
        print("portuna bağlanıldı".format(port))

        server_socket.listen(10)
        print(" dinleniyor")

    except(socket.timeout, socket.error):
        print(port,"kapalı")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Gelen bağlantı: {client_address}")

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Gelen veri: {data}")

        client_socket.close()


def menu():

    print("ne yapmak istersniz")
    print("1. ip bulma")
    print("2. tek port tarama")
    print("3. birden çok port tarama")
    print("4.bir port dinleme(denyesel)")

    istek=int(input())

    if istek == 1:
        whatip()

    elif istek == 2:
        scanoneport()

    elif istek == 3:
        scanmultiport()

    elif istek == 4:
        listenoneport()

    else:
        print("lütfen geçeri bir şıkı seçiniz")


if __name__ == "__main__":
    menu()
