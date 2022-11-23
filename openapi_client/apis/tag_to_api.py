import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.dynamic_dns_api import DynamicDNSApi
from openapi_client.apis.tags.records_api import RecordsApi
from openapi_client.apis.tags.zones_api import ZonesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DYNAMIC_DNS: DynamicDNSApi,
        TagValues.RECORDS: RecordsApi,
        TagValues.ZONES: ZonesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DYNAMIC_DNS: DynamicDNSApi,
        TagValues.RECORDS: RecordsApi,
        TagValues.ZONES: ZonesApi,
    }
)
