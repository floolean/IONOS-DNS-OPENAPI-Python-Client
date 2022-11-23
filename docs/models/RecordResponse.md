# openapi_client.model.record_response.RecordResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**rootName** | str,  | str,  | Root zone name. | [optional] 
**type** | [**RecordTypes**](RecordTypes.md) | [**RecordTypes**](RecordTypes.md) |  | [optional] 
**content** | str,  | str,  |  | [optional] 
**changeDate** | str,  | str,  | The date of the last change formatted as yyyy-MM-dd&#x27;T&#x27;HH:mm:ss.SSS&#x27;Z&#x27; | [optional] 
**ttl** | decimal.Decimal, int,  | decimal.Decimal,  | Time to live for the record, recommended 3600. | [optional] 
**prio** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**disabled** | bool,  | BoolClass,  | When is true, the record is not visible for lookup. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

