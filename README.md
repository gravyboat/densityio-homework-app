# densityio-homework-app
The modified version of
https://github.com/DensityCo/devops-homework/blob/master/app.py

# What This Repo Does

This application is a simple Postgres enabled test application which runs the
application through Travis CI as a test bed, then once merged to the master or
test branch it pushes the image to Docker Hub automatically so it is available
for deployments. The application is not deployed automatically.

# Application Setup

If you got here before setting up the infrastructure portion you’ll want to do
that first, head back over to
https://github.com/gravyboat/densityio-homework-infra and follow the
instructions there first, then come back here once you can run kubectl
commands.

Travis CI is already enabled on this repo, and docker creds are configured
within Travis, you can follow the instructions here that talk about getting
started with Docker and Travis: http://docs.travis-ci.com/user/getting-started/
Note that Travis will automatically test when you make a PR as noted here:
http://docs.travis-ci.com/user/pull-requests/

It is important to ensure that you complete the instructions to use Travis and
Docker (especially the environment variables so you can push to the docker
hub), as users will be pushing to the Docker registry.

# Application Deployment

Once you can push merged PRs to the repo automatically and run kubectl
commands you’re ready to do an image deployment you can use the following
command to do so:

`kubectl run --namespace simple-demo density --image=index.docker.io/forresta/densityio-prod --replicas=1 --port=5000`

This runs the docker container, now you can expose it to the internet via:

`kubectl expose --namespace=simple-demo deployment density --type=LoadBalancer --port=443 --target-port=5000 --name=density`

You can now view how your application is bound to the load balancer for public access:

`kubectl --namespace=simple-demo describe service density`

You can update the image by running the following:

NOTE: You SHOULD typically not be using latest because it can be problematic,
this is simply an example, tagging is better.

`kubectl --namespace simple-demo set image deployment/dock3 dock3=docka-docka-docka:latest`

# Deploying a Specific Feature Branch

Deployments to a specific feature branch can be accomplished by creating a
branch labeled "test" or something similar, then creating PRs against that
with a .travis.yml which pushes to a test version of the docker hub repo.
For an example of this check out the `.travis.yml` from
https://github.com/gravyboat/docka-docka-docka/tree/test where it's simply
checking the branch to confirm it is test then pushing to a different
docker hub repo.
