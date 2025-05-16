# Nome da dupla: Kaique Xavier e Matheus Assis
# Cliente UDP - Envia mensagens para servidor e recebe resposta (echo)

import socket

# Configurações do cliente
HOST = '127.0.0.1'       # Endereço IP do servidor (localhost)
PORT = 6000              # Porta do servidor UDP
BUFFER_SIZE = 65535      # Tamanho máximo de pacote UDP


def isValidMessage(mensagem):
    return mensagem != '' and len(mensagem.encode()) <= BUFFER_SIZE

def sendMessage(mensagem, sock):
    sock.sendto(mensagem.encode(), (HOST, PORT))

def loggout():
    print('Encerrando conexão UDP')

def main():
    """Inicia o cliente UDP que envia mensagens ao servidor e exibe respostas."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_cliente:
        socket_cliente.settimeout(2.0)  # Define timeout de 2 segundos

        while True:
            mensagem = input("Digite uma mensagem (ou 'sair' para encerrar): ").strip()
            if mensagem.lower() == 'sair':
                loggout()
                break  

            if isValidMessage(mensagem):
                sendMessage(mensagem, socket_cliente)

                try:
                    # Aguarda a resposta do servidor (eco)
                    resposta, _ = socket_cliente.recvfrom(BUFFER_SIZE)
                    print(f"[Servidor]: {resposta.decode()}")

                except socket.timeout:
                    print("[!] Tempo de resposta excedido. Sem resposta do servidor.")
                except Exception as erro:
                    print(f"[!] Erro na comunicação: {erro}")
                    
            print("[!] Mensagem inválida. Verifique se está vazia ou excede o tamanho permitido.")

if __name__ == "__main__":
    main()
