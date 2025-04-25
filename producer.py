from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('test_topic', b'Hello Kafka')
producer.flush()
print("Message sent")
