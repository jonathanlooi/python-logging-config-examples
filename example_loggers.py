"""
Example of using logging.basicConfig to log with ISO 8601 compliant timestamps.
"""

import logging
from pythonjsonlogger import jsonlogger
import time
import datetime


def create_utc_logger(logger_name: str, file_name: str) -> logging.Logger:
    """
    :param logger_name: name of the logger
    :param file_name: name of the log file to append to
    :return: Logger object
    """

    logging.Formatter.converter = time.gmtime  # set to UTC
    logging.basicConfig(
        level=logging.INFO,
        filename=file_name,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",  # ISO 8601 compliant
    )
    return logging.getLogger(name=logger_name)


def create_json_logger(logger_name: str, file_name: str) -> logging.Logger:
    """
    Technically the log file created here is a jsonl file rather than json since it is new line delineated.
    This is also in UTC with ISO 8601 formatted timestamps.

    :param logger_name: name of the logger
    :param file_name: name of the log file to append to
    :return: Logger object
    """
    logger = logging.getLogger(name=logger_name)
    logger.setLevel(logging.INFO)
    log_handler = logging.FileHandler(filename=file_name)
    formatter = CustomJsonFormatter(
        "%(timestamp)s - %(name)s - %(levelname)s - %(message)s",
    )
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)

    return logger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record["timestamp"] = datetime.datetime.utcnow().strftime(
            "%Y-%m-%dT%H:%M:%SZ"  # ISO 8601 compliant
        )
        log_record["level"] = log_record["levelname"]
        del log_record["levelname"]
