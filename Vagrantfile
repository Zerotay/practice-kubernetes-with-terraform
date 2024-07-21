# -*- mode: ruby -*- 
# vi: set ft=ruby :

Vagrant_API_Version="2"

Vagrant.configure(Vagrant_API_Version) do |config|

  # Master
  config.vm.define:"master" do |cfg|
    cfg.vm.box = "ubuntu/jammy64"
    cfg.vm.provider:virtualbox do |vb|
        vb.name="master"
        vb.cpus = 4
        vb.memory = 4192
    end
    cfg.vm.hostname = "master"
    cfg.vm.synced_folder ".", "/vagrant"
    cfg.vm.network "private_network", ip: "192.168.56.10"
    cfg.vm.network "forwarded_port", guest: 22, host: 21022, auto_correct: false, id: "ssh"
    cfg.vm.network "forwarded_port", guest: 80, host: 10080
    cfg.vm.network "forwarded_port", guest: 8000, host: 18000
    cfg.vm.network "forwarded_port", guest: 8001, host: 18001
    cfg.vm.network "forwarded_port", guest: 8080, host: 18080
    cfg.vm.provision "shell", path: "cluster-init/master-init.sh"
  end

  # Node01
  config.vm.define "worker1" do |cfg|
    cfg.vm.box = "ubuntu/jammy64"
    cfg.vm.provider:virtualbox do |vb|
      vb.name = "worker1"
      vb.cpus = 2
      vb.memory = 2048
    end
    cfg.vm.hostname = "worker1"
    cfg.vm.synced_folder ".", "/vagrant"
    cfg.vm.network "private_network", ip: "192.168.56.11"
    cfg.vm.network "forwarded_port", guest: 22, host: 22022, auto_correct: false, id: "ssh"
    cfg.vm.network "forwarded_port", guest: 80, host: 30080
    cfg.vm.network "forwarded_port", guest: 8080, host: 38080
    # cfg.vm.provision "shell", path: "sshd_config.sh"
    cfg.vm.provision "shell", path: "cluster-init/worker1-init.sh"
  end

   # Node02
   config.vm.define "worker2" do |cfg|
    cfg.vm.box = "ubuntu/jammy64"
     cfg.vm.provider:virtualbox do |vb|
       vb.name="worker2"
       vb.cpus = 2
       vb.memory = 2048
     end
     cfg.vm.hostname = "worker2"
     cfg.vm.synced_folder ".", "/vagrant"
     cfg.vm.network "private_network", ip: "192.168.56.12"
     cfg.vm.network "forwarded_port", guest: 22, host: 23022, auto_correct: false, id: "ssh"
     cfg.vm.network "forwarded_port", guest: 80, host: 40080
     cfg.vm.network "forwarded_port", guest: 8080, host: 48080
    cfg.vm.provision "shell", path: "cluster-init/worker2-init.sh"
     # cfg.vm.provision "shell", path: "sshd_config.sh"
   end

   # Node03
   config.vm.define "worker3" do |cfg|
    cfg.vm.box = "ubuntu/jammy64"
     cfg.vm.provider:virtualbox do |vb|
       vb.name="worker3"
       vb.cpus = 2
       vb.memory = 2048
     end
     cfg.vm.hostname = "worker3"
     cfg.vm.synced_folder ".", "/vagrant"
     cfg.vm.network "private_network", ip: "192.168.56.13"
     cfg.vm.network "forwarded_port", guest: 22, host: 33022, auto_correct: false, id: "ssh"
     cfg.vm.network "forwarded_port", guest: 80, host: 20080
     cfg.vm.network "forwarded_port", guest: 8080, host: 28080
    cfg.vm.provision "shell", path: "cluster-init/worker3-init.sh"
     # cfg.vm.provision "shell", path: "sshd_config.sh"
   end
end
