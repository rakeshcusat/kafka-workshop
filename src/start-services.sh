#!/bin/bash

# Start Zookeeper
sudo /home/vagrant/workspace/zookeeper-3.4.6/bin/zkServer.sh start

# Start Kafka
sudo /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-server-start.sh -daemon /home/vagrant/workspace/kafka_2.10-0.8.2.1/config/server.properties