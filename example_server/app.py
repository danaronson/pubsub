from flask import Flask, jsonify, request
from pubsub import PubSub
import os
import logging
import time
import signal

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.level = logging.DEBUG

app = Flask(__name__)

class TermException(Exception):
    pass

def handler(signum, frame):
    logger.info('got term... raising TermException')
    make_query_subscription.unsubscribe()
    raise TermException()


signal.signal(signal.SIGTERM, handler)


def create_data():
    return {"data": "here is some data"}



ps = PubSub('AWS',topic_arn=os.environ['AWS_SNS_ARN'], logger=logger)

def make_query_callback(data):
    logger.info('got request of: %s' % data)
    ps.publish('return_result', create_data())
    return
#

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    make_query_subscription.unsubscribe()
    logger.info('unsubscribed')
    func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'    

@app.route("/test", methods=["GET"])
def test():
    items = []
    sub = ps.subscribe('return_result', items=items)
    logger.debug('sleeping for a second to wait for results')
    ps.publish('make_query', {"data":"ok"})
    time.sleep(1)
    sub.unsubscribe()
    ret = {"data":items, "ok":True}
    return jsonify(ret)


if __name__ == '__main__':
    print 'starting'
    make_query_subscription = ps.subscribe('make_query', callback=make_query_callback)
    try:
        app.run(debug=True, use_reloader=False)
    except:
        logger.info('got exception, exiting')
        
