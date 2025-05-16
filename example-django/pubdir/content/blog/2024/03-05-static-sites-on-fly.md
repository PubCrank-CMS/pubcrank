{
  title: A Better Template for Your Frontend on Fly.io
  date: 2024-02-04T06:00:00.000Z
  categories:
  [
    fly.io
    frontend
  ]
  cover: /img/server-monolith.jpg
  description: A better way to serve static content on Fly.io
  draft: false
  template: post.html
}


While the [Fly docs](https://fly.io/docs/languages-and-frameworks/static/) have a good example of serving a static frontend, it leaves many details out and misses some features you will probably want if you're deploying anything with a little complexity. This post goes over how you can improve this setup and make it a better developer experience using Fly.io for static frontends.

## Better Web Server

While the web server documented is fast and simple, it hasn't been updated in ages and is missing some configuration options you will probably want. I found the [Static Web Server](https://static-web-server.net/) that is written in Rust to be fast and simple, but additionally is being actively developed and contains more configuration features you will probably need. My example config is shown below.

```toml
[general]

port = 8080
root = "/app/src/dist"
page-fallback = "/app/src/dist/index.html"

log-level = "info"

cache-control-headers = false

[advanced]

[[advanced.headers]]
source = "**/*.html"
[advanced.headers.headers]
Cache-Control = "public, max-age=1800"

[[advanced.headers]]
source = "**/"
[advanced.headers.headers]
Cache-Control = "public, max-age=1800"

[[advanced.headers]]
source = "**/*.{jpg,jpeg,png,ico,gif,woff2,js,webmanifest,xml,css}"
[advanced.headers.headers]
Cache-Control = "public, max-age=86400"
```

The first thing you'll notice is the `page-fallback` setting. This setting is useful if you're building a Single Page Application (SPA) with URL routes. While the goStatic server can also do this by serving a 404 page, this is incorrect because the browser receives a 404 status code which some browsers interpret as an error thus disrupting what is presented back to the user. Static Web Server properly handles the fallback and presents a 200 status code.

### HTTP Headers

Next you'll notice you can control the HTTP headers with Static Web Server which you can not do so well with goStatic. In my example this allows me to set cache headers for my HTML routes to a shorter time since they are not unique per version deploy. For all other files which have unique compiled names by my bundler I set higher cache times so my server can cut down on bandwidth.

## Build Process

The Fly example also does not show an example build process so I built out an example build process below. If you have a static frontend with some kind of compilation step, you probably want Fly.io to run the build for you, so that you have better repeatable builds. Below is an example `Dockerfile` I use on one of my projects.

```Dockerfile
FROM docker.io/bitnami/minideb:bookworm

USER root
ARG VERSION

RUN mkdir -p /app
WORKDIR /app

RUN install_packages bash curl ca-certificates && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && install_packages nodejs

COPY . /app
COPY bin/static-web-server /usr/bin
ENV VERSION=$VERSION
RUN sed -i -e "s/dev/$VERSION/g" src/version.js
RUN npm install
RUN npm run build

CMD static-web-server --config-file /app/config.toml
```

A couple things to note in this build:

1. I like using the `minideb` container to start from since it is a compact Debian distro that allows you to easily install Linux packages you might need. In this case we install Node 20 LTS.
2. When running the build, you must supply a version build arg like: `fly deploy --build-arg VERSION=v1.0.1`. You could skip this but I wanted to include a version number in my frontend build. This method of using a search and replace with `sed` works best with Vite I found instead of using ENVs.
3. You can see this build process is pretty standard otherwise with `npm install` and `npm run build`. So you can adapt those commands to whatever bundler you are using.

## Summing It Up

By switching your static file server and adding a build pipeline on Fly.io you can improve your frontend deployment process and support extra features you might need.
