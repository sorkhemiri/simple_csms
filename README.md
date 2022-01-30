# simple CSMS
a simple charging station management system with only one route for calculating
the price of charging process according to CDR (charge detail record) and rating
price information.

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
