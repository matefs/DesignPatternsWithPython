import logging

class LoggerSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.logger = logging.getLogger("Singleton logger")
            cls._instance.logger.setLevel(logging.DEBUG)

            # Criando handler e formatter corretamente
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            
            cls._instance.logger.addHandler(handler)
        return cls._instance

logger = LoggerSingleton().logger
logger.info('Teste')
logger.warning('teste warning')
