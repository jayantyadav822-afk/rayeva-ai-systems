# Settings for environment configuration management

import os

class Settings:
    @staticmethod
    def get(key, default=None):
        return os.getenv(key, default)

    @staticmethod
    def load_from_env_file(file_path):
        with open(file_path) as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

# Load environment variables from .env file
# Settings.load_from_env_file('.env')
