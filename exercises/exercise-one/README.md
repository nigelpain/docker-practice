# Exercise One

## Summary

The objective of this exercise is to create and Docker image and from this run a Docker container that will host a basic 
Python Flask application that returns the text "Hello world!" from an endpoint.

`docker image build -t exercise-one .`
`docker container run -d --name exercise-one -p 8080:8080 exercise-one`