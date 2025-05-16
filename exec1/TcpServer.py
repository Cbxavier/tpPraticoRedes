# Nome da dupla: Kaique Xavier e Matheus Assis
# TcpServer.py - Servidor TCP que aceita múltiplos clientes

import socket
import threading

# Configurações do servidor para rodar na porta específica, nesse caso, 5000
HOST = '0.0.0.0'  
PORT = 5000       

# Função que será executada em uma thread separada para cada cliente que se conectar
# Parâmetros:
#   conn -> objeto de conexão com o cliente (socket)
#   addr -> tupla contendo o IP e a porta do cliente
def handle_client(conn, addr):
    print(f"[+] Conexão estabelecida com {addr}") 
    try:
        while True:
            # Recebe até 1024 bytes do cliente e decodifica de bytes para string
            data = conn.recv(1024).decode()
            if not data:
                break  # Se não receber dados, assume que o cliente encerrou a conexão
            print(f"[{addr}] Mensagem recebida: {data}") 
            conn.sendall("Mensagem recebida".encode())   
    except Exception as e:

        print(f"[!] Erro com {addr}: {e}")
    finally:
        # Fecha a conexão com o cliente de forma segura
        conn.close()
        print(f"[-] Conexão encerrada com {addr}")

# Função principal que inicializa o servidor e aceita conexões de clientes
def main():
    # Cria um socket TCP (AF_INET para IPv4, SOCK_STREAM para TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
       
        server_socket.bind((HOST, PORT))
    
        server_socket.listen()
        print(f"[+] Servidor TCP escutando na porta {PORT}")

        # Laço infinito para aceitar e tratar conexões de clientes
        while True:
            
            conn, addr = server_socket.accept()
           
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()  

if __name__ == "__main__":
    main()
