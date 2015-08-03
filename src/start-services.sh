#!/bin/bash

# Start Zookeeper
sudo /home/vagrant/workspace/zookeeper/bin/zkServer.sh start

# Start Kafka
sudo /home/vagrant/workspace/kafka/bin/kafka-server-start.sh -daemon /home/vagrant/workspace/kafka/config/server.properties
