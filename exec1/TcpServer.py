# Nome: Kaique Xavier e Matheus Assis
# tcp_server.py – Servidor TCP que aceita múltiplos clientes e responde confirmação

import socket
import threading
import sys
from typing import Tuple

# Configurações do servidor
HOST = '0.0.0.0'
PORT = 5000
BUFFER_SIZE = 1024

def inicializar_servidor(host: str, port: int) -> socket.socket:
    """
    Cria, configura e retorna um socket TCP escutando em (host, port).
    """
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_sock.bind((host, port))
    srv_sock.listen()
    print(f"[+] Servidor TCP ativo em {host}:{port}")
    return srv_sock

def aceitar_conexoes(server_sock: socket.socket):
    """
    Loop que aceita conexões de clientes e dispara uma thread para cada um.
    """
    try:
        while True:
            conn, addr = server_sock.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print("\n[!] Interrupção pelo usuário. Finalizando servidor...")
    finally:
        server_sock.close()
        sys.exit(0)

def handle_client(conn: socket.socket, addr: Tuple[str, int]):
    """
    Lida com a comunicação de um cliente em thread separada.
    Recebe mensagens e envia confirmação de volta.
    """
    print(f"[+] Conexão iniciada com {addr}")
    with conn:
        try:
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break  # cliente desconectou
                mensagem = data.decode('utf-8').strip()
                print(f"[{addr}] -> {mensagem}")
                resposta = "Mensagem recebida"
                conn.sendall(resposta.encode('utf-8'))
        except Exception as e:
            print(f"[!] Erro na conexão com {addr}: {e}")
        finally:
            print(f"[-] Conexão encerrada com {addr}")

def main():
    server_socket = inicializar_servidor(HOST, PORT)
    aceitar_conexoes(server_socket)

if __name__ == "__main__":
    main()
