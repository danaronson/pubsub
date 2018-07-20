Generic pubsub library which passes callback functions to when subscribing, and can have multiple back end drivers.

Usage
=====

    import pubsub
    ps = pubsub.PubSub(driver, logger = python_logger, **kwargs) # kwargs dependant on driver

    # to subscribe
    subscription = ps.subscribe(channel, callback_function) # callback function is called with published message

    # to unsubscribe
    subscription.unsubscribe()
    
    # to publish
    ps.publish(channel, message) # message is any object that can be turned into json


Drivers
=======

AWS
---
    keyword arguments for PubSub class
        topic_arn
            AWS SNS topic ARN.
            
    AWS policy for user of package (TOPIC_ARN should be replaced with the real ARN)
       	{
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "VisualEditor0",
                    "Effect": "Allow",
                    "Action": [
                        "sqs:DeleteMessage",
                        "sns:Publish",
                        "sqs:AddPermission",
                        "sqs:ReceiveMessage",
                        "sqs:DeleteQueue",
                        "sqs:SendMessage",
                        "sns:Subscribe",
                        "sqs:GetQueueAttributes",
                        "sqs:CreateQueue",
                        "sqs:SetQueueAttributes"
                    ],
                    "Resource": [
                        "TOPIC-ARN",
                        "arn:aws:sqs:*:*:PS_SUB_*"
                    ]
                },
                {
                    "Sid": "VisualEditor1",
                    "Effect": "Allow",
                    "Action": [
                        "sns:SetSubscriptionAttributes",
                        "sns:Unsubscribe"
                    ],
                    "Resource": "*"
                }
            ]
        }            
        

Changelog
==========
* 0.1:
    * Initial version with support for both python2 and python3
* 0.2:
    * Subscription type support to allow multiple subscribers
    

