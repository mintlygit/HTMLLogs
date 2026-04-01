import logging
import json
import os
import pkg_resources
from . import utils

class htmllogsHandler(logging.Handler):
    
    def __init__(self, filename='logs.html', max_records=1000):
        super().__init__()
        self.filename = filename
        self.max_records = max_records
        self.records = []
        self._load_existing()
    
    def emit(self, record):
        formatted = utils.format_record(record)
        self.records.append(formatted)
        if len(self.records) > self.max_records:
            self.records = self.records[-self.max_records:]
        self._render_html()
    
    def _render_html(self):
        template_path = pkg_resources.resource_filename(__name__, 'templates/log_template.html')
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template = f.read()
        except FileNotFoundError:
            import os
            base_dir = os.path.dirname(os.path.abspath(__file__))
            template_path = os.path.join(base_dir, 'templates', 'log_template.html')
            with open(template_path, 'r', encoding='utf-8') as f:
                template = f.read()
        
        logs_json = json.dumps(self.records, ensure_ascii=False, indent=2)
        html = template.replace('{{ logs_data }}', logs_json)
        
        os.makedirs(os.path.dirname(self.filename) or '.', exist_ok=True)
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(html)
    
    def _load_existing(self):
        pass