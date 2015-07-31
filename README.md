# Kafka-workshop

## Prerequisites
---
 - Vagrant (if it is not installed then follow the instrctions given [here](https://github.com/rakeshcusat/kafka-workshop/wiki/Vagrant-installation-steps))
 - Internet connection
 - Basic python understanding
 
## Setup
---
1. Clone this repository or download it by clicking `Dowload zip` button given on left.
  
  ```
  git clone git@github.com:rakeshcusat/kafka-workshop.git
  ```
2. Bring up the vagrant box by executing the following command.
  
  ```
  cd kafka-workshop
  vagrant up
  ```
  This step will take couple of minutes. This step will bring up the `Ubuntu 14.04` box with `zookeeper` and `kafa` installed in `/home/vagrant/workspace/` directory. This vagrant box also has `.kafka-workspace` virtual environment in `/home/vagrant/workspace/` direcotry. This virtual environment is used by the python scripts (kafka-consumer.py & kafka-producer.py)
  
3. Open two terminals and ssh to the vagrant from `kafka-workshop` directory. One can be used for producer whereas other can be used for consumer script. Run the following commands on both the terminals.
  
  ```
  vagrant ssh
  cd workspace
  ```
  You will notice zookeeper and kafka directory inside `workshop` directory, whereas `src` directory of the project is mapped to `/vagrant/src/` directory.
  
4. On one of the terminals start the services by executing the following command.
  
  ```
  /vagrant/src/start-services.sh
  ```
  Execute `pgrep java` to make sure services (zookeeper & kafka) are up. If you don't see any output then something is definitely wrong. Check the troubleshooting section.
  
5. Execute the following command on any of the terminals to create the kafka topic.

  ```
  /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
  ```
  
6. Execute the following command on consumer-terminal. Consumer script will keep waiting for the messages from the producer. Once a message is available, it will print on the console.
  
  ```
  source /home/vagrant/workspace/.kafka-workspace/bin/activate
  python /vagrant/src/kafka-consumer.py
  ```
  
7. Execute the following command on producer-terminal to publish `"Hello from script"` message on `test` topic.
  
  ```
  source /home/vagrant/workspace/.kafka-workspace/bin/activate
  python /vagrant/src/kafka-producer.py
  ```
  
8. **__voila!!!__** The client will print the message on the console. It will be something similar to this.
  
  ```
  (.kafka-workspace)vagrant@kafka-workshop:~/workspace$ python /vagrant/src/kafka-consumer.py
  test:0:24: key=topic-key value=Hello from script
  ```
  
9. Feel free to play with the consumer and producer scripts. Also check out the [command section](#commands) for cool commands.

### Commands
---
##### Kafka commands
---
Following is a list of interesting commands, more can be found [here](https://cwiki.apache.org/confluence/display/KAFKA/Replication+tools) and [here](https://cwiki.apache.org/confluence/display/KAFKA/System+Tools#SystemTools-GetOffsetShell).

1. To list all the topics.
  
  ```
  bin/kafka-topics.sh --zookeeper <zookeeper-host>:<port> --list
  ```
  e.g
  
  ```
  /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-topics.sh --zookeeper localhost:2181 --list
  ```
2. To create a topic.
  
  ```
  bin/kafka-topics.sh --create --zookeeper <zookeeper-host>:<port> --replication-factor <factor> --partitions <#-of-partition --topic <topic-name>
  ```
  e.g
  
  ```
  /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test2
  ```
3. To print latest log size.
  
  ```
  bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list <broker-host>:<port> --topic <topic> --time <time>
  ```
  e.g
  
  ```
  /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic test --time -1
  ```
4. List info for topics whose leader for a partition is not available
  
  ```
  bin/kafka-topics.sh --zookeeper <zookeeper-host>:<port> --describe --unavailable-partitions
  ```
  e.g
  
  ```
  /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-topics.sh --zookeeper localhost:2181 --describe --unavailable-partitions
  ```
5. List info for topics which have under replicated count
  
  ```
  bin/kafka-topics.sh --zookeeper <zookeeper-host>:<port> --describe --under-replicated-partitions
  ```
  e.g
  
  ```
  /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-topics.sh --zookeeper localhost:2181 --describe --under-replicated-partitions
  ```
6. Start kafka producer.
  ```
  bin/kafka-console-producer.sh --broker-list <broker-host>:<port> --topic <topic-name>
  ```
  e.g
  
  ```
  /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test 
  ```
  once this command is executed, you can type on the console and hit enter to send the text.
7. Start kafka consumer.
  
  ```
  bin/kafka-console-consumer.sh --zookeeper <zookeeper-host>:<port> --topic test --from-beginning
  ```
  e.g
  
  ```
  /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning
  ```
  This application reads the messages from the begining and it also print the messages on the console as soon as soon it is available for consumption. This script doesn't commit the messages. That's means if you start the application again it will again consume the messages from begning.
8. Export zookeeper offsets
  
  ```
  bin/kafka-run-class.sh kafka.tools.ExportZkOffsets  --zkconnect  <zookeeper-host>:<port> --output-file <output-file-name>
  ```
  e.g
  
  ```
  /home/vagrant/workspace/kafka_2.10-0.8.2.1/bin/kafka-run-class.sh kafka.tools.ExportZkOffsets  --zkconnect localhost:2181 --output-file test.txt
  ```
    
##### Zookeeper commands
---
1. To connect to Zookeeper client.
  
  ```
  bin/zkCli.sh -server <zookeeper-host>:<port>
  ```
  e.g
  
  ```
  /home/vagrant/workspace/zookeeper-3.4.6/bin/zkCli.sh -server localhost:2181
  ```
  Once you are logged into cli then you can explore the zk data structure. It is organized as file system. you can use command like `ls /consumers` to list down the different consumers.
    
### Repository information
---
The most important files are listed below.
```
├── Vagrantfile
└── src
    ├── kafka-consumer.py
    ├── kafka-producer.py
    ├── start-services.sh
    └── stop-services.sh
```
 1. [Vagrantfile](https://github.com/rakeshcusat/kafka-workshop/blob/master/Vagrantfile): This file creates the vagrant box which is Ubuntu-14.04 based. This vagrant box provide required environment. The provision script of vagrant automatically create the environment and installed the required packages in `/home/vagrant/workspace/` directory.
 2. [src/kafka-consumer.py](https://github.com/rakeshcusat/kafka-workshop/blob/master/src/kafka-consumer.py): This python script act as consumer which consumes the messages publish on `test` topic. It uses python library called [kafka-python](http://kafka-python.readthedocs.org/en/latest/usage.html#kafkaconsumer)
 3. [src/kafka-producer.py](https://github.com/rakeshcusat/kafka-workshop/blob/master/src/kafka-producer.py): This python script act as producer which publishes the messages on `test` topic.  It uses python library called [kafka-python](http://kafka-python.readthedocs.org/en/latest/usage.html#simpleproducer)
 4. [src/start-services.sh](https://github.com/rakeshcusat/kafka-workshop/blob/master/src/start-services.sh): This shell script starts zookeeper and kafka service.
 5. [src/stop-services.sh](https://github.com/rakeshcusat/kafka-workshop/blob/master/src/stop-services.sh): This shell script stops zookeeper and kafka service.
