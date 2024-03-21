import os
import sys
import time

import pika

from models import Contact
from faker import Faker

fake = Faker()


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    queue_name = 'queue'
    channel.queue_declare(queue=queue_name, durable=True)

    #consumer = "Olena"
    users = []
    for _ in range(10):
        user = {"name": fake.name(),
                "phone": fake.phone_number(),
                "email": fake.email(),
                "address": fake.address()}
        users.append(user)

    for el in users:
        for _ in el.values():
            name = el["name"]
            phone = el["phone"]
            email = el["email"]

            address = el["address"]

    def callback(ch, method, properties, body):
        pk = body.decode()
        task = Contact.objects(id=pk, completed=False).first()
        if task:
            task.update(set__completed=True,
                        set__name=name,
                        set__phone=phone,
                        set__email=email,
                        set__address=address)
            print(f" [x] Received {task}")
            time.sleep(0.5)
            print(f" [x] Completed {method.delivery_tag} task")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
