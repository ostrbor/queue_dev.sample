from connection import Connection, QUEUE


def callback(channel, method, prop, msg):
    from datetime import datetime
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open('log/consumer.log', 'ab') as log:
        log.write(now.encode('utf-8') + b' message: ' + msg + b'\n')

def consume():
    with Connection() as con:
        con.basic_consume(callback,
                          queue=QUEUE,
                          no_ack=True,
                         )
        con.start_consuming()

if __name__ == '__main__':
    consume()
