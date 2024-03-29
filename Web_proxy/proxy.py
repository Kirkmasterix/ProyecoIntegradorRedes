from socket import *
import sys
import traceback

# if len(sys.argv) <= 1:
#     print ('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
#     sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(("10.0.0.2", 8000))
tcpSerSock.listen(1)

while True:
    # Start receiving data from the client
    print('\n\nReady to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(2048).decode()
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(message)

# Extract the filename from the given message
    #print(message.split()[1])
    #filename = message.split()[1].partition("/")[2]
    filename = message.split()[1].split("/")[1]
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "rb")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())
        tcpCliSock.send("\r\n".encode())
        for line in outputdata:
            tcpCliSock.send(line + "\r\n".encode())
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = message.split()[1].split("/")[0].split(":")[0]
            print(hostn)
            try:
                # Connect to the socket to port 3000
                c.connect((hostn, 3000))
                # Create a temporary file on this socket and ask port 3000 for the file requested by the client
                fileobj = c.makefile('rwb', 0)
                fileobj.write("GET ".encode()+"http://".encode() + filename.encode() + " HTTP/1.0\n\n".encode())
                # Read the response into buffer
                data = fileobj.read()
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename,"wb")
                tmpFile.write(data)
                tcpCliSock.send(data)
            except Exception as e:
                print("Illegal request")
                traceback.print_exc()
                print('Exception: ', e)
        else:
            # HTTP response message for file not found
            print("NET ERROR")
    # Close the client and the server sockets
    tcpCliSock.close()
tcpSerSock.close()
