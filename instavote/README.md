Distributed Customer Feedback Application
=========

Overview
---------------
Distributed microservice applications are becoming the premier architecture in the software and I.T industry due to their scalability, high availablity, and versatility. Microservice architecture allows applications to scale independently of each other as well as fail independently of each other. In addition, developers can build microservices independently of other teams and build their microservices how they choose. This customer feedback application is a perfect example of this. The frontend apps are written with JavaScript and Python, and the backend controllers are written in Java and NodeJS. Redis provides a caching layer for collecting incoming customer feedback. Last but not least, the PostgreSQL database resides in a container just like the rest of the microservices.

In order to add actionable insights for businesses, I included a service that automatically facilitates customer service response to negative customer reviews. This service is hosted mainly using AWS Eventbridge along with a third party API integration for Zendesk. When a customer leaves negative feedback, the service issues an event to Eventbridge, which then formats the event and sends the data to Zendesk, creating a brand new, actionable ticket for customer service reps. 

Each microservice, as mentioned, exists independently of the others, living inside their containers. To orchestrate and manage multiple containers, I used Kubernetes on top of AWS EKS. You'll find the Terraform code for starting up the EKS cluster in this repo. You will also find the application code, their Dockerfiles, and also Jenkins build automation code for automated code integration and deployment into your EKS cluster. 

Getting started
---------------
Download and install Terraform (https://developer.hashicorp.com/terraform/install). Installation should be relatively painless with a package manager like Homebrew or Chocolatey. Once installed, you can build the required Kubernetes infrastructure in AWS using the files in the Terraform folder.

Download [Docker](https://www.docker.com/products/overview). If you are on Mac or Windows, [Docker Compose](https://docs.docker.com/compose) will be automatically installed. On Linux, make sure you have the latest version of [Compose](https://docs.docker.com/compose/install/). If you're using [Docker for Windows](https://docs.docker.com/docker-for-windows/) on Windows 10 pro or later, you must also [switch to Linux containers](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers).

Run in this directory:
```
docker-compose up
```
The app will be running at [http://localhost:5000](http://localhost:5000), and the results will be at [http://localhost:5001](http://localhost:5001).

Alternately, if you want to run it on a [Docker Swarm](https://docs.docker.com/engine/swarm/), first make sure you have a swarm. If you don't, run:
```
docker swarm init
```
Once you have your swarm, in this directory run:
```
docker stack deploy --compose-file docker-stack.yml vote
```

Architecture
-----

![Architecture diagram](architecture.png)

* A Python webapp which lets you vote between two options
* A Redis queue which collects new votes
* A .NET worker which consumes votes and stores them in…
* A Postgres database backed by a Docker volume
* A Node.js webapp which shows the results of the voting in real time


Note
----

The voting application only accepts one vote per client. It does not register votes if a vote has already been submitted from a client.
