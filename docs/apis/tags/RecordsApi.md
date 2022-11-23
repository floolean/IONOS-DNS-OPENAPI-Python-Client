<a name="__pageTop"></a>
# openapi_client.apis.tags.records_api.RecordsApi

All URIs are relative to *https://api.hosting.ionos.com/dns*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_records**](#create_records) | **post** /v1/zones/{zoneId}/records | 
[**delete_record**](#delete_record) | **delete** /v1/zones/{zoneId}/records/{recordId} | 
[**get_record**](#get_record) | **get** /v1/zones/{zoneId}/records/{recordId} | 
[**update_record**](#update_record) | **put** /v1/zones/{zoneId}/records/{recordId} | 

# **create_records**
<a name="create_records"></a>
> [RecordResponse] create_records(zone_idrecord)



Creates records for a customer zone.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import records_api
from openapi_client.model.record import Record
from openapi_client.model.error import Error
from openapi_client.model.record_response import RecordResponse
from pprint import pprint
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
    api_instance = records_api.RecordsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zoneId': "zoneId_example",
    }
    body = [
        Record(
            name="name_example",
            type=RecordTypes("A"),
            content="content_example",
            ttl=1,
            prio=1,
            disabled=False,
        )
    ]
    try:
        api_response = api_instance.create_records(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->create_records: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Record**]({{complexTypePrefix}}Record.md) | [**Record**]({{complexTypePrefix}}Record.md) | [**Record**]({{complexTypePrefix}}Record.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zoneId | ZoneIdSchema | | 

# ZoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_records.ApiResponseFor201) | Records created.
400 | [ApiResponseFor400](#create_records.ApiResponseFor400) | Bad request.
401 | [ApiResponseFor401](#create_records.ApiResponseFor401) | Unauthorized request.
500 | [ApiResponseFor500](#create_records.ApiResponseFor500) | Internal server error.

#### create_records.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RecordResponse**]({{complexTypePrefix}}RecordResponse.md) | [**RecordResponse**]({{complexTypePrefix}}RecordResponse.md) | [**RecordResponse**]({{complexTypePrefix}}RecordResponse.md) |  | 

#### create_records.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### create_records.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### create_records.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_record**
<a name="delete_record"></a>
> delete_record(zone_idrecord_id)



Delete a record from the customer zone.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import records_api
from openapi_client.model.error import Error
from pprint import pprint
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
    api_instance = records_api.RecordsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zoneId': "zoneId_example",
        'recordId': "recordId_example",
    }
    try:
        api_response = api_instance.delete_record(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->delete_record: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zoneId | ZoneIdSchema | | 
recordId | RecordIdSchema | | 

# ZoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RecordIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_record.ApiResponseFor200) | Succesful response.
404 | [ApiResponseFor404](#delete_record.ApiResponseFor404) | Record not found.
401 | [ApiResponseFor401](#delete_record.ApiResponseFor401) | Unauthorized request.
500 | [ApiResponseFor500](#delete_record.ApiResponseFor500) | Internal server error.

#### delete_record.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_record.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### delete_record.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### delete_record.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_record**
<a name="get_record"></a>
> RecordResponse get_record(zone_idrecord_id)



Returns the record from the customer zone with the mentioned id.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import records_api
from openapi_client.model.error import Error
from openapi_client.model.record_response import RecordResponse
from pprint import pprint
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
    api_instance = records_api.RecordsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zoneId': "zoneId_example",
        'recordId': "recordId_example",
    }
    try:
        api_response = api_instance.get_record(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->get_record: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zoneId | ZoneIdSchema | | 
recordId | RecordIdSchema | | 

# ZoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RecordIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_record.ApiResponseFor200) | Succesful response.
404 | [ApiResponseFor404](#get_record.ApiResponseFor404) | Record not found.
401 | [ApiResponseFor401](#get_record.ApiResponseFor401) | Unauthorized request.
500 | [ApiResponseFor500](#get_record.ApiResponseFor500) | Internal server error.

#### get_record.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RecordResponse**](../../models/RecordResponse.md) |  | 


#### get_record.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### get_record.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### get_record.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_record**
<a name="update_record"></a>
> RecordResponse update_record(zone_idrecord_idrecord_update)



Update a record from the customer zone.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import records_api
from openapi_client.model.error import Error
from openapi_client.model.record_response import RecordResponse
from openapi_client.model.record_update import RecordUpdate
from openapi_client.model.errors import Errors
from pprint import pprint
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
    api_instance = records_api.RecordsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zoneId': "zoneId_example",
        'recordId': "recordId_example",
    }
    body = RecordUpdate(
        disabled=False,
        content="content_example",
        ttl=1,
        prio=1,
    )
    try:
        api_response = api_instance.update_record(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecordsApi->update_record: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RecordUpdate**](../../models/RecordUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zoneId | ZoneIdSchema | | 
recordId | RecordIdSchema | | 

# ZoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RecordIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_record.ApiResponseFor200) | Record updated.
400 | [ApiResponseFor400](#update_record.ApiResponseFor400) | Bad request.
401 | [ApiResponseFor401](#update_record.ApiResponseFor401) | Unauthorized request.
404 | [ApiResponseFor404](#update_record.ApiResponseFor404) | Record not found.
500 | [ApiResponseFor500](#update_record.ApiResponseFor500) | Internal server error.

#### update_record.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RecordResponse**](../../models/RecordResponse.md) |  | 


#### update_record.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Errors**]({{complexTypePrefix}}Errors.md) | [**Errors**]({{complexTypePrefix}}Errors.md) | [**Errors**]({{complexTypePrefix}}Errors.md) |  | 

#### update_record.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### update_record.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### update_record.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

