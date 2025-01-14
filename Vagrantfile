# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant_API_Version="2"
require "yaml"
settings = YAML.load_file "node_scripts/vagrant-setting.yaml"
controls = settings["nodes"]["control"]["count"]
workers = settings["nodes"]["workers"]["count"]

Vagrant.configure(Vagrant_API_Version) do |config|

  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vbguest.auto_update = false
  end
   config.vm.define "host" do |host|
    host.vm.hostname = 'host'
    host.vm.box = settings["software"]["cluster"]["box"]
    host.vm.box_version = settings["software"]["cluster"]["version"]
    host.vm.network :private_network, ip: "192.168.80.9", :netmask => "255.255.255.0"
    host.vm.network :private_network, ip: "192.168.90.9", :netmask => "255.255.255.0"
    host.vm.provider :virtualbox do |vbox|
        vbox.customize ["modifyvm", :id, "--memory", 2048]
        vbox.customize ["modifyvm", :id, "--cpus", 2]
    end
  end

  (1..controls).each do |node_number|

    config.vm.define "master#{node_number}" do |master|
      master.vm.box = settings["software"]["cluster"]["box"]
      master.vm.box_version = settings["software"]["cluster"]["version"]
      master.vm.hostname = "master#{node_number}"
      # ip addr of control node will get ip + 10
      ip = node_number + 10
      master.vm.synced_folder ".", "/vagrant"
      master.vm.network :private_network, ip: "192.168.80.#{ip}", netmask: settings["network"]["netmask"]
      master.vm.network :private_network, ip: settings["network"]["extra_control_ip"], netmask: settings["network"]["netmask"]

      master.vm.provision "shell",
        env: {
          "DNS_SERVERS" => settings["network"]["dns_servers"].join(" "),
          "KUBERNETES_VERSION" => settings["software"]["kubernetes"],
          # there is no key in yaml, actually.
          "OS" => settings["software"]["os"],
          "ENVIRONMENT" => settings["environment"],
        },
        path: "node_scripts/common.sh"
      master.vm.provision "shell",
        env: {
          "CNI_NAME" => settings["software"]["cni"]["name"],
          "CNI_VERSION" => settings["software"]["cni"]["name"],
          "CALICO_VERSION" => settings["software"]["calico"],
          "CONTROL_IP" => settings["network"]["control_ip"],
          "POD_CIDR" => settings["network"]["pod_cidr"],
          "SERVICE_CIDR" => settings["network"]["service_cidr"]
        },
        path: "node_scripts/master.sh"

      master.vm.provider:virtualbox do |vb|
          vb.cpus = 4
          vb.memory = 4096
      end
      master.vm.disk :disk, size: "20GB", name: "extra_storage"
      # master.vm.provider :virtualbox do |vbox|
      #     vbox.customize ["modifyvm", :id, "--memory", 4096]
      #     vbox.customize ["modifyvm", :id, "--cpus", 2]
      #     vbox.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      # end
    end

  end

  (1..workers).each do |node_number|

    config.vm.define "worker#{node_number}" do |worker|
      worker.vm.box = settings["software"]["cluster"]["box"]
      worker.vm.hostname = "worker#{node_number}"
      ip = node_number + 20
      worker.vm.network :private_network, ip: "192.168.80.#{ip}", netmask: settings["network"]["netmask"]

      worker.vm.provision "shell",
        env: {
          "DNS_SERVERS" => settings["network"]["dns_servers"].join(" "),
          "ENVIRONMENT" => settings["environment"],
          "KUBERNETES_VERSION" => settings["software"]["kubernetes"],
          "OS" => settings["software"]["os"]
        },
        path: "node_scripts/common.sh"
      worker.vm.provision "shell", path: "node_scripts/worker.sh"

      worker.vm.provider:virtualbox do |vb|
          vb.cpus = 2
          vb.memory = 2048
      end
      worker.vm.disk :disk, size: "20GB", name: "extra_storage"
    end

  end
end
