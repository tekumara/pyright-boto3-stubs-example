import sys
from typing import overload, Any, Union
from botocore.config import Config
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
from mypy_boto3.ec2 import EC2Client
from mypy_boto3.ec2 import EC2ServiceResource

def client(
    service_name: Literal["ec2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> EC2Client:
    pass
def resource(
    service_name: Literal["ec2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> EC2ServiceResource:
    pass