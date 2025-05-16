# Nome: Kaique Xavier e Matheus Assis
# ChatClient.py - Cliente TCP para chat em tempo real

import socket
import threading

HOST = '127.0.0.1'
PORT = 7000

# Função para receber mensagens do servidor
def receber_mensagens(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

# Função principal do cliente
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((HOST, PORT))
            print("[+] Conectado ao servidor de chat.")
            
            # Inicia thread para receber mensagens
            threading.Thread(target=receber_mensagens, args=(client_socket,), daemon=True).start()

            # Envia mensagens até digitar "sair"
            while True:
                msg = input()
                if msg.strip().lower() == 'sair':
                    client_socket.sendall(msg.encode())
                    break
                if not msg:
                    continue
                client_socket.sendall(msg.encode())

        except Exception as e:
            print(f"[!] Erro: {e}")

if __name__ == "__main__":
    main()
