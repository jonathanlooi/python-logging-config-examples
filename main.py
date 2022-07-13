import smtplib
import example_loggers


def main():
    utc_logger = example_loggers.create_utc_logger(
        logger_name="utc_logger", file_name="example.log"
    )
    json_logger = example_loggers.create_json_logger(
        logger_name="json_logger", file_name="example.jsonl"
    )
    with smtplib.SMTP(host="smtp-relay.gmail.com", port=587) as server:
        utc_logger.info(server.noop())
        json_logger.info(server.noop(), extra={"cool_new_field": 100})


if __name__ == "__main__":
    main()
