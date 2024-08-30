# /workspaces/autenticacion-sotelo/src/generate_key.py

import os

# Generate a random secret key
key = os.urandom(24).hex()
print(f"SECRET_KEY={key}")
