from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# Defina o caminho para o diretório de dados
ftp_dir = os.path.join(os.getcwd(), 'ftp_data')
if not os.path.exists(ftp_dir):
    os.makedirs(ftp_dir)

# Configura as credenciais de acesso
authorizer = DummyAuthorizer()
authorizer.add_user("user2", "12345", ftp_dir, perm="elradfmw")
authorizer.add_anonymous(ftp_dir, perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

# Inicia o servidor na porta 2121
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
