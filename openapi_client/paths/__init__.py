# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_ZONES = "/v1/zones"
    V1_ZONES_ZONE_ID = "/v1/zones/{zoneId}"
    V1_ZONES_ZONE_ID_RECORDS = "/v1/zones/{zoneId}/records"
    V1_ZONES_ZONE_ID_RECORDS_RECORD_ID = "/v1/zones/{zoneId}/records/{recordId}"
    V1_DYNDNS = "/v1/dyndns"
    V1_DYNDNS_BULK_ID = "/v1/dyndns/{bulkId}"
