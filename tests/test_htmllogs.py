import logging
import lognice
import os
import time

def test_lognice():
    logfile = 'test_logs.html'
    lognice.setup(logfile, level=logging.DEBUG, max_records=10)
    
    logging.info("Test info")
    logging.error("Test error")
    time.sleep(0.1)  #Выдача времени на запись!
    
    assert os.path.exists(logfile)
    with open(logfile, 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'Test info' in content
        assert 'Test error' in content
    
#Очистка
    os.remove(logfile)

if __name__ == '__main__':
    test_lognice()
    print("Test passed")