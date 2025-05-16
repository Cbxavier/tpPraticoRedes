# Nome: Kaique Xavier e Matheus Assis
# tcp_client.py – Cliente TCP para enviar mensagens ao servidor

import socket
import sys

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024

def conectar_servidor(host: str, port: int) -> socket.socket:
    """
    Cria um socket TCP e conecta ao servidor.
    Retorna o socket conectado.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f"[+] Conectado ao servidor em {host}:{port}")
    return sock

def ler_entrada_usuario() -> str:
    """
    Lê uma linha do usuário e retorna a mensagem sem espaços nas extremidades.
    """
    return input("Digite uma mensagem (ou 'sair' para encerrar): ").strip()

def enviar_mensagem(sock: socket.socket, msg: str):
    """
    Envia uma string para o servidor via socket.
    """
    sock.sendall(msg.encode('utf-8'))

def receber_resposta(sock: socket.socket) -> str:
    """
    Aguarda e decodifica a resposta do servidor.
    """
    data = sock.recv(BUFFER_SIZE)
    return data.decode('utf-8')

def main():
    # Tenta conectar ao servidor
    try:
        cliente = conectar_servidor(HOST, PORT)
    except ConnectionRefusedError:
        print(f"[!] Não foi possível conectar ao servidor em {HOST}:{PORT}.")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Erro ao conectar: {e}")
        sys.exit(1)

    # Usa o socket dentro de um contexto para garantir fechamento
    with cliente:
        while True:
            mensagem = ler_entrada_usuario()

            if not mensagem:
                print("[!] Mensagem vazia não permitida.")
                continue

            if mensagem.lower() == 'sair':
                print("[x] Encerrando chat.")
                break

            try:
                enviar_mensagem(cliente, mensagem)
                resposta = receber_resposta(cliente)

                if not resposta:
                    print("[!] O servidor fechou a conexão.")
                    break

                print(f"[Servidor]: {resposta}")

            except Exception as e:
                print(f"[!] Erro na comunicação: {e}")
                break

if __name__ == "__main__":
    main()
