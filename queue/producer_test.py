from connection import Connection, QUEUE


def produce(msg):
    with Connection() as ch:
        ch.basic_publish(exchange='',
                         routing_key=QUEUE,
                         body=msg)

if __name__ == '__main__':
    import time # delay for docker compose
    time.sleep(6)
    produce('hi from producer_test.py')
