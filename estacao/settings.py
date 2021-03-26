# False para Desenvolvimento
PRODUCTION=True

if PRODUCTION:
    DB_PATH='/estacao/estacao.db'
else:
    DB_PATH='estacao.db'

PREFIX_API_VERSION = '/api/v1'
API_PORT = 5000                         # Se alterar a Porta da API aqui, deve-se alterar no arquivo uwsgi.ini também.
API_DEBUG = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH

LOGGING_CONF = 'logging.ini'

SERVICE_MESSAGE = True
SERVICE_NOTIFICATION = True

# Altere para informações do Servidor de Fila de Mensagens (Broker)
# Projeto utiliza o broker do RabbitMQ
RABBIT_SERVER = {
    'HOST' : 'broker.example.com',       # Ou IP do servidor.
    'PORT' : 5672,                       # Porta para conexão, padrão do RabbitMQ é 5672.
    'USER' : 'User',                     # Usuário do servidor de mensagens.
    'PASS' : 'Pass'                      # Senha do Usuário informando.
}
EXCHANGE_NOTIFICATIONS='notifications'   # Exchange do Servidor RabbitMQ para envio das notificações.






