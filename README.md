Generic pubsub library which passes callback functions to when subscribing, and can have multiple back end drivers.

Usage
=====

    import pubsub
    ps = pubsub.PubSub(driver, logger = python_logger, **kwargs) # kwargs dependant on driver

    # to subscribe
    ps.subscribe(channel, callback_function) # callback function is called with published message

    # to unsubscribe
    ps.unsubscribe()
    
    # to publish
    ps.publish(channel, message) # message is any object that can be turned into json


Drivers
=======

AWS
---
* topic_arn
AWS SNS topic ARN.

Changelog
==========
* 0.1:
    * Initial version with support for both python2 and python3

