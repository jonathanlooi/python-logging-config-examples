"""
Example of using logging.basicConfig to log with ISO 8601 compliant timestamps.
"""

import smtplib
import logging
import time

logging.Formatter.converter = time.gmtime  # set to UTC

logging.basicConfig(
    level=logging.INFO,
    filename="test.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",  # ISO 8601 compliant
)


def main():
    with smtplib.SMTP(host="smtp-relay.gmail.com", port=587) as server:
        logging.info(server.noop())


if __name__ == "__main__":
    main()
