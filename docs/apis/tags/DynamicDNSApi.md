<a name="__pageTop"></a>
# openapi_client.apis.tags.dynamic_dns_api.DynamicDNSApi

All URIs are relative to *https://api.hosting.ionos.com/dns*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_dyn_dns**](#activate_dyn_dns) | **post** /v1/dyndns | 
[**delete_dyn_dns**](#delete_dyn_dns) | **delete** /v1/dyndns/{bulkId} | 
[**disable_dyn_dns**](#disable_dyn_dns) | **delete** /v1/dyndns | 
[**update_dyn_dns**](#update_dyn_dns) | **put** /v1/dyndns/{bulkId} | 

# **activate_dyn_dns**
<a name="activate_dyn_dns"></a>
> DynamicDns activate_dyn_dns(dyn_dns_request)



Activate Dynamic Dns for a bundle of (sub)domains. The url from response will be used to update the ips of the (sub)domains. The following quota applies: 2 requests per minute per IP address. 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import dynamic_dns_api
from openapi_client.model.dynamic_dns import DynamicDns
from openapi_client.model.error import Error
from openapi_client.model.dyn_dns_request import DynDnsRequest
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
    api_instance = dynamic_dns_api.DynamicDNSApi(api_client)

    # example passing only required values which don't have defaults set
    body = DynDnsRequest(
        domains=[
            "domains_example"
        ],
        description="description_example",
    )
    try:
        api_response = api_instance.activate_dyn_dns(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DynamicDNSApi->activate_dyn_dns: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DynDnsRequest**](../../models/DynDnsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#activate_dyn_dns.ApiResponseFor200) | Succesful response.
400 | [ApiResponseFor400](#activate_dyn_dns.ApiResponseFor400) | Bad request.
401 | [ApiResponseFor401](#activate_dyn_dns.ApiResponseFor401) | Unauthorized request.
429 | [ApiResponseFor429](#activate_dyn_dns.ApiResponseFor429) | Rate limit excedeed.
500 | [ApiResponseFor500](#activate_dyn_dns.ApiResponseFor500) | Internal server error.

#### activate_dyn_dns.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DynamicDns**](../../models/DynamicDns.md) |  | 


#### activate_dyn_dns.ApiResponseFor400
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

#### activate_dyn_dns.ApiResponseFor401
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

#### activate_dyn_dns.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### activate_dyn_dns.ApiResponseFor500
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

# **delete_dyn_dns**
<a name="delete_dyn_dns"></a>
> delete_dyn_dns(bulk_id)



Disable Dynamic Dns for bulk id. The following quota applies: 2 requests per minute per IP address. 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import dynamic_dns_api
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
    api_instance = dynamic_dns_api.DynamicDNSApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bulkId': "bulkId_example",
    }
    try:
        api_response = api_instance.delete_dyn_dns(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DynamicDNSApi->delete_dyn_dns: %s\n" % e)
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
bulkId | BulkIdSchema | | 

# BulkIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_dyn_dns.ApiResponseFor200) | Succesful response.
401 | [ApiResponseFor401](#delete_dyn_dns.ApiResponseFor401) | Unauthorized request.
429 | [ApiResponseFor429](#delete_dyn_dns.ApiResponseFor429) | Rate limit excedeed.
500 | [ApiResponseFor500](#delete_dyn_dns.ApiResponseFor500) | Internal server error.

#### delete_dyn_dns.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_dyn_dns.ApiResponseFor401
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

#### delete_dyn_dns.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_dyn_dns.ApiResponseFor500
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

# **disable_dyn_dns**
<a name="disable_dyn_dns"></a>
> disable_dyn_dns()



Disable Dynamic Dns. The following quota applies: 2 requests per minute per IP address. 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import dynamic_dns_api
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
    api_instance = dynamic_dns_api.DynamicDNSApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.disable_dyn_dns()
    except openapi_client.ApiException as e:
        print("Exception when calling DynamicDNSApi->disable_dyn_dns: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#disable_dyn_dns.ApiResponseFor200) | Succesful response.
401 | [ApiResponseFor401](#disable_dyn_dns.ApiResponseFor401) | Unauthorized request.
429 | [ApiResponseFor429](#disable_dyn_dns.ApiResponseFor429) | Rate limit excedeed.
500 | [ApiResponseFor500](#disable_dyn_dns.ApiResponseFor500) | Internal server error.

#### disable_dyn_dns.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### disable_dyn_dns.ApiResponseFor401
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

#### disable_dyn_dns.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### disable_dyn_dns.ApiResponseFor500
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

# **update_dyn_dns**
<a name="update_dyn_dns"></a>
> update_dyn_dns(bulk_iddyn_dns_request)



Update Dynamic Dns for bulk id. The following quota applies: 2 requests per minute per IP address. 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import openapi_client
from openapi_client.apis.tags import dynamic_dns_api
from openapi_client.model.error import Error
from openapi_client.model.dyn_dns_request import DynDnsRequest
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
    api_instance = dynamic_dns_api.DynamicDNSApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bulkId': "bulkId_example",
    }
    body = DynDnsRequest(
        domains=[
            "domains_example"
        ],
        description="description_example",
    )
    try:
        api_response = api_instance.update_dyn_dns(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DynamicDNSApi->update_dyn_dns: %s\n" % e)
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
[**DynDnsRequest**](../../models/DynDnsRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
bulkId | BulkIdSchema | | 

# BulkIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_dyn_dns.ApiResponseFor200) | Succesful response.
400 | [ApiResponseFor400](#update_dyn_dns.ApiResponseFor400) | Bad request.
401 | [ApiResponseFor401](#update_dyn_dns.ApiResponseFor401) | Unauthorized request.
403 | [ApiResponseFor403](#update_dyn_dns.ApiResponseFor403) | Forbidden request.
404 | [ApiResponseFor404](#update_dyn_dns.ApiResponseFor404) | DynDns not found error.
429 | [ApiResponseFor429](#update_dyn_dns.ApiResponseFor429) | Rate limit excedeed.
500 | [ApiResponseFor500](#update_dyn_dns.ApiResponseFor500) | Internal server error.

#### update_dyn_dns.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dyn_dns.ApiResponseFor400
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

#### update_dyn_dns.ApiResponseFor401
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

#### update_dyn_dns.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) | [**Error**]({{complexTypePrefix}}Error.md) |  | 

#### update_dyn_dns.ApiResponseFor404
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

#### update_dyn_dns.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dyn_dns.ApiResponseFor500
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

