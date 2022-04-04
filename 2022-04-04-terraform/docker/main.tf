# https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

resource "docker_image" "jupyter" {
  # name         = "jupyter/scipy-notebook:latest"
  name         = "jupyter/scipy-notebook:latest"
  keep_locally = false
}

resource "docker_container" "notebook" {
  image = docker_image.jupyter.repo_digest
  name  = "jupyter"
  ports {
    internal = 8888
    external = 9999
  }
}
