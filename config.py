# config.py
# Megatool 
# Dev: Ricardo J. Salomão 30/09/2024 v1.0

# config.py
TOKEN_BD = 'Rjs@8073#Rjs@8073'
DEBUG_MODE = True  # Altere para True / False se não desejar logs de depuração
LOG_LEVEL = 'DEBUG' if DEBUG_MODE else 'INFO'
LOG_FILE = '/app/igo/middleware.log'

DATABASE_CONFIG = {
    'dsn': 'postgresql://megatool:megatool@localhost:5432/megatool'
}
