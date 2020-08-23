from typing import Any, Dict, List, Optional, TypeVar, Union

import boto3
from mypy_boto3_ec2.type_defs import FilterTypeDef

E = TypeVar("E")
T = TypeVar("T")

from mypy_boto3_ec2 import Client


def describe(config: Dict[str, Any], name: Optional[str] = None) -> List[Dict[str, Any]]:
    """List EC2 instances in the region."""

    ec2_client:Client = boto3.client("ec2", region_name=config["region"])

    filters: List[FilterTypeDef] = [] if name is None else [{"Name": "tag:Name", "Values": [name]}]
    response = ec2_client.describe_instances(Filters=filters)

    instances = [
        {
            "State": i["State"]["Name"],
            "Name": first_or_else([t["Value"] for t in i.get("Tags", []) if t["Key"] == "Name"], None),
            "Type": i["InstanceType"],
            "DnsName": i["PublicDnsName"] if i.get("PublicDnsName", None) != "" else i["PrivateDnsName"],
            "LaunchTime": i["LaunchTime"],
            "ImageId": i["ImageId"],
            "InstanceId": i["InstanceId"],
        }
        for r in response["Reservations"]
        for i in r["Instances"]
    ]

    return sorted(instances, key=lambda i: i["State"] + str(i["Name"]))


def first_or_else(li: List[E], default: T) -> Union[E, T]:
    return li[0] if len(li) > 0 else default

