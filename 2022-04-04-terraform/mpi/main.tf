terraform {
  required_providers {
    # null = {}
    # tls  = {}
    google = {
      source  = "hashicorp/google"
      version = "~> 4.15.0"
    }
    http = {
      source  = "hashicorp/http"
      version = "~> 2.1.0"
    }
  }
}

locals {
  user            = "minrk"
  machine_type    = "e2-medium"
  cpu_count       = 2 # cpus per node
  replicas        = 5 # number of nodes
  nfs_mount_point = "/shared"

}

provider "google" {
  project = "jupyter-simula"
  region  = "europe-west1"
  zone    = "europe-west1-b"
}

data "google_project" "project" {
  # make the current project info available
}


locals {
  machinefile = join("\n", [for i in range(local.replicas) : "node-${i}.c.${data.google_project.project.project_id}.internal:${local.cpu_count}"])
}



data "http" "myip" {
  url = "http://ipv4.icanhazip.com"
}


resource "google_compute_network" "net" {
  name                    = "mpi-network"
  auto_create_subnetworks = "false"
}

resource "google_compute_subnetwork" "subnet" {
  name          = "mpi-subnet"
  ip_cidr_range = "10.0.0.0/16"
  network       = google_compute_network.net.self_link
}

resource "google_compute_firewall" "allow-me" {
  name    = "allow-me"
  network = google_compute_network.net.self_link
  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
  source_ranges = ["${chomp(data.http.myip.body)}/32"]
}

resource "google_compute_firewall" "internal" {
  name    = "internal"
  network = google_compute_network.net.self_link
  allow {
    protocol = "all"
  }
  source_ranges = [google_compute_subnetwork.subnet.ip_cidr_range]
}

resource "google_compute_instance" "node" {
  count        = local.replicas
  name         = "node-${count.index}"
  machine_type = local.machine_type

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }
  network_interface {
    network    = google_compute_network.net.self_link
    subnetwork = google_compute_subnetwork.subnet.self_link
    network_ip = cidrhost(google_compute_subnetwork.subnet.ip_cidr_range, 100 + count.index)
    access_config {
    }
  }

  metadata_startup_script = file("startup.sh")

  metadata = {
    user-data = templatefile("./cloudinit.yaml", {
      "user"                   = local.user,
      "nfs_mount_point"        = local.nfs_mount_point,
      "rank"                   = count.index,
      "ssh_private_key"        = file("/Users/minrk/.ssh/id_tools_meetup"),
      "ssh_public_key"         = file("/Users/minrk/.ssh/id_tools_meetup.pub"),
      "ipcontroller_config_py" = file("ipcontroller_config.py"),
      "ipcluster_config_py"    = file("ipcluster_config.py"),
      "root_ip"                = cidrhost(google_compute_subnetwork.subnet.ip_cidr_range, 100),
      "cidr"                   = google_compute_subnetwork.subnet.ip_cidr_range,
      "machinefile"            = local.machinefile,
    })
  }
  scheduling {
    preemptible       = true
    automatic_restart = false
  }
}

output "public_ips" {
  value       = google_compute_instance.node[*].network_interface[0].access_config[0].nat_ip
  description = "all public IPs"
}

output "private_ips" {
  value       = google_compute_instance.node[*].network_interface[0].network_ip
  description = "all private IPs endpoints"
}

output "machinefile" {
  value       = local.machinefile
  description = "mpi machinefile using private dns"
}


output "root-ip" {
  value       = google_compute_instance.node[0].network_interface[0].access_config[0].nat_ip
  description = "public host of the root node"
}

output "root-ssh" {
  value       = "${google_compute_instance.node[0].name}.${google_compute_instance.node[0].zone}.${data.google_project.project.project_id}"
  description = "SSH name for root, after `gcloud compute config-ssh --project ..."
}

output "n" {
  value       = local.cpu_count * local.replicas
  description = "total number of cpu threads"
}
