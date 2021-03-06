# simple CSMS
a simple charging station management system with only one route for calculating
the price of charging process according to CDR (charge detail record) and rating
price information.

## Note for the Reviewer
for the second part of the challenge see [here](NOTES.md)

## Getting Started
create a `.env` file in the root directory of the project. then copy and paste
`.env.example` file content into the `.env` file.  
NOTE: you can change all the default values of the [project config](src/settings/config.py)
by adding the specified key and custom value to `.env` file (environment keys are NOT case-sensitive)

## API Security
the project use API key as a method of authorization. You would need to create
a random hash as API key and set it inside the `.env` file with `API_KEY_SECRET` for the APIs to work properly.
```bash
openssl rand -hex 32
```
the output is something like this:
`e5720f7032fed2478c57b3f6a87a175a250806e3afba74fa15e5bc84032176d1`  
set the desired value to `API_KEY_SECRET` inside the `.env` file. like this
```
API_KEY_SECRET=your_desired_value
```
remember to set the value as the value of `X_ACCESS_KEY` header (you can change the
header key by setting your desired name as value for `API_KEY_NAME` in the `.env` file just like above.) in the
request.

# Building The Project
## Running Using Docker
if you have docker and docker-compose installed you can build the project
by the command below in the project root directory.
```bash
make docker
```

## Build Locally (For Development)
run the command below in the project root directory to build the project 
locally (without using Docker):
```bash
make build
```
NOTE: to see other options provided by make file run the command below in the
root directory.
```bash
make help
```
## TESTS
to run the tests in dockerized mode run the command below in the root directory.
```bash
 chmod +x run_test.sh && ./run_test.sh
```
to run the tests in the local build mode (without using docker) run the command
below in the project root:
```bash
make test
```
## API DOCUMENTS
if you are running the project in the debug mode(with `DEBUG` key set to true in
the `.env` file, debug is true by default) you can see projects SWAGGER API in the [here](http://localhost:8000/docs).