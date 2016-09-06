from connection import Connection, QUEUE


def callback(ch, method, prop, msg):
    from datetime import datetime
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open('log/consumer.log', 'ab') as fp:
        fp.write(now.encode('utf-8') + b' message: ' + msg + b'\n')
    
def consume():
    with Connection() as ch:
        ch.basic_consume(callback,
                         queue=QUEUE,
                         no_ack=True,
        )
        ch.start_consuming()

if __name__ == '__main__':
    consume()
