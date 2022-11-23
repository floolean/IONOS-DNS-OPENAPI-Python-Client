import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.v1_zones import V1Zones
from openapi_client.apis.paths.v1_zones_zone_id import V1ZonesZoneId
from openapi_client.apis.paths.v1_zones_zone_id_records import V1ZonesZoneIdRecords
from openapi_client.apis.paths.v1_zones_zone_id_records_record_id import V1ZonesZoneIdRecordsRecordId
from openapi_client.apis.paths.v1_dyndns import V1Dyndns
from openapi_client.apis.paths.v1_dyndns_bulk_id import V1DyndnsBulkId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ZONES: V1Zones,
        PathValues.V1_ZONES_ZONE_ID: V1ZonesZoneId,
        PathValues.V1_ZONES_ZONE_ID_RECORDS: V1ZonesZoneIdRecords,
        PathValues.V1_ZONES_ZONE_ID_RECORDS_RECORD_ID: V1ZonesZoneIdRecordsRecordId,
        PathValues.V1_DYNDNS: V1Dyndns,
        PathValues.V1_DYNDNS_BULK_ID: V1DyndnsBulkId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ZONES: V1Zones,
        PathValues.V1_ZONES_ZONE_ID: V1ZonesZoneId,
        PathValues.V1_ZONES_ZONE_ID_RECORDS: V1ZonesZoneIdRecords,
        PathValues.V1_ZONES_ZONE_ID_RECORDS_RECORD_ID: V1ZonesZoneIdRecordsRecordId,
        PathValues.V1_DYNDNS: V1Dyndns,
        PathValues.V1_DYNDNS_BULK_ID: V1DyndnsBulkId,
    }
)
