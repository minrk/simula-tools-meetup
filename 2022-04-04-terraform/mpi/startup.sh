#!/bin/sh
set -e

apt-get update
apt-get install -y cloud-init nfs-common nfs-kernel-server

# load cloud-init service
cloud-init init
cloud-init modules
cloud-init modules --mode final
