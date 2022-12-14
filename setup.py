# coding: utf-8

"""
    DNS API

    ## Working with the API Every endpoint uses the `X-API-Key` header for authorization, to obtain the key please see the [Official Documentation](/docs/getstarted).  Please note that any zone or record updates might conflict with active services. In such cases, the DNS records belonging to the conflicting services will be deactivated.  ## Support Support questions may be posted in English: <a href='/docs/getstarted#support'>API Support</a>.  Please note that we offer support in the business Hours Mo-Fri 9:00-17:00 EET. <h2> <details>   <summary>Release notes</summary>   <ul>     <li>Version 1.0.0 Exposed CRUD operations for customer zone.</li>     <li>Version 1.0.1 Added response body for UPDATE and CREATE record operations.</li>     <li>Version 1.0.2 Added new supported record types.</li>   </ul> </details> </h2>   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "openapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.7.0",
    "setuptools >= 21.0.0",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.7",
]

setup(
    name=NAME,
    version=VERSION,
    description="DNS API",
    author="API Support",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "DNS API"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    ## Working with the API Every endpoint uses the &#x60;X-API-Key&#x60; header for authorization, to obtain the key please see the [Official Documentation](/docs/getstarted).  Please note that any zone or record updates might conflict with active services. In such cases, the DNS records belonging to the conflicting services will be deactivated.  ## Support Support questions may be posted in English: &lt;a href&#x3D;&#x27;/docs/getstarted#support&#x27;&gt;API Support&lt;/a&gt;.  Please note that we offer support in the business Hours Mo-Fri 9:00-17:00 EET. &lt;h2&gt; &lt;details&gt;   &lt;summary&gt;Release notes&lt;/summary&gt;   &lt;ul&gt;     &lt;li&gt;Version 1.0.0 Exposed CRUD operations for customer zone.&lt;/li&gt;     &lt;li&gt;Version 1.0.1 Added response body for UPDATE and CREATE record operations.&lt;/li&gt;     &lt;li&gt;Version 1.0.2 Added new supported record types.&lt;/li&gt;   &lt;/ul&gt; &lt;/details&gt; &lt;/h2&gt;   # noqa: E501
    """
)
