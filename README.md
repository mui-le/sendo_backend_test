## Challenge

-------------------------------------------
You are recommended to build a Voucher system, to manage the code, so that no two codes have the same time, or overlap time on each other.
**E.g Valid**:

```
Code       | Value        | Start                | End
----------------------------------------------------------
SNSD       | 50000        | 2018-09-01 17:00:00  | 2018-09-15 17:00:00
SNSD       | 100000       | 2019-09-01 17:00:00  | 2019-09-15 17:00:00
```
**E.g Invalid**

```
Code       | Value        | Start                | End
----------------------------------------------------------
SNSD       | 50000        | 2018-09-01 17:00:00  | 2018-09-15 17:00:00
SNSD       | 100000       | 2018-09-01 17:00:00  | 2018-09-15 17:00:00
```
**Requirements**

- 1. Write a document provide the design that makes it easy to scale, and has good performance
- 2. Implement the functionality according to the above design, the recommended Go / or Python language here because it is necessary and suitable for your position
- 3. The code is well design, has Unit Test, has Integration Test / Benchmark Test to prove the program's correctness. You are recommended to use it with Docker to easily setup and start the program quickly.

Test data
---------

Test overlap times - true
code: SNSD, value: 5000, start: 2018-09-01 17:00:00, end: 2018-09-15 17:00:00
code: SNSD, value: 100000, start: 2019-09-01 17:00:00, end: 2019-09-15 17:00:00
Test unit overlap ... ok

Test overlap times - false
code: SNSD, value: 10000, start: 2019-09-14 17:00:00, end: 2019-09-15 17:00:00
Test unit overlap ... ok

Test overlap times with others(for updating) - True
code: SNSD, value: 5000, start: 2018-09-01 17:00:00, end: 2019-09-15 17:00:00
code: SNSD, value: 10000, start: 2019-09-01 17:00:00, end: 2019-09-15 17:00:00
Test unit overlap with others for updating ... ok

Test overlap times with others(for updating) - False
code: SNSD, value: 10000, start: 2020-09-01 17:00:00, end: 2021-09-01 17:00:00
Test unit overlap with others for updating ... ok

Test API can create a Voucher (POST request) - True
code: 'SNSD', value: 10000, start: '2018-09-01 17:00:00', end: '2019-09-15 17:00:00'
Test API can get a Voucher (GET request) ... ok

Test API can create a Voucher (POST request) - False
code: 'SNSD', value: 10000, start: '2018-09-01 17:00:00', end: '2019-09-15 17:00:00'
Test API can get a Voucher (GET request) ... ok

## Code
- The code was developed using docker container with the following stack
- Python 3.6
- Flask micro web framework
- Python unittest

It should work in other versions but it was not tested.

### Implementation design
- Implement a crud system that these requirements. Although I Can do it better than now, because I quite not good in the week. Thanks for your consideration.

### Considerations
- FlaskRESTful
- cURL command line 

### Testing
The development was based on docker containers - please check Dockerfile - and here are the step-by-step to reproduce the tests. Again, it should work on any other environment but it was not tested. Also, I'm assuming docker is already installed.


Clone the repo:
```sh
$ git clone git@github.com:mui-le/sendo_backend_test.git
```

Change to the project directory
```sh
$ cd sendo_backend_test
```

Build the image
```sh
$ docker build -t sendo:latest .
```

Starting container
```sh
$ docker run --name sendo -d -p 8000:5000 --rm sendo:latest
```

Execute the test
```sh
$ docker exec -it sendo /\home/\sendo/\tests.sh
```

**Demo version**
Listing
```sh
curl -i http://0.0.0.0:8000/api/v1.0/vouchers
```
-->response in the case already have data
```
HTTP/1.1 200 OK
Server: gunicorn/20.0.4
Date: Sun, 08 Dec 2019 10:24:26 GMT
Connection: close
Content-Type: application/json
Content-Length: 130

{"vouchers":[{"code":"SNSD","end":"Sun, 15 Sep 2019 17:00:00 GMT","id":1,"start":"Sat, 01 Sep 2018 17:00:00 GMT","value":10000}]}
```

Creating
```sh
curl -X POST -d '{"code": "SNSD", "value": 10000, "start": "2018-09-01 17:00:00", "end": "2019-09-15 17:00:00"}' -i -H "Content-Type: application/json" http://0.0.0.0:8000/api/v1.0/vouchers
```
-> Response:
```
HTTP/1.1 200 OK
Server: gunicorn/20.0.4
Date: Sun, 08 Dec 2019 10:24:26 GMT
Connection: close
Content-Type: application/json
Content-Length: 130

{"vouchers":[{"code":"SNSD","end":"Sun, 15 Sep 2019 17:00:00 GMT","id":1,"start":"Sat, 01 Sep 2018 17:00:00 GMT","value":10000}]}
```

Creating overlap -> fail
```sh
curl -X POST -d '{"code": "SNSD", "value": 10000, "start": "2018-09-01 17:00:00", "end": "2019-09-15 17:00:00"}' -i -H "Content-Type: application/json" http://0.0.0.0:8000/api/v1.0/vouchers
```

-> Response:
```
HTTP/1.1 400 BAD REQUEST
Server: gunicorn/20.0.4
Date: Sun, 08 Dec 2019 10:21:39 GMT
Connection: close
Content-Type: application/json
Content-Length: 24

{"error":"Bad request"}
```

Updating
```sh
curl -X PUT -d '{"code": "SNSD", "value": 10000, "start": "2020-09-01 17:00:00", "end": "2020-09-15 17:00:00"}' -i -H "Content-Type: application/json" http://0.0.0.0:8000/api/v1.0/vouchers/1
```

-> response:
```
HTTP/1.1 201 CREATED
Server: gunicorn/20.0.4
Date: Sun, 08 Dec 2019 10:32:33 GMT
Connection: close
Content-Type: application/json
Content-Length: 127

{"voucher":{"code":"SNSD","end":"Tue, 15 Sep 2020 17:00:00 GMT","id":1,"start":"Tue, 01 Sep 2020 17:00:00 GMT","value":10000}}
```

### Others
You can make some examples with url
- DETAIL: /api/v1.0/vouchers/<int:voucher_id>
- DELETE: /api/v1.0/vouchers/<int:voucher_id>', methods=['DELETE']















