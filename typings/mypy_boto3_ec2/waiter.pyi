# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for ec2 service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_ec2 import EC2Client
    from mypy_boto3_ec2.waiter import (
        BundleTaskCompleteWaiter,
        ConversionTaskCancelledWaiter,
        ConversionTaskCompletedWaiter,
        ConversionTaskDeletedWaiter,
        CustomerGatewayAvailableWaiter,
        ExportTaskCancelledWaiter,
        ExportTaskCompletedWaiter,
        ImageAvailableWaiter,
        ImageExistsWaiter,
        InstanceExistsWaiter,
        InstanceRunningWaiter,
        InstanceStatusOkWaiter,
        InstanceStoppedWaiter,
        InstanceTerminatedWaiter,
        KeyPairExistsWaiter,
        NatGatewayAvailableWaiter,
        NetworkInterfaceAvailableWaiter,
        PasswordDataAvailableWaiter,
        SecurityGroupExistsWaiter,
        SnapshotCompletedWaiter,
        SpotInstanceRequestFulfilledWaiter,
        SubnetAvailableWaiter,
        SystemStatusOkWaiter,
        VolumeAvailableWaiter,
        VolumeDeletedWaiter,
        VolumeInUseWaiter,
        VpcAvailableWaiter,
        VpcExistsWaiter,
        VpcPeeringConnectionDeletedWaiter,
        VpcPeeringConnectionExistsWaiter,
        VpnConnectionAvailableWaiter,
        VpnConnectionDeletedWaiter,
    )

    client: EC2Client = boto3.client("ec2")

    bundle_task_complete_waiter: BundleTaskCompleteWaiter = client.get_waiter("bundle_task_complete")
    conversion_task_cancelled_waiter: ConversionTaskCancelledWaiter = client.get_waiter("conversion_task_cancelled")
    conversion_task_completed_waiter: ConversionTaskCompletedWaiter = client.get_waiter("conversion_task_completed")
    conversion_task_deleted_waiter: ConversionTaskDeletedWaiter = client.get_waiter("conversion_task_deleted")
    customer_gateway_available_waiter: CustomerGatewayAvailableWaiter = client.get_waiter("customer_gateway_available")
    export_task_cancelled_waiter: ExportTaskCancelledWaiter = client.get_waiter("export_task_cancelled")
    export_task_completed_waiter: ExportTaskCompletedWaiter = client.get_waiter("export_task_completed")
    image_available_waiter: ImageAvailableWaiter = client.get_waiter("image_available")
    image_exists_waiter: ImageExistsWaiter = client.get_waiter("image_exists")
    instance_exists_waiter: InstanceExistsWaiter = client.get_waiter("instance_exists")
    instance_running_waiter: InstanceRunningWaiter = client.get_waiter("instance_running")
    instance_status_ok_waiter: InstanceStatusOkWaiter = client.get_waiter("instance_status_ok")
    instance_stopped_waiter: InstanceStoppedWaiter = client.get_waiter("instance_stopped")
    instance_terminated_waiter: InstanceTerminatedWaiter = client.get_waiter("instance_terminated")
    key_pair_exists_waiter: KeyPairExistsWaiter = client.get_waiter("key_pair_exists")
    nat_gateway_available_waiter: NatGatewayAvailableWaiter = client.get_waiter("nat_gateway_available")
    network_interface_available_waiter: NetworkInterfaceAvailableWaiter = client.get_waiter("network_interface_available")
    password_data_available_waiter: PasswordDataAvailableWaiter = client.get_waiter("password_data_available")
    security_group_exists_waiter: SecurityGroupExistsWaiter = client.get_waiter("security_group_exists")
    snapshot_completed_waiter: SnapshotCompletedWaiter = client.get_waiter("snapshot_completed")
    spot_instance_request_fulfilled_waiter: SpotInstanceRequestFulfilledWaiter = client.get_waiter("spot_instance_request_fulfilled")
    subnet_available_waiter: SubnetAvailableWaiter = client.get_waiter("subnet_available")
    system_status_ok_waiter: SystemStatusOkWaiter = client.get_waiter("system_status_ok")
    volume_available_waiter: VolumeAvailableWaiter = client.get_waiter("volume_available")
    volume_deleted_waiter: VolumeDeletedWaiter = client.get_waiter("volume_deleted")
    volume_in_use_waiter: VolumeInUseWaiter = client.get_waiter("volume_in_use")
    vpc_available_waiter: VpcAvailableWaiter = client.get_waiter("vpc_available")
    vpc_exists_waiter: VpcExistsWaiter = client.get_waiter("vpc_exists")
    vpc_peering_connection_deleted_waiter: VpcPeeringConnectionDeletedWaiter = client.get_waiter("vpc_peering_connection_deleted")
    vpc_peering_connection_exists_waiter: VpcPeeringConnectionExistsWaiter = client.get_waiter("vpc_peering_connection_exists")
    vpn_connection_available_waiter: VpnConnectionAvailableWaiter = client.get_waiter("vpn_connection_available")
    vpn_connection_deleted_waiter: VpnConnectionDeletedWaiter = client.get_waiter("vpn_connection_deleted")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_ec2.type_defs import FilterTypeDef, WaiterConfigTypeDef

__all__ = (
    "BundleTaskCompleteWaiter",
    "ConversionTaskCancelledWaiter",
    "ConversionTaskCompletedWaiter",
    "ConversionTaskDeletedWaiter",
    "CustomerGatewayAvailableWaiter",
    "ExportTaskCancelledWaiter",
    "ExportTaskCompletedWaiter",
    "ImageAvailableWaiter",
    "ImageExistsWaiter",
    "InstanceExistsWaiter",
    "InstanceRunningWaiter",
    "InstanceStatusOkWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
    "KeyPairExistsWaiter",
    "NatGatewayAvailableWaiter",
    "NetworkInterfaceAvailableWaiter",
    "PasswordDataAvailableWaiter",
    "SecurityGroupExistsWaiter",
    "SnapshotCompletedWaiter",
    "SpotInstanceRequestFulfilledWaiter",
    "SubnetAvailableWaiter",
    "SystemStatusOkWaiter",
    "VolumeAvailableWaiter",
    "VolumeDeletedWaiter",
    "VolumeInUseWaiter",
    "VpcAvailableWaiter",
    "VpcExistsWaiter",
    "VpcPeeringConnectionDeletedWaiter",
    "VpcPeeringConnectionExistsWaiter",
    "VpnConnectionAvailableWaiter",
    "VpnConnectionDeletedWaiter",
)


class BundleTaskCompleteWaiter(Boto3Waiter):
    """
    [Waiter.BundleTaskComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.BundleTaskComplete)
    """

    def wait(
        self,
        BundleIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [BundleTaskComplete.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.BundleTaskComplete.wait)
        """


class ConversionTaskCancelledWaiter(Boto3Waiter):
    """
    [Waiter.ConversionTaskCancelled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ConversionTaskCancelled)
    """

    def wait(
        self,
        ConversionTaskIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ConversionTaskCancelled.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ConversionTaskCancelled.wait)
        """


class ConversionTaskCompletedWaiter(Boto3Waiter):
    """
    [Waiter.ConversionTaskCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ConversionTaskCompleted)
    """

    def wait(
        self,
        ConversionTaskIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ConversionTaskCompleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ConversionTaskCompleted.wait)
        """


class ConversionTaskDeletedWaiter(Boto3Waiter):
    """
    [Waiter.ConversionTaskDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ConversionTaskDeleted)
    """

    def wait(
        self,
        ConversionTaskIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ConversionTaskDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ConversionTaskDeleted.wait)
        """


class CustomerGatewayAvailableWaiter(Boto3Waiter):
    """
    [Waiter.CustomerGatewayAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.CustomerGatewayAvailable)
    """

    def wait(
        self,
        CustomerGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [CustomerGatewayAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.CustomerGatewayAvailable.wait)
        """


class ExportTaskCancelledWaiter(Boto3Waiter):
    """
    [Waiter.ExportTaskCancelled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ExportTaskCancelled)
    """

    def wait(
        self,
        ExportTaskIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ExportTaskCancelled.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ExportTaskCancelled.wait)
        """


class ExportTaskCompletedWaiter(Boto3Waiter):
    """
    [Waiter.ExportTaskCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ExportTaskCompleted)
    """

    def wait(
        self,
        ExportTaskIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ExportTaskCompleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ExportTaskCompleted.wait)
        """


class ImageAvailableWaiter(Boto3Waiter):
    """
    [Waiter.ImageAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ImageAvailable)
    """

    def wait(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ImageAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ImageAvailable.wait)
        """


class ImageExistsWaiter(Boto3Waiter):
    """
    [Waiter.ImageExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ImageExists)
    """

    def wait(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [ImageExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.ImageExists.wait)
        """


class InstanceExistsWaiter(Boto3Waiter):
    """
    [Waiter.InstanceExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.InstanceExists)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.InstanceExists.wait)
        """


class InstanceRunningWaiter(Boto3Waiter):
    """
    [Waiter.InstanceRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.InstanceRunning)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceRunning.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.InstanceRunning.wait)
        """


class InstanceStatusOkWaiter(Boto3Waiter):
    """
    [Waiter.InstanceStatusOk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.InstanceStatusOk)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceStatusOk.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.InstanceStatusOk.wait)
        """


class InstanceStoppedWaiter(Boto3Waiter):
    """
    [Waiter.InstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.InstanceStopped)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceStopped.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.InstanceStopped.wait)
        """


class InstanceTerminatedWaiter(Boto3Waiter):
    """
    [Waiter.InstanceTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.InstanceTerminated)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [InstanceTerminated.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.InstanceTerminated.wait)
        """


class KeyPairExistsWaiter(Boto3Waiter):
    """
    [Waiter.KeyPairExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.KeyPairExists)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        KeyNames: List[str] = None,
        KeyPairIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [KeyPairExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.KeyPairExists.wait)
        """


class NatGatewayAvailableWaiter(Boto3Waiter):
    """
    [Waiter.NatGatewayAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.NatGatewayAvailable)
    """

    def wait(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NatGatewayIds: List[str] = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [NatGatewayAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.NatGatewayAvailable.wait)
        """


class NetworkInterfaceAvailableWaiter(Boto3Waiter):
    """
    [Waiter.NetworkInterfaceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.NetworkInterfaceAvailable)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [NetworkInterfaceAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.NetworkInterfaceAvailable.wait)
        """


class PasswordDataAvailableWaiter(Boto3Waiter):
    """
    [Waiter.PasswordDataAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.PasswordDataAvailable)
    """

    def wait(
        self, InstanceId: str, DryRun: bool = None, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [PasswordDataAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.PasswordDataAvailable.wait)
        """


class SecurityGroupExistsWaiter(Boto3Waiter):
    """
    [Waiter.SecurityGroupExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.SecurityGroupExists)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [SecurityGroupExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.SecurityGroupExists.wait)
        """


class SnapshotCompletedWaiter(Boto3Waiter):
    """
    [Waiter.SnapshotCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.SnapshotCompleted)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [SnapshotCompleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.SnapshotCompleted.wait)
        """


class SpotInstanceRequestFulfilledWaiter(Boto3Waiter):
    """
    [Waiter.SpotInstanceRequestFulfilled documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.SpotInstanceRequestFulfilled)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [SpotInstanceRequestFulfilled.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.SpotInstanceRequestFulfilled.wait)
        """


class SubnetAvailableWaiter(Boto3Waiter):
    """
    [Waiter.SubnetAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.SubnetAvailable)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [SubnetAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.SubnetAvailable.wait)
        """


class SystemStatusOkWaiter(Boto3Waiter):
    """
    [Waiter.SystemStatusOk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.SystemStatusOk)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [SystemStatusOk.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.SystemStatusOk.wait)
        """


class VolumeAvailableWaiter(Boto3Waiter):
    """
    [Waiter.VolumeAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VolumeAvailable)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [VolumeAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VolumeAvailable.wait)
        """


class VolumeDeletedWaiter(Boto3Waiter):
    """
    [Waiter.VolumeDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VolumeDeleted)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [VolumeDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VolumeDeleted.wait)
        """


class VolumeInUseWaiter(Boto3Waiter):
    """
    [Waiter.VolumeInUse documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VolumeInUse)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [VolumeInUse.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VolumeInUse.wait)
        """


class VpcAvailableWaiter(Boto3Waiter):
    """
    [Waiter.VpcAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpcAvailable)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [VpcAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpcAvailable.wait)
        """


class VpcExistsWaiter(Boto3Waiter):
    """
    [Waiter.VpcExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpcExists)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [VpcExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpcExists.wait)
        """


class VpcPeeringConnectionDeletedWaiter(Boto3Waiter):
    """
    [Waiter.VpcPeeringConnectionDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionDeleted)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [VpcPeeringConnectionDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionDeleted.wait)
        """


class VpcPeeringConnectionExistsWaiter(Boto3Waiter):
    """
    [Waiter.VpcPeeringConnectionExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionExists)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [VpcPeeringConnectionExists.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionExists.wait)
        """


class VpnConnectionAvailableWaiter(Boto3Waiter):
    """
    [Waiter.VpnConnectionAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpnConnectionAvailable)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VpnConnectionIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [VpnConnectionAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpnConnectionAvailable.wait)
        """


class VpnConnectionDeletedWaiter(Boto3Waiter):
    """
    [Waiter.VpnConnectionDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpnConnectionDeleted)
    """

    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        VpnConnectionIds: List[str] = None,
        DryRun: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [VpnConnectionDeleted.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Waiter.VpnConnectionDeleted.wait)
        """
