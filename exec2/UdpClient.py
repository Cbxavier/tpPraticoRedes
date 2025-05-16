# Nome: Kaique
# UdpClient.py - Cliente UDP Echo

import socket

HOST = '127.0.0.1'  # IP do servidor
PORT = 6000         # Porta do servidor UDP
BUFFER_SIZE = 65535  # Tamanho máximo permitido no UDP

def main():
    # Criação do socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        # Define timeout para aguardar resposta (2 segundos)
        client_socket.settimeout(2.0)

        while True:
            msg = input("Digite uma mensagem (ou 'sair' para encerrar): ").strip()

            if msg.lower() == 'sair':
                print("Encerrando conexão.")
                break

            if not msg:
                print("[!] Mensagem vazia não é permitida.")
                continue

            if len(msg.encode()) > BUFFER_SIZE:
                print(f"[!] A mensagem excede o tamanho máximo de {BUFFER_SIZE} bytes.")
                continue

            # Envia a mensagem para o servidor
            client_socket.sendto(msg.encode(), (HOST, PORT))

            try:
                # Aguarda a resposta do servidor
                data, _ = client_socket.recvfrom(BUFFER_SIZE)
                print(f"[Servidor]: {data.decode()}")

            except socket.timeout:
                print("[!] Tempo de resposta excedido. O servidor pode não ter respondido.")
            except Exception as e:
                print(f"[!] Erro na comunicação: {e}")

if __name__ == "__main__":
    main()
