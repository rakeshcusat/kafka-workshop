# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  if Vagrant.has_plugin?('vagrant-cachier')
    config.cache.enable :apt
  else
    printf("** Install vagrant-cachier plugin `vagrant plugin install vagrant-cachier` to speedup deploy.**\n")
  end

  if Vagrant.has_plugin?('vagrant-hostmanager')
    config.hostmanager.enabled = true
    config.hostmanager.manage_host = true
  else
    raise "** Install vagrant-hostmanager plugin `vagrant plugin install vagrant-hostmanager`.**\n"
  end


  app_servers = {
      "kafka-workshop" => "172.16.32.152",
  }

  app_servers.each do |app_server_name, app_server_ip|
    config.vm.define app_server_name do |app_config|
        app_config.vm.box = "chef/ubuntu-14.04"
        app_config.vm.provision "shell", inline: $provision_shell_script
        app_config.ssh.insert_key = false

        app_config.vm.network :private_network, ip: app_server_ip 
        app_config.vm.hostname = app_server_name 

        app_config.vm.provider :virtualbox do |vb|
          vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        end
      end
    end
end

# Provisioning script which sets-up the environment.

$provision_shell_script = <<SCRIPT
apt-get -qy update
echo "Setting timezone..."
echo "America/Los_Angeles" | sudo tee /etc/timezone
sudo dpkg-reconfigure --frontend noninteractive tzdata

# Install 
echo "Installing jre and jdk"
apt-get install htop default-jre default-jdk -y

# Make workspace directory in /home/vagrant directory
mkdir -p /home/vagrant/workspace

# Install Zookeeper
echo "Installing zookeeper"
cd /home/vagrant/workspace
tar -xf /vagrant/packages/zookeeper-3.4.6.tar.gz
ln -s zookeeper-3.4.6 zookeeper
cd zookeeper-3.4.6/
cp conf/zoo_sample.cfg conf/zoo.cfg


# Install kafka
echo "Installing kafka"
cd /home/vagrant/workspace
tar xzf /vagrant/packages/kafka_2.8.0-0.8.1.1-SNAPSHOT.tgz
ln -s  kafka_2.8.0-0.8.1.1-SNAPSHOT kafka

# Install pip and ipython
echo "Installing pip and ipython"
apt-get install python-pip ipython -y

# Install virtual environment
echo "Installing virtualenv"
sudo pip install virtualenv

# Create virtual environment in '/home/vagrant/workspace' directory
echo "Creating virtual env"
cd /home/vagrant/workspace
virtualenv .kafka-workspace

# Install kafka-python in virtual environment
echo "Installing kafka-python in virtualenv"
source .kafka-workspace/bin/activate
pip install kafka-python

SCRIPT
