import logging
import logging.config
import yaml

def setup_logging():

    logging_config = """
version: 1

formatters:
    simple:
        format: "%(name)s - %(lineno)d -  %(message)s"

handlers:
    console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: simple

loggers:

    rhino_logging:
        level: DEBUG
        handlers: [console]
        propagate: yes

    __main__:
        level: DEBUG
        handlers: [console]
        propagate: yes

    """

    config = yaml.safe_load(logging_config)
    logging.config.dictConfig(config)
    return logging.getLogger("rhino_logging")
