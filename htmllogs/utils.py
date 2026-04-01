import json
import logging
import html
import re

def escape_html(text):
    return html.escape(str(text))

def is_json(text):
    if not isinstance(text, str):
        return False
    text = text.strip()
    if (text.startswith('{') and text.endswith('}')) or (text.startswith('[') and text.endswith(']')):
        try:
            json.loads(text)
            return True
        except:
            pass
    return False

def format_record(record):
    time_str = record.asctime if hasattr(record, 'asctime') else record.created
    if isinstance(time_str, float):
        from datetime import datetime
        time_str = datetime.fromtimestamp(time_str).isoformat()
    
    return {
        'time': time_str,
        'level': record.levelname,
        'logger': record.name,
        'message': record.getMessage(),
        'module': record.module,
        'lineno': record.lineno,
        'funcName': record.funcName,
#можно добавить другие поля
    }