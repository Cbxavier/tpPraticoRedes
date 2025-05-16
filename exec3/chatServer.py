# Nome da dupla: Kaique Xavier e Matheus Assis
# ChatServer.py - Servidor TCP para chat entre dois clientes

import socket
import threading

HOST = '0.0.0.0'
PORT = 7000

clients = []

# Função que repassa a mensagem de um cliente para o outro
def handle_client(conn, addr):
    print(f"[+] Cliente conectado: {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break  # cliente desconectou
            mensagem = data.decode()

            # Se for a palavra de saída, desconecta
            if mensagem.lower() == 'sair':
                print(f"[-] {addr} saiu do chat.")
                break

            # Envia a mensagem para o outro cliente
            for c in clients:
                if c != conn:
                    c.sendall(f"[{addr[0]}]: {mensagem}".encode())

        except:
            break

    # Remove o cliente e fecha a conexão
    clients.remove(conn)
    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(2)
        print(f"[+] Servidor de chat TCP escutando na porta {PORT}")

        while len(clients) < 2:
            conn, addr = server_socket.accept()
            clients.append(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

        print("[*] Dois clientes conectados. Chat iniciado.")

if __name__ == "__main__":
    main()
