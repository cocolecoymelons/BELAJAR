import logging
from log_setup import setup_logging
import payment

setup_logging()
logger = logging.getLogger(__name__)

logger.info("Start program")
payment.pay(10000, 5000)
payment.pay(2000, 5000)

print("payment.py -> __name__ =", __name__)
print("main.py -> __name__ =", __name__)


try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Failed to calculate")

logger.info("Program finish")
