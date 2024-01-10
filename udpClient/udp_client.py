import socket
import time
while True:
    print("\nElija una opción")
    print("-------------------------")
    print("1. Presione cualquier tecla para iniciar")
    print("2. Presione 0 para salir")
    print("-------------------------\n")

    option = input("Opcion: ")
    if option == 0:
        break
    print("-------------------------")
    print("Sending message...")
    print("-------------------------\n")
    msg = "wiiiiiiiiiiiiiiiiiii"

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Crea un socket UDP para el cliente
    server_address = ('10.0.0.4', 4000)  # Direccion ip y puerto del servidor
   # mysocket.settimeout(2)  # El timeout ocurrira en 2 segundos

    try:
        mysocket.sendto(msg.encode("utf-8"), server_address)
        print("Message sent!!")
        # for i in range(0, 9):
        #     start = time.time()  # Momento en que se envia el mensaje
        #     message = 'Ping ' + str(i) + " " + time.ctime(start)
        #     try:
        #         sent = mysocket.sendto(message.encode("utf-8"), server_address)
        #         print("Sent " + message)
        #         data, server = mysocket.recvfrom(4096)  # Maxima cantidad de bytes recibidos 4096
        #         print("Received " + str(data))
        #         end = time.time();
        #         elapsed = end - start # RTT
        #         print("Time: " + str(elapsed * 1000) + " Milliseconds\n")
        #     except socket.timeout:
        #         print("#" + str(i) + " Requested Time out\n")
    finally:
        print("Finishing, closing socket")
        mysocket.close()
