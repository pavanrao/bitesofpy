import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


def test_ValueError(json_file):
    with pytest.raises(ValueError) as excinfo:
        service_ranges = parse_ipv4_service_ranges(json_file)
        get_aws_service_range("256.0.0.0", service_ranges) 
    assert 'Address must be a valid IPv4 address' in str(excinfo.value) 


def test_valid(json_file):
    service_ranges = parse_ipv4_service_ranges(json_file)
    x = get_aws_service_range("35.180.0.0", service_ranges) 
    assert x == [ServiceIPRange(service='AMAZON', region='eu-west-3', cidr=IPv4Network('35.180.0.0/16')), 
    ServiceIPRange(service='EC2', region='eu-west-3', cidr=IPv4Network('35.180.0.0/16'))]
    assert str(x[0]) == '35.180.0.0/16 is allocated to the AMAZON service in the eu-west-3 region'
