#!/bin/bash
apt-get update -y

apt-get upgrade -y

sudo apt-get install -y \
    exfat-fuse \
    exfat-utils \
    git \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    openssl \
    ;

curl -fsSL https://get.docker.com -o get-docker.s
sh get-docker.sh

cp .env.example .env
