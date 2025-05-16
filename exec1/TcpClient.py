# Nome: Kaique Xavier e Matheus Assis
# TcpClient.py - Cliente TCP que vai se conectar ao servidor e enviar as mensagens

import socket 

# Define o endereço IP e a porta do servidor
HOST = '127.0.0.1'  
PORT = 5000         

# Função principal do cliente, responsável por contectar ao servidor e enviar mensagens
def main():
    # Cria um socket TCP (AF_INET para IPv4, SOCK_STREAM para protocolo TCP)
   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
           
            client_socket.connect((HOST, PORT))
            print("[+] Conectado ao servidor.")

            # Loop principal de envio de mensagens
            while True:
                msg = input("Digite uma mensagem (ou 'sair' para encerrar): ").strip()

                if msg.lower() == 'sair':
                    break

                if not msg:
                    print("[!] Mensagem vazia não permitida.")
                    continue

                client_socket.sendall(msg.encode())

                resposta = client_socket.recv(1024).decode()
                print(f"[Servidor]: {resposta}")

        except ConnectionRefusedError:
            print("[!] Não foi possível conectar ao servidor.")

        except Exception as e:
            print(f"[!] Erro: {e}")

if __name__ == "__main__":
    main()
