# Nome da dupla: Kaique Xavier e Matheus Assis
# TimeServer.py - Servidor TCP que fornece a hora atual para múltiplos clientes

import socket
import threading
from datetime import datetime

HOST = '0.0.0.0'
PORT = 8000  # Porta do servidor de hora

# Função para lidar com cada cliente individualmente
def handle_client(conn, addr):
    print(f"[+] Conexão recebida de {addr}")
    try:
        # Obtém a hora atual no formato HH:MM:SS
        hora_atual = datetime.now().strftime("%H:%M:%S")
        conn.sendall(hora_atual.encode())
        print(f"[{addr}] Hora enviada: {hora_atual}")
    except Exception as e:
        print(f"[!] Erro ao atender {addr}: {e}")
    finally:
        conn.close()
        print(f"[-] Conexão encerrada com {addr}")

# Função principal do servidor
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[+] Servidor de hora escutando na porta {PORT}")

        while True:
            try:
                conn, addr = server_socket.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()
            except KeyboardInterrupt:
                print("\n[!] Servidor encerrado manualmente.")
                break
            except Exception as e:
                print(f"[!] Erro geral: {e}")

if __name__ == "__main__":
    main()
