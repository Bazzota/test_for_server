import sys

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_1': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'handler_stderr': {
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_1'
        },
        'handler_stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_1',
            'stream': sys.stdout
        }
    },
    'loggers': {},
    'root': {
        'level': 'INFO',
        'formatter': 'default',
        'handlers': ['default']
    }
}