#!/bin/bash

# Stop Kafka
sudo /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-server-stop.sh

# Stop Zookeeper
sudo /home/vagrant/workspace/zookeeper-3.4.6/bin/zkServer.sh stop

