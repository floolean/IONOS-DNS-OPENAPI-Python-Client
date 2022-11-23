<a name="__pageTop"></a>
# openapi_client.apis.tags.zones_api.ZonesApi

All URIs are relative to *https://api.hosting.ionos.com/dns*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zone**](#get_zone) | **get** /v1/zones/{zoneId} | 
[**get_zones**](#get_zones) | **get** /v1/zones | 
[**patch_zone**](#patch_zone) | **patch** /v1/zones/{zoneId} | 
[**update_zone**](#update_zone) | **put** /v1/zones/{zoneId} | 

# **get_zone**
<a name="get_zone"></a>
> CustomerZone get_zone(zone_id)



Returns a customer zone.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import zones_api
from openapi_client.model.customer_zone import CustomerZone
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
    api_instance = zones_api.ZonesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zoneId': "zoneId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_zone(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->get_zone: %s\n" % e)

    # example passing only optional values
    path_params = {
        'zoneId': "zoneId_example",
    }
    query_params = {
        'suffix': "subhost.example.com",
        'recordName': "www.subdomain.example.com",
        'recordType': "A,AAAA",
    }
    try:
        api_response = api_instance.get_zone(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->get_zone: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
suffix | SuffixSchema | | optional
recordName | RecordNameSchema | | optional
recordType | RecordTypeSchema | | optional


# SuffixSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RecordNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RecordTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#get_zone.ApiResponseFor200) | Succesful response.
401 | [ApiResponseFor401](#get_zone.ApiResponseFor401) | Unauthorized request.
500 | [ApiResponseFor500](#get_zone.ApiResponseFor500) | Internal server error.

#### get_zone.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomerZone**](../../models/CustomerZone.md) |  | 


#### get_zone.ApiResponseFor401
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

#### get_zone.ApiResponseFor500
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

# **get_zones**
<a name="get_zones"></a>
> [Zone] get_zones()



Returns list of customer zones.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import zones_api
from openapi_client.model.error import Error
from openapi_client.model.zone import Zone
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
    api_instance = zones_api.ZonesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_zones()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->get_zones: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_zones.ApiResponseFor200) | Succesful response.
401 | [ApiResponseFor401](#get_zones.ApiResponseFor401) | Unauthorized request.
500 | [ApiResponseFor500](#get_zones.ApiResponseFor500) | Internal server error.

#### get_zones.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Zone**]({{complexTypePrefix}}Zone.md) | [**Zone**]({{complexTypePrefix}}Zone.md) | [**Zone**]({{complexTypePrefix}}Zone.md) |  | 

#### get_zones.ApiResponseFor401
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

#### get_zones.ApiResponseFor500
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

# **patch_zone**
<a name="patch_zone"></a>
> patch_zone(zone_idrecord)



Replaces all records of the same name and type with the ones provided.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import zones_api
from openapi_client.model.record import Record
from openapi_client.model.error import Error
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
    api_instance = zones_api.ZonesApi(api_client)

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
        api_response = api_instance.patch_zone(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->patch_zone: %s\n" % e)
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
200 | [ApiResponseFor200](#patch_zone.ApiResponseFor200) | Succesful response.
400 | [ApiResponseFor400](#patch_zone.ApiResponseFor400) | Bad request.
401 | [ApiResponseFor401](#patch_zone.ApiResponseFor401) | Unauthorized request.
500 | [ApiResponseFor500](#patch_zone.ApiResponseFor500) | Internal server error.

#### patch_zone.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### patch_zone.ApiResponseFor400
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

#### patch_zone.ApiResponseFor401
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

#### patch_zone.ApiResponseFor500
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

# **update_zone**
<a name="update_zone"></a>
> update_zone(zone_idrecord)



Replaces all records in the zone with the ones provided

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import zones_api
from openapi_client.model.record import Record
from openapi_client.model.error import Error
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
    api_instance = zones_api.ZonesApi(api_client)

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
        api_response = api_instance.update_zone(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ZonesApi->update_zone: %s\n" % e)
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
200 | [ApiResponseFor200](#update_zone.ApiResponseFor200) | Succesful response.
400 | [ApiResponseFor400](#update_zone.ApiResponseFor400) | Bad request.
401 | [ApiResponseFor401](#update_zone.ApiResponseFor401) | Unauthorized request.
500 | [ApiResponseFor500](#update_zone.ApiResponseFor500) | Internal server error.

#### update_zone.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_zone.ApiResponseFor400
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

#### update_zone.ApiResponseFor401
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

#### update_zone.ApiResponseFor500
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

