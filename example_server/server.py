import logging
from pubsub import PubSub
import os
import time
import signal


class TermException(Exception):
    pass

logging.basicConfig(format='%(asctime)s %(process)d [%(levelname)s] %(name)s: %(message)s')
logger = logging.getLogger(__name__)
logger.level = logging.DEBUG

def handler(signum, frame):
    logger.info('got term... raising TermException')
    raise TermException()


signal.signal(signal.SIGTERM, handler)


def create_data():
    logger.info("callback invoked")
    return {"data": "here is some data from server"}



def make_query_callback(data):
    logger.info('got request of: %s' % data)
    ps.publish('return_result', create_data())
    return


ps = PubSub('AWS',topic_arn=os.environ['AWS_SNS_ARN'], logger=logger)
make_query_subscription = ps.subscribe('make_query', callback=make_query_callback)

try:
    while True:
        time.sleep(100)
except:
    logger.info('terminating... dropping subscriber')
    make_query_subscription.unsubscribe()
    
    

