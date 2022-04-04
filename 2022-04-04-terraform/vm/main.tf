terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.15.0"
    }
  }
}

locals {
  machine_type = "e2-medium"
}

provider "google" {
  project = "jupyter-simula"
  zone    = "europe-west1-b"
}

data "google_project" "project" {
  # make the current project info available
}


resource "google_compute_instance" "node" {
  name         = "tools-meetup"
  machine_type = local.machine_type

  boot_disk {
    initialize_params {
      # see `gcloud compute images list`
      image = "ubuntu-os-cloud/ubuntu-2004-lts"
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }

  metadata_startup_script = file("startup.sh")

  scheduling {
    preemptible       = true
    automatic_restart = false
  }
}

output "public_ip" {
  value       = google_compute_instance.node.network_interface[0].access_config[0].nat_ip
  description = "Public IP"
}

output "ssh" {
  value       = "${google_compute_instance.node.name}.${google_compute_instance.node.zone}.${data.google_project.project.project_id}"
  description = "SSH name for root, after `gcloud compute config-ssh --project ..."
}
