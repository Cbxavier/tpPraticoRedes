# Nome da dupla: Kaique Xavier e Matheus Assis
# UdpServer.py - Servidor UDP Echo

import socket

HOST = '0.0.0.0'  # Escuta em todas as interfaces de rede
PORT = 6000       # Porta do servidor UDP
BUFFER_SIZE = 65535  # Tamanho máximo de mensagem UDP (64 KB)

def main():
    # Criação do socket UDP (SOCK_DGRAM)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print(f"[+] Servidor UDP escutando na porta {PORT}")

        while True:
            # Recebe dados e o endereço do cliente
            data, addr = server_socket.recvfrom(BUFFER_SIZE)
            mensagem = data.decode()
            print(f"[{addr}] Mensagem recebida: {mensagem}")

            # Envia de volta a mesma mensagem (eco)
            server_socket.sendto(data, addr)

if __name__ == "__main__":
    main()
