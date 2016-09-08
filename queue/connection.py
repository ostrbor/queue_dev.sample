import pika

URL = "amqp://guest:guest@rabbitmq:5672/%2F"
QUEUE = "project"


class Connection:

    def __init__(self):
        param = pika.URLParameters(URL)
        self.con = pika.BlockingConnection(param)
            
    def __enter__(self):
        channel = self.con.channel()
        channel.queue_declare(queue=QUEUE,
                              durable=True,
        )
        return channel
        
    def __exit__(self, exc_type, value, traceback):
        if exc_type is None:
            self.con.close()
        else:
            return False

