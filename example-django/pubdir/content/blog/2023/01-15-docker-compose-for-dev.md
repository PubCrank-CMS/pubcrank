---
title: Using Docker Compose for Development without Going Crazy
date: 2023-01-15 00:00:00 -0600
categories:
  - development
  - docker compose
  - DX
cover: /img/docker-compose.jpg
canonical_url: https://hackernoon.com/using-docker-compose-for-development-without-going-crazy
---

Docker Compose is a great tool for development but I've never found a good example of how to use it for an ideal development workflow. Containers are immutable and thus by default are not an ideal development environment because development is fundamentally about changing things and then running the change. Most Docker Compose blogs talk about mounting your code repository as a volume which gets you around the immutability problem and mapping a port, but they don't go much past that. There are many more little tricks you can do to make your development experience better. Here I gathered all the tricks I've used to make Docker Compose a great development workflow.

## Create a Development Container

Your development container will probably diverge from your production and CI containers so you can handle having two diverging containers by either having a multi-staged build or having a separate Dockerfile for development. I normally fall into having a separate Dockerfile because your production and CI containers are often optimized for caching and being efficient to ship the container around. Trying to fit a development workflow into that can become clumsy and difficult to do cleanly. The downside is that you may duplicate some Dockerfile code between the two files. However, this should be small since the development container is often very few Dockerfile lines.

If you do use the staged build approach, use the [target](https://docs.docker.com/compose/compose-file/compose-file-v3/#target) attribute in your Docker Compose file.

## Sync User Permissions

It's good practice to not run as root but also for your development container it's nice to sync up the container user with your local user. This ensures your files mounted outside the container will have the correct permissions. To do this:

### 1. Add some build args to your Dockerfile

```
ARG userid
ARG groupid
```

### 2. Create a user in your Dockerfile with sudo access

```
# User setup
RUN addgroup mygroup --gid $groupid
RUN useradd -ms /bin/bash -u $userid -g $groupid myuser
RUN echo 'myuser ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
```

### 3. When building, pass in your build args

`docker-compose build --build-arg userid=$(id -u) --build-arg groupid=$(id -g)`

## Share Secrets

There is a `secrets` attribute you can use in Docker Compose. However, since this is for development we don't need to secure a production environment. I've found it easier to just mount some shared files and directories. Below is an example of some "secrets" I like to share.

```yaml
services:
  myapp:
    volumes:
      - .:/opt/myapp
      - $HOME/.git:/home/myuser/.git
      - $HOME/.ssh:/home/myuser/.ssh
      - $HOME/.netrc:/home/myuser/.netrc
      - $HOME/.pypirc:/home/myuser/.pypirc

```

## Share Git and SSH

See above. If you share your `.git` and `.ssh` directories with your development container you can execute git commands in your container without needing to jump in and out. This makes your development workflow much more enjoyable with fewer terminals open or fewer keystrokes.

## Install Some Development Tools

Especially if you use a separate Dockerfile and thus don't need to worry about the container size, install some extra development tools. Some apt packages I like to install: `procps, nano, vim, sudo, htop, tmux, redis-tools, autojump, openssh-client, wget, unzip`

And one of my other favorite tools: [thefuck](https://github.com/nvbn/thefuck)

## Share Shell Environments

Since you have a development container you can now really easy make a shared development environment setup. I like to include a shared `.bashrc` in my repository and then in the Dockerfile copy that to the user's home directory.

`COPY .bashrc /home/myuser/`

## Remember Your Command History

Since containers are immutable, they will lose your command history on rebuild. You can solve this by linking in a `.bash_history` file in your Dockerfile.

`RUN ln -s /opt/myapp/.bash_history /home/myuser/.bash_history`

## Full Setup

Below is the full setup, `Dockerfile.dev`, `compose.yaml`, and `.gitignore` additions.

### Dockerfile.dev

```Dockerfile
FROM ubuntu:bionic

ARG userid
ARG groupid

WORKDIR /build

# apt layer
RUN apt update
RUN apt install -y python3.8 python3.8-venv libpython3.8

# dev tools
RUN apt install -y procps nano vim sudo htop tmux redis-tools autojump openssh-client wget unzip

# pip, pdm setup
RUN python3.8 -m pip install pip --upgrade
RUN pip3.8 install --upgrade pip
RUN pip3.8 install pdm thefuck

# User setup
RUN addgroup mygroup --gid $groupid
RUN useradd -ms /bin/bash -u $userid -g $groupid myuser
RUN echo 'myuser ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /opt/myapp
USER myuser

COPY .bashrc /home/myuser/
RUN ln -s /opt/myapp/.bash_history /home/myuser/.bash_history
```

### compose.yaml

```yaml
version: "3.9"

services:
    myapp:
        network_mode: host
        build:
            context: .
            dockerfile: Dockerfile.dev
        command: /bin/bash
        environment:
            - DEV_CONTAINER=1
            - PYTHONUNBUFFERED=1
            - XDG_DATA_HOME=/opt/myapp/.local/share
        volumes:
            - .:/opt/myapp
            - $HOME/.git:/home/myuser/.git
            - $HOME/.ssh:/home/myuser/.ssh
            - $HOME/.netrc:/home/myuser/.netrc
            - $HOME/.pypirc:/home/myuser/.pypirc
        ports:
            - 8888:8888
            - 8000:8000
            - 8080:8080
            - 8081:8081
            - 3000:3000
            - 5000:5000
        shm_size: 4gb
        depends_on:
            - redis

    redis:
        image: 'bitnami/redis:latest'
        ports:
            - 6379:6379
        environment:
            - ALLOW_EMPTY_PASSWORD=yes
```

### .gitignore additions

```
.bash_history
.local

```
