# Sample App

This is a simple app created to get all Fibonacci numbers up to nth place.

## Installatin (ArgoCD) (Preferred)

TPD

## Installation (Helm)

1. Navigate into the `charts` directory
2. Run `helm install peppy-penguin .`

## Installation (Docker)

1. Run `docker build -t sample-app .`
2. Run `docker run --publish 8080:8080 sample-app`
3. Open browser and go to link `localhost:8080/`

## Tests

1. Run `nosetests . -v`
