# Nome da dupla: Kaique Xavier e Matheus Assis
# Servidor UDP - Echo Server

import socket

# Configurações do servidor
HOST = '0.0.0.0'        # Escuta em todas as interfaces de rede
PORT = 6000             # Porta para escutar conexões
BUFFER_SIZE = 65535     # Tamanho máximo do pacote UDP

def main():
    """Inicia o servidor UDP que escuta mensagens e devolve (echo) para o cliente."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_servidor:
        socket_servidor.bind((HOST, PORT))
        print(f"[+] Servidor UDP escutando em {HOST}:{PORT}")

        while True:
            # Recebe dados do cliente e o endereço de origem
            dados, endereco = socket_servidor.recvfrom(BUFFER_SIZE)
            mensagem = dados.decode()
            print(f"[{endereco}] Mensagem recebida: {mensagem}")

            # Envia de volta a mesma mensagem (echo)
            socket_servidor.sendto(dados, endereco)

if __name__ == "__main__":
    main()
