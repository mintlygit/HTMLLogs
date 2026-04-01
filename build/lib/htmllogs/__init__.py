import logging
from .handler import htmllogsHandler
from .config import Config

__version__ = "0.1.0"

def setup(html_file='logs.html', level=logging.DEBUG, max_records=1000):
### ======================================================================
###    Настраивает логирование с использованием htmllogsHandler. 
###    Args:
###      html_file (str): Путь к HTML-файлу для вывода логов.
###        level (int): Уровень логирования (logging.DEBUG, INFO, WARNING, ERROR).
###        max_records (int): Максимальное количество записей для хранения.
###    Returns:
###        htmllogsHandler: Установленный обработчик.
### ======================================================================
    handler = htmllogsHandler(html_file, max_records)
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(level)
    return handler

def setup_from_config(config_file=None, **overrides):
### ======================================================================
###    Настраивает логирование, используя конфигурацию из файла.  
###    Args:
###        config_file (str): Путь к JSON-файлу конфигурации.
###        **overrides: Параметры, переопределяющие настройки из файла.
###            Возможные ключи: html_file, level, max_records.
###    Returns:
###        htmllogsHandler: Установленный обработчик.
### ======================================================================
    cfg = Config(config_file)
    html_file = overrides.get('html_file', cfg.html_file)
    level_name = overrides.get('level', cfg.level)
    max_records = overrides.get('max_records', cfg.max_records)
    
    # Преобразуем строку уровня в константу logging
    level = getattr(logging, level_name.upper(), logging.DEBUG)
    
    return setup(html_file, level, max_records)