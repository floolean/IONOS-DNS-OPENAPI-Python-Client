# openapi-client
## Working with the API
Every endpoint uses the `X-API-Key` header for authorization, to obtain the key please see the [Official Documentation](/docs/getstarted).

Please note that any zone or record updates might conflict with active services. In such cases, the DNS records belonging to the conflicting services will be deactivated.

## Support
Support questions may be posted in English: <a href='/docs/getstarted#support'>API Support</a>.

Please note that we offer support in the business Hours Mo-Fri 9:00-17:00 EET.
<h2>
<details>
  <summary>Release notes</summary>
  <ul>
    <li>Version 1.0.0 Exposed CRUD operations for customer zone.</li>
    <li>Version 1.0.1 Added response body for UPDATE and CREATE record operations.</li>
    <li>Version 1.0.2 Added new supported record types.</li>
  </ul>
</details>
</h2>


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.2
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [/docs/getstarted#support](/docs/getstarted#support)

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import dynamic_dns_api
from openapi_client.model.dyn_dns_request import DynDnsRequest
from openapi_client.model.dynamic_dns import DynamicDns
from openapi_client.model.error import Error
# Defining the host is optional and defaults to https://api.hosting.ionos.com/dns
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.hosting.ionos.com/dns"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dynamic_dns_api.DynamicDNSApi(api_client)
    dyn_dns_request = DynDnsRequest(
        domains=[
            "domains_example"
        ],
        description="description_example",
    ) # DynDnsRequest | Dynamic Dns configuration.

    try:
        api_response = api_instance.activate_dyn_dns(dyn_dns_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DynamicDNSApi->activate_dyn_dns: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.hosting.ionos.com/dns*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DynamicDNSApi* | [**activate_dyn_dns**](docs/apis/tags/DynamicDNSApi.md#activate_dyn_dns) | **post** /v1/dyndns | 
*DynamicDNSApi* | [**delete_dyn_dns**](docs/apis/tags/DynamicDNSApi.md#delete_dyn_dns) | **delete** /v1/dyndns/{bulkId} | 
*DynamicDNSApi* | [**disable_dyn_dns**](docs/apis/tags/DynamicDNSApi.md#disable_dyn_dns) | **delete** /v1/dyndns | 
*DynamicDNSApi* | [**update_dyn_dns**](docs/apis/tags/DynamicDNSApi.md#update_dyn_dns) | **put** /v1/dyndns/{bulkId} | 
*RecordsApi* | [**create_records**](docs/apis/tags/RecordsApi.md#create_records) | **post** /v1/zones/{zoneId}/records | 
*RecordsApi* | [**delete_record**](docs/apis/tags/RecordsApi.md#delete_record) | **delete** /v1/zones/{zoneId}/records/{recordId} | 
*RecordsApi* | [**get_record**](docs/apis/tags/RecordsApi.md#get_record) | **get** /v1/zones/{zoneId}/records/{recordId} | 
*RecordsApi* | [**update_record**](docs/apis/tags/RecordsApi.md#update_record) | **put** /v1/zones/{zoneId}/records/{recordId} | 
*ZonesApi* | [**get_zone**](docs/apis/tags/ZonesApi.md#get_zone) | **get** /v1/zones/{zoneId} | 
*ZonesApi* | [**get_zones**](docs/apis/tags/ZonesApi.md#get_zones) | **get** /v1/zones | 
*ZonesApi* | [**patch_zone**](docs/apis/tags/ZonesApi.md#patch_zone) | **patch** /v1/zones/{zoneId} | 
*ZonesApi* | [**update_zone**](docs/apis/tags/ZonesApi.md#update_zone) | **put** /v1/zones/{zoneId} | 

## Documentation For Models

 - [CustomerZone](docs/models/CustomerZone.md)
 - [DynDnsRequest](docs/models/DynDnsRequest.md)
 - [DynamicDns](docs/models/DynamicDns.md)
 - [Error](docs/models/Error.md)
 - [Errors](docs/models/Errors.md)
 - [Record](docs/models/Record.md)
 - [RecordResponse](docs/models/RecordResponse.md)
 - [RecordTypes](docs/models/RecordTypes.md)
 - [RecordUpdate](docs/models/RecordUpdate.md)
 - [Zone](docs/models/Zone.md)
 - [ZoneTypes](docs/models/ZoneTypes.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Author





## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.apis.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```
