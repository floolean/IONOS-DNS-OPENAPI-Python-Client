# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.customer_zone import CustomerZone
from openapi_client.model.dyn_dns_request import DynDnsRequest
from openapi_client.model.dynamic_dns import DynamicDns
from openapi_client.model.error import Error
from openapi_client.model.errors import Errors
from openapi_client.model.record import Record
from openapi_client.model.record_response import RecordResponse
from openapi_client.model.record_types import RecordTypes
from openapi_client.model.record_update import RecordUpdate
from openapi_client.model.zone import Zone
from openapi_client.model.zone_types import ZoneTypes
