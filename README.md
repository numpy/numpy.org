# Numpy.org

## Getting Started

To contribute to the website, you'll first need to install Hugo.

https://gohugo.io/getting-started/quick-start/

Hint: If you're on a Mac, you can run `brew install hugo`.

Next, clone this repository, and install the theme:

```
git submodule update --init
```

The development web server is started with:

```
hugo server
```

or

```
hugo server -D
```

to run the hugo server with draft enabled.

after which the site should be served at http://localhost:1313.

## Using docker:

* Build the docker image:

```

  $ docker build -t deploy_surge .
  $ docker images

```

Run the image:

```
  $ docker run -e SURGE_LOGIN=${SURGE_LOGIN} -e SURGE_TOKEN=${SURGE_TOKEN} -e PR_NUMBER=${TRAVIS_PULL_REQUEST} deploy_surge
```

Note: `SURGE_LOGIN` and `SURGE_TOKEN` is needed only when you want to push the
build in surge server. The URL will look like: numpy-${PR_NUMBER}.surge.sh

So you can use some random number instead of `TRAVIS_PULL_REQUEST` variable.

You also can run the docker image in daemon mode and then interact with the container and run the hugo server.



