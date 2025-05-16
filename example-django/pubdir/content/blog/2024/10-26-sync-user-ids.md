{
  template: post.html
  draft: false
  categories:
  [
    Docker
    DX
  ]
  title: Syncing User IDs in Your Dev Containers
  description: How to sync user ids in docker so your files have the correct owner.
  date: 2024-10-26T11:00:00.000Z
  cover: /posts/docker-city.jpg
}


If you use Docker on Linux (aka Docker Engine) for development without Docker Desktop, as you create new files they will often be owned by the root user and not your account. Of course you can just switch to Docker Desktop but then you lose the native performance of Docker Engine because everything in Docker Desktop is run in a Virtual Machine so that it works the same cross platform.

So if you wish to run Docker Engine and sync your User ID with your container, you can use the scripts below in your container build to make sure the User ID running your code is the same as your current account. This keeps files that are created in the container to have the correct owner synced with your user.

<script src="https://gist.github.com/pizzapanther/e341fd980d8469724465018db657d529.js"></script>

You can copy and install those scripts manually or add the following into your `Dockerfile`.

```Dockerfile
FROM bitnami/minideb:bookworm

ARG userid
ARG groupid

RUN install_packages curl wget unzip

WORKDIR /tmp
RUN wget -O scripts.zip https://gist.github.com/pizzapanther/e341fd980d8469724465018db657d529/archive/9feb4b9a6683b8534f9d906bdbafc24747740667.zip
RUN unzip -j scripts.zip
RUN chmod 777 *.bsh
RUN /tmp/group_init.bsh $groupid
RUN /tmp/user_init.bsh $userid $groupid

RUN mkdir -p /app
RUN chown -R $userid:$groupid /app
WORKDIR /app

USER $userid
RUN /tmp/dx_init.bsh
```

When you build your container you will have to pass in your User and Group ID like so:
`docker compose build --build-arg userid=$(id -u) --build-arg groupid=$(id -g)`

**Note:** The user created has sudo access and is named `worker`.

**Note:** This is assumes you will mount your code in `/app` with Docker Compose.

**Note:** The `dx_init.bsh` script is an additional script to link your Bash and Python history files so they are not lost when the container is stopped.
