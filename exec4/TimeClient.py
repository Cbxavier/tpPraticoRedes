# Nome da dupla: Kaique Xavier e Matheus Assis
# TimeClient.py - Cliente TCP que solicita a hora atual ao servidor

import socket

HOST = '127.0.0.1'
PORT = 8000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((HOST, PORT))
            print("[+] Conectado ao servidor de hora.")

            # Aguarda a resposta do servidor
            hora = client_socket.recv(1024).decode()
            print(f"[Servidor]: Hora atual: {hora}")

        except ConnectionRefusedError:
            print("[!] Não foi possível conectar ao servidor.")
        except Exception as e:
            print(f"[!] Erro: {e}")

if __name__ == "__main__":
    main()
