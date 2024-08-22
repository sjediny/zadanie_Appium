import json
import os
from cryptography.fernet import Fernet

class Config:
    def __init__(self, config_file='config.json', key_file='secret.key'):
        self.config_file = config_file
        self.config_path = os.path.join(os.path.dirname(__file__), '../../', self.config_file)
        self.key_file = key_file
        self.key_path = os.path.join(os.path.dirname(__file__), '../../', self.key_file)
        self.config = self.load_config()
        self.name = self.config['name']
        self.email = self.config['email']
        self.password = self.decrypt_password(self.config['password'])

    def load_config(self):
        with open(self.config_path, 'r') as config_file:
            return json.load(config_file)

    def decrypt_password(self, encrypted_password):
        with open(self.key_path, 'rb') as key_file:
            key = key_file.read()
        cipher_suite = Fernet(key)
        return cipher_suite.decrypt(encrypted_password.encode('utf-8')).decode('utf-8')