import logging
logger = logging.getLogger(__name__)

def pay(balance, price):
    logger.debug("pay() called: balance=%s price=%s", balance, price)
    if price > balance:
        logger.warning("insufficient balance: price was %s, your balance is %s", price, balance)
        return False
    logger.info("payment success: %s", price)
    return True
