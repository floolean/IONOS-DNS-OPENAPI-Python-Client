# coding: utf-8

"""
    DNS API

    ## Working with the API Every endpoint uses the `X-API-Key` header for authorization, to obtain the key please see the [Official Documentation](/docs/getstarted).  Please note that any zone or record updates might conflict with active services. In such cases, the DNS records belonging to the conflicting services will be deactivated.  ## Support Support questions may be posted in English: <a href='/docs/getstarted#support'>API Support</a>.  Please note that we offer support in the business Hours Mo-Fri 9:00-17:00 EET. <h2> <details>   <summary>Release notes</summary>   <ul>     <li>Version 1.0.0 Exposed CRUD operations for customer zone.</li>     <li>Version 1.0.1 Added response body for UPDATE and CREATE record operations.</li>     <li>Version 1.0.2 Added new supported record types.</li>   </ul> </details> </h2>   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class RecordTypes(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Holds supported dns record types.
    """
    
    @schemas.classproperty
    def A(cls):
        return cls("A")
    
    @schemas.classproperty
    def AAAA(cls):
        return cls("AAAA")
    
    @schemas.classproperty
    def CNAME(cls):
        return cls("CNAME")
    
    @schemas.classproperty
    def MX(cls):
        return cls("MX")
    
    @schemas.classproperty
    def NS(cls):
        return cls("NS")
    
    @schemas.classproperty
    def SOA(cls):
        return cls("SOA")
    
    @schemas.classproperty
    def SRV(cls):
        return cls("SRV")
    
    @schemas.classproperty
    def TXT(cls):
        return cls("TXT")
    
    @schemas.classproperty
    def CAA(cls):
        return cls("CAA")
    
    @schemas.classproperty
    def TLSA(cls):
        return cls("TLSA")
    
    @schemas.classproperty
    def SMIMEA(cls):
        return cls("SMIMEA")
    
    @schemas.classproperty
    def SSHFP(cls):
        return cls("SSHFP")
    
    @schemas.classproperty
    def DS(cls):
        return cls("DS")
    
    @schemas.classproperty
    def HTTPS(cls):
        return cls("HTTPS")
    
    @schemas.classproperty
    def SVCB(cls):
        return cls("SVCB")
    
    @schemas.classproperty
    def CERT(cls):
        return cls("CERT")
    
    @schemas.classproperty
    def URI(cls):
        return cls("URI")
    
    @schemas.classproperty
    def RP(cls):
        return cls("RP")
    
    @schemas.classproperty
    def LOC(cls):
        return cls("LOC")
    
    @schemas.classproperty
    def OPENPGPKEY(cls):
        return cls("OPENPGPKEY")