import json
import os

DEFAULT_CONFIG = {
    "html_file": "logs.html",
    "level": "DEBUG",
    "max_records": 1000,
    "template": None
}

class Config:
### ==========================================================================
###    Управление конфигурацией htmllogs.
###    Пример:
###        config = Config('config.json')
###        html_file = config.html_file
### ==========================================================================
    
    def __init__(self, config_file=None):
### ==========================================================================
###        Args:
###            config_file (str, optional): Путь к JSON-файлу с настройками.
### ==========================================================================
        self._config = DEFAULT_CONFIG.copy()
        if config_file and os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                user_config = json.load(f)
                self._config.update(user_config)
    
    def get(self, key, default=None):
        return self._config.get(key, default)
    
    def set(self, key, value):
        self._config[key] = value
    
    @property
    def html_file(self):
        return self._config['html_file']
    
    @property
    def level(self):
        return self._config['level']
    
    @property
    def max_records(self):
        return self._config['max_records']
    
    @property
    def template(self):
        return self._config.get('template')