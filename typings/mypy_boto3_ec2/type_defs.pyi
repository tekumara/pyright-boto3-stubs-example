"""
Main interface for ec2 service type definitions.

Usage::

    ```python
    from mypy_boto3_ec2.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountAttributeTypeDef",
    "AccountAttributeValueTypeDef",
    "ActiveInstanceTypeDef",
    "AddressTypeDef",
    "AllowedPrincipalTypeDef",
    "AssignedPrivateIpAddressTypeDef",
    "AssociatedTargetNetworkTypeDef",
    "AssociationStatusTypeDef",
    "AttributeBooleanValueTypeDef",
    "AttributeValueTypeDef",
    "AuthorizationRuleTypeDef",
    "AvailabilityZoneMessageTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableCapacityTypeDef",
    "BlockDeviceMappingTypeDef",
    "BundleTaskErrorTypeDef",
    "BundleTaskTypeDef",
    "ByoipCidrTypeDef",
    "CancelSpotFleetRequestsErrorItemTypeDef",
    "CancelSpotFleetRequestsErrorTypeDef",
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    "CancelledSpotInstanceRequestTypeDef",
    "CapacityReservationGroupTypeDef",
    "CapacityReservationOptionsRequestTypeDef",
    "CapacityReservationOptionsTypeDef",
    "CapacityReservationSpecificationResponseTypeDef",
    "CapacityReservationTargetResponseTypeDef",
    "CapacityReservationTargetTypeDef",
    "CapacityReservationTypeDef",
    "CarrierGatewayTypeDef",
    "CertificateAuthenticationRequestTypeDef",
    "CertificateAuthenticationTypeDef",
    "CidrBlockTypeDef",
    "ClassicLinkDnsSupportTypeDef",
    "ClassicLinkInstanceTypeDef",
    "ClassicLoadBalancerTypeDef",
    "ClassicLoadBalancersConfigTypeDef",
    "ClientCertificateRevocationListStatusTypeDef",
    "ClientVpnAuthenticationTypeDef",
    "ClientVpnAuthorizationRuleStatusTypeDef",
    "ClientVpnConnectionStatusTypeDef",
    "ClientVpnConnectionTypeDef",
    "ClientVpnEndpointStatusTypeDef",
    "ClientVpnEndpointTypeDef",
    "ClientVpnRouteStatusTypeDef",
    "ClientVpnRouteTypeDef",
    "CoipAddressUsageTypeDef",
    "CoipPoolTypeDef",
    "ConnectionLogResponseOptionsTypeDef",
    "ConnectionNotificationTypeDef",
    "ConversionTaskTypeDef",
    "CpuOptionsTypeDef",
    "CreateFleetErrorTypeDef",
    "CreateFleetInstanceTypeDef",
    "CreateVolumePermissionTypeDef",
    "CreditSpecificationRequestTypeDef",
    "CreditSpecificationTypeDef",
    "CustomerGatewayTypeDef",
    "DeleteFleetErrorItemTypeDef",
    "DeleteFleetErrorTypeDef",
    "DeleteFleetSuccessItemTypeDef",
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    "DeleteQueuedReservedInstancesErrorTypeDef",
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    "DescribeFleetErrorTypeDef",
    "DescribeFleetsInstancesTypeDef",
    "DhcpConfigurationTypeDef",
    "DhcpOptionsTypeDef",
    "DirectoryServiceAuthenticationRequestTypeDef",
    "DirectoryServiceAuthenticationTypeDef",
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    "DisableFastSnapshotRestoreStateErrorTypeDef",
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    "DiskImageDescriptionTypeDef",
    "DiskImageDetailTypeDef",
    "DiskImageVolumeDescriptionTypeDef",
    "DiskInfoTypeDef",
    "DnsEntryTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsInfoTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "EbsInstanceBlockDeviceTypeDef",
    "EbsOptimizedInfoTypeDef",
    "EgressOnlyInternetGatewayTypeDef",
    "ElasticGpuAssociationTypeDef",
    "ElasticGpuHealthTypeDef",
    "ElasticGpuSpecificationResponseTypeDef",
    "ElasticGpuSpecificationTypeDef",
    "ElasticGpusTypeDef",
    "ElasticInferenceAcceleratorAssociationTypeDef",
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    "EnableFastSnapshotRestoreStateErrorTypeDef",
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    "EventInformationTypeDef",
    "ExportImageTaskTypeDef",
    "ExportTaskS3LocationTypeDef",
    "ExportTaskTypeDef",
    "ExportToS3TaskTypeDef",
    "FailedQueuedPurchaseDeletionTypeDef",
    "FederatedAuthenticationRequestTypeDef",
    "FederatedAuthenticationTypeDef",
    "FleetDataTypeDef",
    "FleetLaunchTemplateConfigTypeDef",
    "FleetLaunchTemplateOverridesRequestTypeDef",
    "FleetLaunchTemplateOverridesTypeDef",
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    "FleetLaunchTemplateSpecificationTypeDef",
    "FlowLogTypeDef",
    "FpgaDeviceInfoTypeDef",
    "FpgaDeviceMemoryInfoTypeDef",
    "FpgaImageAttributeTypeDef",
    "FpgaImageStateTypeDef",
    "FpgaImageTypeDef",
    "FpgaInfoTypeDef",
    "GpuDeviceInfoTypeDef",
    "GpuDeviceMemoryInfoTypeDef",
    "GpuInfoTypeDef",
    "GroupIdentifierTypeDef",
    "HibernationOptionsTypeDef",
    "HistoryRecordEntryTypeDef",
    "HistoryRecordTypeDef",
    "HostInstanceTypeDef",
    "HostOfferingTypeDef",
    "HostPropertiesTypeDef",
    "HostReservationTypeDef",
    "HostTypeDef",
    "IKEVersionsListValueTypeDef",
    "IKEVersionsRequestListValueTypeDef",
    "IamInstanceProfileAssociationTypeDef",
    "IamInstanceProfileSpecificationTypeDef",
    "IamInstanceProfileTypeDef",
    "IcmpTypeCodeTypeDef",
    "IdFormatTypeDef",
    "ImageTypeDef",
    "ImportImageLicenseConfigurationResponseTypeDef",
    "ImportImageTaskTypeDef",
    "ImportInstanceTaskDetailsTypeDef",
    "ImportInstanceVolumeDetailItemTypeDef",
    "ImportSnapshotTaskTypeDef",
    "ImportVolumeTaskDetailsTypeDef",
    "InferenceAcceleratorInfoTypeDef",
    "InferenceDeviceInfoTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceCapacityTypeDef",
    "InstanceCountTypeDef",
    "InstanceCreditSpecificationTypeDef",
    "InstanceExportDetailsTypeDef",
    "InstanceFamilyCreditSpecificationTypeDef",
    "InstanceIpv6AddressRequestTypeDef",
    "InstanceIpv6AddressTypeDef",
    "InstanceMetadataOptionsResponseTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceNetworkInterfaceAssociationTypeDef",
    "InstanceNetworkInterfaceAttachmentTypeDef",
    "InstanceNetworkInterfaceSpecificationTypeDef",
    "InstanceNetworkInterfaceTypeDef",
    "InstancePrivateIpAddressTypeDef",
    "InstanceStateChangeTypeDef",
    "InstanceStateTypeDef",
    "InstanceStatusDetailsTypeDef",
    "InstanceStatusEventTypeDef",
    "InstanceStatusSummaryTypeDef",
    "InstanceStatusTypeDef",
    "InstanceStorageInfoTypeDef",
    "InstanceTagNotificationAttributeTypeDef",
    "InstanceTypeDef",
    "InstanceTypeInfoTypeDef",
    "InstanceTypeOfferingTypeDef",
    "InstanceUsageTypeDef",
    "InternetGatewayAttachmentTypeDef",
    "InternetGatewayTypeDef",
    "IpPermissionTypeDef",
    "IpRangeTypeDef",
    "Ipv6CidrAssociationTypeDef",
    "Ipv6CidrBlockTypeDef",
    "Ipv6PoolTypeDef",
    "Ipv6RangeTypeDef",
    "KeyPairInfoTypeDef",
    "LastErrorTypeDef",
    "LaunchPermissionTypeDef",
    "LaunchSpecificationTypeDef",
    "LaunchTemplateAndOverridesResponseTypeDef",
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    "LaunchTemplateBlockDeviceMappingTypeDef",
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    "LaunchTemplateConfigTypeDef",
    "LaunchTemplateCpuOptionsRequestTypeDef",
    "LaunchTemplateCpuOptionsTypeDef",
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    "LaunchTemplateEbsBlockDeviceTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorTypeDef",
    "LaunchTemplateHibernationOptionsRequestTypeDef",
    "LaunchTemplateHibernationOptionsTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    "LaunchTemplateLicenseConfigurationTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplatePlacementRequestTypeDef",
    "LaunchTemplatePlacementTypeDef",
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    "LaunchTemplateSpotMarketOptionsTypeDef",
    "LaunchTemplateTagSpecificationRequestTypeDef",
    "LaunchTemplateTagSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LaunchTemplateVersionTypeDef",
    "LaunchTemplatesMonitoringRequestTypeDef",
    "LaunchTemplatesMonitoringTypeDef",
    "LicenseConfigurationTypeDef",
    "LoadBalancersConfigTypeDef",
    "LoadPermissionRequestTypeDef",
    "LoadPermissionTypeDef",
    "LocalGatewayRouteTableTypeDef",
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    "LocalGatewayRouteTypeDef",
    "LocalGatewayTypeDef",
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    "LocalGatewayVirtualInterfaceTypeDef",
    "ManagedPrefixListTypeDef",
    "MemoryInfoTypeDef",
    "MonitoringTypeDef",
    "MovingAddressStatusTypeDef",
    "NatGatewayAddressTypeDef",
    "NatGatewayTypeDef",
    "NetworkAclAssociationTypeDef",
    "NetworkAclEntryTypeDef",
    "NetworkAclTypeDef",
    "NetworkInfoTypeDef",
    "NetworkInterfaceAssociationTypeDef",
    "NetworkInterfaceAttachmentTypeDef",
    "NetworkInterfaceIpv6AddressTypeDef",
    "NetworkInterfacePermissionStateTypeDef",
    "NetworkInterfacePermissionTypeDef",
    "NetworkInterfacePrivateIpAddressTypeDef",
    "NetworkInterfaceTypeDef",
    "OnDemandOptionsTypeDef",
    "PciIdTypeDef",
    "PeeringAttachmentStatusTypeDef",
    "PeeringConnectionOptionsTypeDef",
    "PeeringTgwInfoTypeDef",
    "Phase1DHGroupNumbersListValueTypeDef",
    "Phase1DHGroupNumbersRequestListValueTypeDef",
    "Phase1EncryptionAlgorithmsListValueTypeDef",
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase1IntegrityAlgorithmsListValueTypeDef",
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef",
    "Phase2DHGroupNumbersListValueTypeDef",
    "Phase2DHGroupNumbersRequestListValueTypeDef",
    "Phase2EncryptionAlgorithmsListValueTypeDef",
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase2IntegrityAlgorithmsListValueTypeDef",
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef",
    "PlacementGroupInfoTypeDef",
    "PlacementGroupTypeDef",
    "PlacementResponseTypeDef",
    "PlacementTypeDef",
    "PoolCidrBlockTypeDef",
    "PortRangeTypeDef",
    "PrefixListAssociationTypeDef",
    "PrefixListEntryTypeDef",
    "PrefixListIdTypeDef",
    "PrefixListTypeDef",
    "PriceScheduleTypeDef",
    "PricingDetailTypeDef",
    "PrincipalIdFormatTypeDef",
    "PrivateDnsNameConfigurationTypeDef",
    "PrivateIpAddressSpecificationTypeDef",
    "ProcessorInfoTypeDef",
    "ProductCodeTypeDef",
    "PropagatingVgwTypeDef",
    "ProvisionedBandwidthTypeDef",
    "PublicIpv4PoolRangeTypeDef",
    "PublicIpv4PoolTypeDef",
    "PurchaseTypeDef",
    "RecurringChargeTypeDef",
    "RegionTypeDef",
    "ReservationTypeDef",
    "ReservationValueTypeDef",
    "ReservedInstanceReservationValueTypeDef",
    "ReservedInstancesConfigurationTypeDef",
    "ReservedInstancesIdTypeDef",
    "ReservedInstancesListingTypeDef",
    "ReservedInstancesModificationResultTypeDef",
    "ReservedInstancesModificationTypeDef",
    "ReservedInstancesOfferingTypeDef",
    "ReservedInstancesTypeDef",
    "ResponseErrorTypeDef",
    "ResponseLaunchTemplateDataTypeDef",
    "RouteTableAssociationStateTypeDef",
    "RouteTableAssociationTypeDef",
    "RouteTableTypeDef",
    "RouteTypeDef",
    "RunInstancesMonitoringEnabledTypeDef",
    "S3StorageTypeDef",
    "ScheduledInstanceAvailabilityTypeDef",
    "ScheduledInstanceRecurrenceTypeDef",
    "ScheduledInstanceTypeDef",
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    "ScheduledInstancesEbsTypeDef",
    "ScheduledInstancesIamInstanceProfileTypeDef",
    "ScheduledInstancesIpv6AddressTypeDef",
    "ScheduledInstancesMonitoringTypeDef",
    "ScheduledInstancesNetworkInterfaceTypeDef",
    "ScheduledInstancesPlacementTypeDef",
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    "SecurityGroupIdentifierTypeDef",
    "SecurityGroupReferenceTypeDef",
    "SecurityGroupTypeDef",
    "ServiceConfigurationTypeDef",
    "ServiceDetailTypeDef",
    "ServiceTypeDetailTypeDef",
    "SnapshotDetailTypeDef",
    "SnapshotInfoTypeDef",
    "SnapshotTaskDetailTypeDef",
    "SnapshotTypeDef",
    "SpotDatafeedSubscriptionTypeDef",
    "SpotFleetLaunchSpecificationTypeDef",
    "SpotFleetMonitoringTypeDef",
    "SpotFleetRequestConfigDataTypeDef",
    "SpotFleetRequestConfigTypeDef",
    "SpotFleetTagSpecificationTypeDef",
    "SpotInstanceRequestTypeDef",
    "SpotInstanceStateFaultTypeDef",
    "SpotInstanceStatusTypeDef",
    "SpotMarketOptionsTypeDef",
    "SpotOptionsTypeDef",
    "SpotPlacementTypeDef",
    "SpotPriceTypeDef",
    "StaleIpPermissionTypeDef",
    "StaleSecurityGroupTypeDef",
    "StateReasonTypeDef",
    "StorageTypeDef",
    "SubnetAssociationTypeDef",
    "SubnetCidrBlockStateTypeDef",
    "SubnetIpv6CidrBlockAssociationTypeDef",
    "SubnetTypeDef",
    "SuccessfulInstanceCreditSpecificationItemTypeDef",
    "SuccessfulQueuedPurchaseDeletionTypeDef",
    "TagDescriptionTypeDef",
    "TagSpecificationTypeDef",
    "TargetCapacitySpecificationTypeDef",
    "TargetConfigurationTypeDef",
    "TargetGroupTypeDef",
    "TargetGroupsConfigTypeDef",
    "TargetNetworkTypeDef",
    "TargetReservationValueTypeDef",
    "TerminateConnectionStatusTypeDef",
    "TrafficMirrorFilterRuleTypeDef",
    "TrafficMirrorFilterTypeDef",
    "TrafficMirrorPortRangeTypeDef",
    "TrafficMirrorSessionTypeDef",
    "TrafficMirrorTargetTypeDef",
    "TransitGatewayAssociationTypeDef",
    "TransitGatewayAttachmentAssociationTypeDef",
    "TransitGatewayAttachmentPropagationTypeDef",
    "TransitGatewayAttachmentTypeDef",
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    "TransitGatewayMulticastDomainAssociationTypeDef",
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    "TransitGatewayMulticastDomainTypeDef",
    "TransitGatewayMulticastGroupTypeDef",
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    "TransitGatewayOptionsTypeDef",
    "TransitGatewayPeeringAttachmentTypeDef",
    "TransitGatewayPropagationTypeDef",
    "TransitGatewayRouteAttachmentTypeDef",
    "TransitGatewayRouteTableAssociationTypeDef",
    "TransitGatewayRouteTablePropagationTypeDef",
    "TransitGatewayRouteTableTypeDef",
    "TransitGatewayRouteTypeDef",
    "TransitGatewayTypeDef",
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    "TransitGatewayVpcAttachmentTypeDef",
    "TunnelOptionTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    "UnsuccessfulItemErrorTypeDef",
    "UnsuccessfulItemTypeDef",
    "UserBucketDetailsTypeDef",
    "UserBucketTypeDef",
    "UserDataTypeDef",
    "UserIdGroupPairTypeDef",
    "VCpuInfoTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
    "VgwTelemetryTypeDef",
    "VolumeAttachmentTypeDef",
    "VolumeDetailTypeDef",
    "VolumeModificationTypeDef",
    "VolumeStatusActionTypeDef",
    "VolumeStatusAttachmentStatusTypeDef",
    "VolumeStatusDetailsTypeDef",
    "VolumeStatusEventTypeDef",
    "VolumeStatusInfoTypeDef",
    "VolumeStatusItemTypeDef",
    "VolumeTypeDef",
    "VpcAttachmentTypeDef",
    "VpcCidrBlockAssociationTypeDef",
    "VpcCidrBlockStateTypeDef",
    "VpcClassicLinkTypeDef",
    "VpcEndpointConnectionTypeDef",
    "VpcEndpointTypeDef",
    "VpcIpv6CidrBlockAssociationTypeDef",
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    "VpcPeeringConnectionStateReasonTypeDef",
    "VpcPeeringConnectionTypeDef",
    "VpcPeeringConnectionVpcInfoTypeDef",
    "VpcTypeDef",
    "VpnConnectionOptionsTypeDef",
    "VpnConnectionTypeDef",
    "VpnGatewayTypeDef",
    "VpnStaticRouteTypeDef",
    "VpnTunnelOptionsSpecificationTypeDef",
    "AcceptReservedInstancesExchangeQuoteResultTypeDef",
    "AcceptTransitGatewayPeeringAttachmentResultTypeDef",
    "AcceptTransitGatewayVpcAttachmentResultTypeDef",
    "AcceptVpcEndpointConnectionsResultTypeDef",
    "AcceptVpcPeeringConnectionResultTypeDef",
    "AddPrefixListEntryTypeDef",
    "AdvertiseByoipCidrResultTypeDef",
    "AllocateAddressResultTypeDef",
    "AllocateHostsResultTypeDef",
    "ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef",
    "AssignIpv6AddressesResultTypeDef",
    "AssignPrivateIpAddressesResultTypeDef",
    "AssociateAddressResultTypeDef",
    "AssociateClientVpnTargetNetworkResultTypeDef",
    "AssociateIamInstanceProfileResultTypeDef",
    "AssociateRouteTableResultTypeDef",
    "AssociateSubnetCidrBlockResultTypeDef",
    "AssociateTransitGatewayMulticastDomainResultTypeDef",
    "AssociateTransitGatewayRouteTableResultTypeDef",
    "AssociateVpcCidrBlockResultTypeDef",
    "AttachClassicLinkVpcResultTypeDef",
    "AttachNetworkInterfaceResultTypeDef",
    "AttachVpnGatewayResultTypeDef",
    "AuthorizeClientVpnIngressResultTypeDef",
    "BlobAttributeValueTypeDef",
    "BundleInstanceResultTypeDef",
    "CancelBundleTaskResultTypeDef",
    "CancelCapacityReservationResultTypeDef",
    "CancelImportTaskResultTypeDef",
    "CancelReservedInstancesListingResultTypeDef",
    "CancelSpotFleetRequestsResponseTypeDef",
    "CancelSpotInstanceRequestsResultTypeDef",
    "CapacityReservationSpecificationTypeDef",
    "CidrAuthorizationContextTypeDef",
    "ClientDataTypeDef",
    "ClientVpnAuthenticationRequestTypeDef",
    "ConfirmProductInstanceResultTypeDef",
    "ConnectionLogOptionsTypeDef",
    "CopyFpgaImageResultTypeDef",
    "CopyImageResultTypeDef",
    "CopySnapshotResultTypeDef",
    "CpuOptionsRequestTypeDef",
    "CreateCapacityReservationResultTypeDef",
    "CreateCarrierGatewayResultTypeDef",
    "CreateClientVpnEndpointResultTypeDef",
    "CreateClientVpnRouteResultTypeDef",
    "CreateCustomerGatewayResultTypeDef",
    "CreateDefaultSubnetResultTypeDef",
    "CreateDefaultVpcResultTypeDef",
    "CreateDhcpOptionsResultTypeDef",
    "CreateEgressOnlyInternetGatewayResultTypeDef",
    "CreateFleetResultTypeDef",
    "CreateFlowLogsResultTypeDef",
    "CreateFpgaImageResultTypeDef",
    "CreateImageResultTypeDef",
    "CreateInstanceExportTaskResultTypeDef",
    "CreateInternetGatewayResultTypeDef",
    "CreateLaunchTemplateResultTypeDef",
    "CreateLaunchTemplateVersionResultTypeDef",
    "CreateLocalGatewayRouteResultTypeDef",
    "CreateLocalGatewayRouteTableVpcAssociationResultTypeDef",
    "CreateManagedPrefixListResultTypeDef",
    "CreateNatGatewayResultTypeDef",
    "CreateNetworkAclResultTypeDef",
    "CreateNetworkInterfacePermissionResultTypeDef",
    "CreateNetworkInterfaceResultTypeDef",
    "CreatePlacementGroupResultTypeDef",
    "CreateReservedInstancesListingResultTypeDef",
    "CreateRouteResultTypeDef",
    "CreateRouteTableResultTypeDef",
    "CreateSecurityGroupResultTypeDef",
    "CreateSnapshotsResultTypeDef",
    "CreateSpotDatafeedSubscriptionResultTypeDef",
    "CreateSubnetResultTypeDef",
    "CreateTrafficMirrorFilterResultTypeDef",
    "CreateTrafficMirrorFilterRuleResultTypeDef",
    "CreateTrafficMirrorSessionResultTypeDef",
    "CreateTrafficMirrorTargetResultTypeDef",
    "CreateTransitGatewayMulticastDomainResultTypeDef",
    "CreateTransitGatewayPeeringAttachmentResultTypeDef",
    "CreateTransitGatewayResultTypeDef",
    "CreateTransitGatewayRouteResultTypeDef",
    "CreateTransitGatewayRouteTableResultTypeDef",
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "CreateTransitGatewayVpcAttachmentResultTypeDef",
    "CreateVolumePermissionModificationsTypeDef",
    "CreateVpcEndpointConnectionNotificationResultTypeDef",
    "CreateVpcEndpointResultTypeDef",
    "CreateVpcEndpointServiceConfigurationResultTypeDef",
    "CreateVpcPeeringConnectionResultTypeDef",
    "CreateVpcResultTypeDef",
    "CreateVpnConnectionResultTypeDef",
    "CreateVpnGatewayResultTypeDef",
    "DeleteCarrierGatewayResultTypeDef",
    "DeleteClientVpnEndpointResultTypeDef",
    "DeleteClientVpnRouteResultTypeDef",
    "DeleteEgressOnlyInternetGatewayResultTypeDef",
    "DeleteFleetsResultTypeDef",
    "DeleteFlowLogsResultTypeDef",
    "DeleteFpgaImageResultTypeDef",
    "DeleteLaunchTemplateResultTypeDef",
    "DeleteLaunchTemplateVersionsResultTypeDef",
    "DeleteLocalGatewayRouteResultTypeDef",
    "DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef",
    "DeleteManagedPrefixListResultTypeDef",
    "DeleteNatGatewayResultTypeDef",
    "DeleteNetworkInterfacePermissionResultTypeDef",
    "DeleteQueuedReservedInstancesResultTypeDef",
    "DeleteTrafficMirrorFilterResultTypeDef",
    "DeleteTrafficMirrorFilterRuleResultTypeDef",
    "DeleteTrafficMirrorSessionResultTypeDef",
    "DeleteTrafficMirrorTargetResultTypeDef",
    "DeleteTransitGatewayMulticastDomainResultTypeDef",
    "DeleteTransitGatewayPeeringAttachmentResultTypeDef",
    "DeleteTransitGatewayResultTypeDef",
    "DeleteTransitGatewayRouteResultTypeDef",
    "DeleteTransitGatewayRouteTableResultTypeDef",
    "DeleteTransitGatewayVpcAttachmentResultTypeDef",
    "DeleteVpcEndpointConnectionNotificationsResultTypeDef",
    "DeleteVpcEndpointServiceConfigurationsResultTypeDef",
    "DeleteVpcEndpointsResultTypeDef",
    "DeleteVpcPeeringConnectionResultTypeDef",
    "DeprovisionByoipCidrResultTypeDef",
    "DeregisterInstanceEventNotificationAttributesResultTypeDef",
    "DeregisterInstanceTagAttributeRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupMembersResultTypeDef",
    "DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeAggregateIdFormatResultTypeDef",
    "DescribeAvailabilityZonesResultTypeDef",
    "DescribeBundleTasksResultTypeDef",
    "DescribeByoipCidrsResultTypeDef",
    "DescribeCapacityReservationsResultTypeDef",
    "DescribeCarrierGatewaysResultTypeDef",
    "DescribeClassicLinkInstancesResultTypeDef",
    "DescribeClientVpnAuthorizationRulesResultTypeDef",
    "DescribeClientVpnConnectionsResultTypeDef",
    "DescribeClientVpnEndpointsResultTypeDef",
    "DescribeClientVpnRoutesResultTypeDef",
    "DescribeClientVpnTargetNetworksResultTypeDef",
    "DescribeCoipPoolsResultTypeDef",
    "DescribeConversionTasksResultTypeDef",
    "DescribeCustomerGatewaysResultTypeDef",
    "DescribeDhcpOptionsResultTypeDef",
    "DescribeEgressOnlyInternetGatewaysResultTypeDef",
    "DescribeElasticGpusResultTypeDef",
    "DescribeExportImageTasksResultTypeDef",
    "DescribeExportTasksResultTypeDef",
    "DescribeFastSnapshotRestoresResultTypeDef",
    "DescribeFleetHistoryResultTypeDef",
    "DescribeFleetInstancesResultTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeFlowLogsResultTypeDef",
    "DescribeFpgaImageAttributeResultTypeDef",
    "DescribeFpgaImagesResultTypeDef",
    "DescribeHostReservationOfferingsResultTypeDef",
    "DescribeHostReservationsResultTypeDef",
    "DescribeHostsResultTypeDef",
    "DescribeIamInstanceProfileAssociationsResultTypeDef",
    "DescribeIdFormatResultTypeDef",
    "DescribeIdentityIdFormatResultTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeImportImageTasksResultTypeDef",
    "DescribeImportSnapshotTasksResultTypeDef",
    "DescribeInstanceCreditSpecificationsResultTypeDef",
    "DescribeInstanceEventNotificationAttributesResultTypeDef",
    "DescribeInstanceStatusResultTypeDef",
    "DescribeInstanceTypeOfferingsResultTypeDef",
    "DescribeInstanceTypesResultTypeDef",
    "DescribeInstancesResultTypeDef",
    "DescribeInternetGatewaysResultTypeDef",
    "DescribeIpv6PoolsResultTypeDef",
    "DescribeKeyPairsResultTypeDef",
    "DescribeLaunchTemplateVersionsResultTypeDef",
    "DescribeLaunchTemplatesResultTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef",
    "DescribeLocalGatewayRouteTablesResultTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef",
    "DescribeLocalGatewayVirtualInterfacesResultTypeDef",
    "DescribeLocalGatewaysResultTypeDef",
    "DescribeManagedPrefixListsResultTypeDef",
    "DescribeMovingAddressesResultTypeDef",
    "DescribeNatGatewaysResultTypeDef",
    "DescribeNetworkAclsResultTypeDef",
    "DescribeNetworkInterfaceAttributeResultTypeDef",
    "DescribeNetworkInterfacePermissionsResultTypeDef",
    "DescribeNetworkInterfacesResultTypeDef",
    "DescribePlacementGroupsResultTypeDef",
    "DescribePrefixListsResultTypeDef",
    "DescribePrincipalIdFormatResultTypeDef",
    "DescribePublicIpv4PoolsResultTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeReservedInstancesListingsResultTypeDef",
    "DescribeReservedInstancesModificationsResultTypeDef",
    "DescribeReservedInstancesOfferingsResultTypeDef",
    "DescribeReservedInstancesResultTypeDef",
    "DescribeRouteTablesResultTypeDef",
    "DescribeScheduledInstanceAvailabilityResultTypeDef",
    "DescribeScheduledInstancesResultTypeDef",
    "DescribeSecurityGroupReferencesResultTypeDef",
    "DescribeSecurityGroupsResultTypeDef",
    "DescribeSnapshotAttributeResultTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeSpotDatafeedSubscriptionResultTypeDef",
    "DescribeSpotFleetInstancesResponseTypeDef",
    "DescribeSpotFleetRequestHistoryResponseTypeDef",
    "DescribeSpotFleetRequestsResponseTypeDef",
    "DescribeSpotInstanceRequestsResultTypeDef",
    "DescribeSpotPriceHistoryResultTypeDef",
    "DescribeStaleSecurityGroupsResultTypeDef",
    "DescribeSubnetsResultTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeTrafficMirrorFiltersResultTypeDef",
    "DescribeTrafficMirrorSessionsResultTypeDef",
    "DescribeTrafficMirrorTargetsResultTypeDef",
    "DescribeTransitGatewayAttachmentsResultTypeDef",
    "DescribeTransitGatewayMulticastDomainsResultTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsResultTypeDef",
    "DescribeTransitGatewayRouteTablesResultTypeDef",
    "DescribeTransitGatewayVpcAttachmentsResultTypeDef",
    "DescribeTransitGatewaysResultTypeDef",
    "DescribeVolumeAttributeResultTypeDef",
    "DescribeVolumeStatusResultTypeDef",
    "DescribeVolumesModificationsResultTypeDef",
    "DescribeVolumesResultTypeDef",
    "DescribeVpcAttributeResultTypeDef",
    "DescribeVpcClassicLinkDnsSupportResultTypeDef",
    "DescribeVpcClassicLinkResultTypeDef",
    "DescribeVpcEndpointConnectionNotificationsResultTypeDef",
    "DescribeVpcEndpointConnectionsResultTypeDef",
    "DescribeVpcEndpointServiceConfigurationsResultTypeDef",
    "DescribeVpcEndpointServicePermissionsResultTypeDef",
    "DescribeVpcEndpointServicesResultTypeDef",
    "DescribeVpcEndpointsResultTypeDef",
    "DescribeVpcPeeringConnectionsResultTypeDef",
    "DescribeVpcsResultTypeDef",
    "DescribeVpnConnectionsResultTypeDef",
    "DescribeVpnGatewaysResultTypeDef",
    "DetachClassicLinkVpcResultTypeDef",
    "DisableEbsEncryptionByDefaultResultTypeDef",
    "DisableFastSnapshotRestoresResultTypeDef",
    "DisableTransitGatewayRouteTablePropagationResultTypeDef",
    "DisableVpcClassicLinkDnsSupportResultTypeDef",
    "DisableVpcClassicLinkResultTypeDef",
    "DisassociateClientVpnTargetNetworkResultTypeDef",
    "DisassociateIamInstanceProfileResultTypeDef",
    "DisassociateSubnetCidrBlockResultTypeDef",
    "DisassociateTransitGatewayMulticastDomainResultTypeDef",
    "DisassociateTransitGatewayRouteTableResultTypeDef",
    "DisassociateVpcCidrBlockResultTypeDef",
    "DiskImageTypeDef",
    "DnsServersOptionsModifyStructureTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "EnableEbsEncryptionByDefaultResultTypeDef",
    "EnableFastSnapshotRestoresResultTypeDef",
    "EnableTransitGatewayRouteTablePropagationResultTypeDef",
    "EnableVpcClassicLinkDnsSupportResultTypeDef",
    "EnableVpcClassicLinkResultTypeDef",
    "ExportClientVpnClientCertificateRevocationListResultTypeDef",
    "ExportClientVpnClientConfigurationResultTypeDef",
    "ExportImageResultTypeDef",
    "ExportTaskS3LocationRequestTypeDef",
    "ExportToS3TaskSpecificationTypeDef",
    "ExportTransitGatewayRoutesResultTypeDef",
    "FilterTypeDef",
    "FleetLaunchTemplateConfigRequestTypeDef",
    "GetAssociatedIpv6PoolCidrsResultTypeDef",
    "GetCapacityReservationUsageResultTypeDef",
    "GetCoipPoolUsageResultTypeDef",
    "GetConsoleOutputResultTypeDef",
    "GetConsoleScreenshotResultTypeDef",
    "GetDefaultCreditSpecificationResultTypeDef",
    "GetEbsDefaultKmsKeyIdResultTypeDef",
    "GetEbsEncryptionByDefaultResultTypeDef",
    "GetGroupsForCapacityReservationResultTypeDef",
    "GetHostReservationPurchasePreviewResultTypeDef",
    "GetLaunchTemplateDataResultTypeDef",
    "GetManagedPrefixListAssociationsResultTypeDef",
    "GetManagedPrefixListEntriesResultTypeDef",
    "GetPasswordDataResultTypeDef",
    "GetReservedInstancesExchangeQuoteResultTypeDef",
    "GetTransitGatewayAttachmentPropagationsResultTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "GetTransitGatewayRouteTableAssociationsResultTypeDef",
    "GetTransitGatewayRouteTablePropagationsResultTypeDef",
    "HibernationOptionsRequestTypeDef",
    "ImageAttributeTypeDef",
    "ImageDiskContainerTypeDef",
    "ImportClientVpnClientCertificateRevocationListResultTypeDef",
    "ImportImageLicenseConfigurationRequestTypeDef",
    "ImportImageResultTypeDef",
    "ImportInstanceLaunchSpecificationTypeDef",
    "ImportInstanceResultTypeDef",
    "ImportKeyPairResultTypeDef",
    "ImportSnapshotResultTypeDef",
    "ImportVolumeResultTypeDef",
    "InstanceAttributeTypeDef",
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    "InstanceCreditSpecificationRequestTypeDef",
    "InstanceMarketOptionsRequestTypeDef",
    "InstanceMetadataOptionsRequestTypeDef",
    "InstanceSpecificationTypeDef",
    "KeyPairTypeDef",
    "LaunchPermissionModificationsTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LicenseConfigurationRequestTypeDef",
    "LoadPermissionModificationsTypeDef",
    "ModifyAvailabilityZoneGroupResultTypeDef",
    "ModifyCapacityReservationResultTypeDef",
    "ModifyClientVpnEndpointResultTypeDef",
    "ModifyDefaultCreditSpecificationResultTypeDef",
    "ModifyEbsDefaultKmsKeyIdResultTypeDef",
    "ModifyFleetResultTypeDef",
    "ModifyFpgaImageAttributeResultTypeDef",
    "ModifyHostsResultTypeDef",
    "ModifyInstanceCapacityReservationAttributesResultTypeDef",
    "ModifyInstanceCreditSpecificationResultTypeDef",
    "ModifyInstanceEventStartTimeResultTypeDef",
    "ModifyInstanceMetadataOptionsResultTypeDef",
    "ModifyInstancePlacementResultTypeDef",
    "ModifyLaunchTemplateResultTypeDef",
    "ModifyManagedPrefixListResultTypeDef",
    "ModifyReservedInstancesResultTypeDef",
    "ModifySpotFleetRequestResponseTypeDef",
    "ModifyTrafficMirrorFilterNetworkServicesResultTypeDef",
    "ModifyTrafficMirrorFilterRuleResultTypeDef",
    "ModifyTrafficMirrorSessionResultTypeDef",
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "ModifyTransitGatewayVpcAttachmentResultTypeDef",
    "ModifyVolumeResultTypeDef",
    "ModifyVpcEndpointConnectionNotificationResultTypeDef",
    "ModifyVpcEndpointResultTypeDef",
    "ModifyVpcEndpointServiceConfigurationResultTypeDef",
    "ModifyVpcEndpointServicePermissionsResultTypeDef",
    "ModifyVpcPeeringConnectionOptionsResultTypeDef",
    "ModifyVpcTenancyResultTypeDef",
    "ModifyVpnConnectionResultTypeDef",
    "ModifyVpnTunnelCertificateResultTypeDef",
    "ModifyVpnTunnelOptionsResultTypeDef",
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    "MonitorInstancesResultTypeDef",
    "MoveAddressToVpcResultTypeDef",
    "NetworkInterfaceAttachmentChangesTypeDef",
    "NewDhcpConfigurationTypeDef",
    "OnDemandOptionsRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PeeringConnectionOptionsRequestTypeDef",
    "PriceScheduleSpecificationTypeDef",
    "ProvisionByoipCidrResultTypeDef",
    "PurchaseHostReservationResultTypeDef",
    "PurchaseRequestTypeDef",
    "PurchaseReservedInstancesOfferingResultTypeDef",
    "PurchaseScheduledInstancesResultTypeDef",
    "RegisterImageResultTypeDef",
    "RegisterInstanceEventNotificationAttributesResultTypeDef",
    "RegisterInstanceTagAttributeRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupMembersResultTypeDef",
    "RegisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    "RejectTransitGatewayPeeringAttachmentResultTypeDef",
    "RejectTransitGatewayVpcAttachmentResultTypeDef",
    "RejectVpcEndpointConnectionsResultTypeDef",
    "RejectVpcPeeringConnectionResultTypeDef",
    "ReleaseHostsResultTypeDef",
    "RemovePrefixListEntryTypeDef",
    "ReplaceIamInstanceProfileAssociationResultTypeDef",
    "ReplaceNetworkAclAssociationResultTypeDef",
    "ReplaceRouteTableAssociationResultTypeDef",
    "ReplaceTransitGatewayRouteResultTypeDef",
    "RequestLaunchTemplateDataTypeDef",
    "RequestSpotFleetResponseTypeDef",
    "RequestSpotInstancesResultTypeDef",
    "RequestSpotLaunchSpecificationTypeDef",
    "ReservedInstanceLimitPriceTypeDef",
    "ResetEbsDefaultKmsKeyIdResultTypeDef",
    "ResetFpgaImageAttributeResultTypeDef",
    "RestoreAddressToClassicResultTypeDef",
    "RestoreManagedPrefixListVersionResultTypeDef",
    "RevokeClientVpnIngressResultTypeDef",
    "RunScheduledInstancesResultTypeDef",
    "ScheduledInstanceRecurrenceRequestTypeDef",
    "ScheduledInstancesLaunchSpecificationTypeDef",
    "SearchLocalGatewayRoutesResultTypeDef",
    "SearchTransitGatewayMulticastGroupsResultTypeDef",
    "SearchTransitGatewayRoutesResultTypeDef",
    "SlotDateTimeRangeRequestTypeDef",
    "SlotStartTimeRangeRequestTypeDef",
    "SnapshotDiskContainerTypeDef",
    "SpotOptionsRequestTypeDef",
    "StartInstancesResultTypeDef",
    "StartVpcEndpointServicePrivateDnsVerificationResultTypeDef",
    "StopInstancesResultTypeDef",
    "StorageLocationTypeDef",
    "TagTypeDef",
    "TargetCapacitySpecificationRequestTypeDef",
    "TargetConfigurationRequestTypeDef",
    "TerminateClientVpnConnectionsResultTypeDef",
    "TerminateInstancesResultTypeDef",
    "TrafficMirrorPortRangeRequestTypeDef",
    "TransitGatewayRequestOptionsTypeDef",
    "UnassignIpv6AddressesResultTypeDef",
    "UnmonitorInstancesResultTypeDef",
    "UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef",
    "UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef",
    "VpnConnectionOptionsSpecificationTypeDef",
    "WaiterConfigTypeDef",
    "WithdrawByoipCidrResultTypeDef",
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {"AttributeName": str, "AttributeValues": List["AccountAttributeValueTypeDef"]},
    total=False,
)

AccountAttributeValueTypeDef = TypedDict(
    "AccountAttributeValueTypeDef", {"AttributeValue": str}, total=False
)

ActiveInstanceTypeDef = TypedDict(
    "ActiveInstanceTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "SpotInstanceRequestId": str,
        "InstanceHealth": Literal["healthy", "unhealthy"],
    },
    total=False,
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "InstanceId": str,
        "PublicIp": str,
        "AllocationId": str,
        "AssociationId": str,
        "Domain": Literal["vpc", "standard"],
        "NetworkInterfaceId": str,
        "NetworkInterfaceOwnerId": str,
        "PrivateIpAddress": str,
        "Tags": List["TagTypeDef"],
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "CustomerOwnedIp": str,
        "CustomerOwnedIpv4Pool": str,
        "CarrierIp": str,
    },
    total=False,
)

AllowedPrincipalTypeDef = TypedDict(
    "AllowedPrincipalTypeDef",
    {
        "PrincipalType": Literal["All", "Service", "OrganizationUnit", "Account", "User", "Role"],
        "Principal": str,
    },
    total=False,
)

AssignedPrivateIpAddressTypeDef = TypedDict(
    "AssignedPrivateIpAddressTypeDef", {"PrivateIpAddress": str}, total=False
)

AssociatedTargetNetworkTypeDef = TypedDict(
    "AssociatedTargetNetworkTypeDef", {"NetworkId": str, "NetworkType": Literal["vpc"]}, total=False
)

AssociationStatusTypeDef = TypedDict(
    "AssociationStatusTypeDef",
    {
        "Code": Literal[
            "associating", "associated", "association-failed", "disassociating", "disassociated"
        ],
        "Message": str,
    },
    total=False,
)

AttributeBooleanValueTypeDef = TypedDict(
    "AttributeBooleanValueTypeDef", {"Value": bool}, total=False
)

AttributeValueTypeDef = TypedDict("AttributeValueTypeDef", {"Value": str}, total=False)

AuthorizationRuleTypeDef = TypedDict(
    "AuthorizationRuleTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Description": str,
        "GroupId": str,
        "AccessAll": bool,
        "DestinationCidr": str,
        "Status": "ClientVpnAuthorizationRuleStatusTypeDef",
    },
    total=False,
)

AvailabilityZoneMessageTypeDef = TypedDict(
    "AvailabilityZoneMessageTypeDef", {"Message": str}, total=False
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "State": Literal["available", "information", "impaired", "unavailable"],
        "OptInStatus": Literal["opt-in-not-required", "opted-in", "not-opted-in"],
        "Messages": List["AvailabilityZoneMessageTypeDef"],
        "RegionName": str,
        "ZoneName": str,
        "ZoneId": str,
        "GroupName": str,
        "NetworkBorderGroup": str,
        "ZoneType": str,
        "ParentZoneName": str,
        "ParentZoneId": str,
    },
    total=False,
)

AvailableCapacityTypeDef = TypedDict(
    "AvailableCapacityTypeDef",
    {"AvailableInstanceCapacity": List["InstanceCapacityTypeDef"], "AvailableVCpus": int},
    total=False,
)

BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {"DeviceName": str, "VirtualName": str, "Ebs": "EbsBlockDeviceTypeDef", "NoDevice": str},
    total=False,
)

BundleTaskErrorTypeDef = TypedDict(
    "BundleTaskErrorTypeDef", {"Code": str, "Message": str}, total=False
)

BundleTaskTypeDef = TypedDict(
    "BundleTaskTypeDef",
    {
        "BundleId": str,
        "BundleTaskError": "BundleTaskErrorTypeDef",
        "InstanceId": str,
        "Progress": str,
        "StartTime": datetime,
        "State": Literal[
            "pending",
            "waiting-for-shutdown",
            "bundling",
            "storing",
            "cancelling",
            "complete",
            "failed",
        ],
        "Storage": "StorageTypeDef",
        "UpdateTime": datetime,
    },
    total=False,
)

ByoipCidrTypeDef = TypedDict(
    "ByoipCidrTypeDef",
    {
        "Cidr": str,
        "Description": str,
        "StatusMessage": str,
        "State": Literal[
            "advertised",
            "deprovisioned",
            "failed-deprovision",
            "failed-provision",
            "pending-deprovision",
            "pending-provision",
            "provisioned",
            "provisioned-not-publicly-advertisable",
        ],
    },
    total=False,
)

CancelSpotFleetRequestsErrorItemTypeDef = TypedDict(
    "CancelSpotFleetRequestsErrorItemTypeDef",
    {"Error": "CancelSpotFleetRequestsErrorTypeDef", "SpotFleetRequestId": str},
    total=False,
)

CancelSpotFleetRequestsErrorTypeDef = TypedDict(
    "CancelSpotFleetRequestsErrorTypeDef",
    {
        "Code": Literal[
            "fleetRequestIdDoesNotExist",
            "fleetRequestIdMalformed",
            "fleetRequestNotInCancellableState",
            "unexpectedError",
        ],
        "Message": str,
    },
    total=False,
)

CancelSpotFleetRequestsSuccessItemTypeDef = TypedDict(
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    {
        "CurrentSpotFleetRequestState": Literal[
            "submitted",
            "active",
            "cancelled",
            "failed",
            "cancelled_running",
            "cancelled_terminating",
            "modifying",
        ],
        "PreviousSpotFleetRequestState": Literal[
            "submitted",
            "active",
            "cancelled",
            "failed",
            "cancelled_running",
            "cancelled_terminating",
            "modifying",
        ],
        "SpotFleetRequestId": str,
    },
    total=False,
)

CancelledSpotInstanceRequestTypeDef = TypedDict(
    "CancelledSpotInstanceRequestTypeDef",
    {
        "SpotInstanceRequestId": str,
        "State": Literal["active", "open", "closed", "cancelled", "completed"],
    },
    total=False,
)

CapacityReservationGroupTypeDef = TypedDict(
    "CapacityReservationGroupTypeDef", {"GroupArn": str, "OwnerId": str}, total=False
)

CapacityReservationOptionsRequestTypeDef = TypedDict(
    "CapacityReservationOptionsRequestTypeDef",
    {"UsageStrategy": Literal["use-capacity-reservations-first"]},
    total=False,
)

CapacityReservationOptionsTypeDef = TypedDict(
    "CapacityReservationOptionsTypeDef",
    {"UsageStrategy": Literal["use-capacity-reservations-first"]},
    total=False,
)

CapacityReservationSpecificationResponseTypeDef = TypedDict(
    "CapacityReservationSpecificationResponseTypeDef",
    {
        "CapacityReservationPreference": Literal["open", "none"],
        "CapacityReservationTarget": "CapacityReservationTargetResponseTypeDef",
    },
    total=False,
)

CapacityReservationTargetResponseTypeDef = TypedDict(
    "CapacityReservationTargetResponseTypeDef",
    {"CapacityReservationId": str, "CapacityReservationResourceGroupArn": str},
    total=False,
)

CapacityReservationTargetTypeDef = TypedDict(
    "CapacityReservationTargetTypeDef",
    {"CapacityReservationId": str, "CapacityReservationResourceGroupArn": str},
    total=False,
)

CapacityReservationTypeDef = TypedDict(
    "CapacityReservationTypeDef",
    {
        "CapacityReservationId": str,
        "OwnerId": str,
        "CapacityReservationArn": str,
        "AvailabilityZoneId": str,
        "InstanceType": str,
        "InstancePlatform": Literal[
            "Linux/UNIX",
            "Red Hat Enterprise Linux",
            "SUSE Linux",
            "Windows",
            "Windows with SQL Server",
            "Windows with SQL Server Enterprise",
            "Windows with SQL Server Standard",
            "Windows with SQL Server Web",
            "Linux with SQL Server Standard",
            "Linux with SQL Server Web",
            "Linux with SQL Server Enterprise",
        ],
        "AvailabilityZone": str,
        "Tenancy": Literal["default", "dedicated"],
        "TotalInstanceCount": int,
        "AvailableInstanceCount": int,
        "EbsOptimized": bool,
        "EphemeralStorage": bool,
        "State": Literal["active", "expired", "cancelled", "pending", "failed"],
        "EndDate": datetime,
        "EndDateType": Literal["unlimited", "limited"],
        "InstanceMatchCriteria": Literal["open", "targeted"],
        "CreateDate": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CarrierGatewayTypeDef = TypedDict(
    "CarrierGatewayTypeDef",
    {
        "CarrierGatewayId": str,
        "VpcId": str,
        "State": Literal["pending", "available", "deleting", "deleted"],
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CertificateAuthenticationRequestTypeDef = TypedDict(
    "CertificateAuthenticationRequestTypeDef", {"ClientRootCertificateChainArn": str}, total=False
)

CertificateAuthenticationTypeDef = TypedDict(
    "CertificateAuthenticationTypeDef", {"ClientRootCertificateChain": str}, total=False
)

CidrBlockTypeDef = TypedDict("CidrBlockTypeDef", {"CidrBlock": str}, total=False)

ClassicLinkDnsSupportTypeDef = TypedDict(
    "ClassicLinkDnsSupportTypeDef", {"ClassicLinkDnsSupported": bool, "VpcId": str}, total=False
)

ClassicLinkInstanceTypeDef = TypedDict(
    "ClassicLinkInstanceTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "InstanceId": str,
        "Tags": List["TagTypeDef"],
        "VpcId": str,
    },
    total=False,
)

ClassicLoadBalancerTypeDef = TypedDict("ClassicLoadBalancerTypeDef", {"Name": str}, total=False)

ClassicLoadBalancersConfigTypeDef = TypedDict(
    "ClassicLoadBalancersConfigTypeDef",
    {"ClassicLoadBalancers": List["ClassicLoadBalancerTypeDef"]},
    total=False,
)

ClientCertificateRevocationListStatusTypeDef = TypedDict(
    "ClientCertificateRevocationListStatusTypeDef",
    {"Code": Literal["pending", "active"], "Message": str},
    total=False,
)

ClientVpnAuthenticationTypeDef = TypedDict(
    "ClientVpnAuthenticationTypeDef",
    {
        "Type": Literal[
            "certificate-authentication",
            "directory-service-authentication",
            "federated-authentication",
        ],
        "ActiveDirectory": "DirectoryServiceAuthenticationTypeDef",
        "MutualAuthentication": "CertificateAuthenticationTypeDef",
        "FederatedAuthentication": "FederatedAuthenticationTypeDef",
    },
    total=False,
)

ClientVpnAuthorizationRuleStatusTypeDef = TypedDict(
    "ClientVpnAuthorizationRuleStatusTypeDef",
    {"Code": Literal["authorizing", "active", "failed", "revoking"], "Message": str},
    total=False,
)

ClientVpnConnectionStatusTypeDef = TypedDict(
    "ClientVpnConnectionStatusTypeDef",
    {"Code": Literal["active", "failed-to-terminate", "terminating", "terminated"], "Message": str},
    total=False,
)

ClientVpnConnectionTypeDef = TypedDict(
    "ClientVpnConnectionTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Timestamp": str,
        "ConnectionId": str,
        "Username": str,
        "ConnectionEstablishedTime": str,
        "IngressBytes": str,
        "EgressBytes": str,
        "IngressPackets": str,
        "EgressPackets": str,
        "ClientIp": str,
        "CommonName": str,
        "Status": "ClientVpnConnectionStatusTypeDef",
        "ConnectionEndTime": str,
    },
    total=False,
)

ClientVpnEndpointStatusTypeDef = TypedDict(
    "ClientVpnEndpointStatusTypeDef",
    {"Code": Literal["pending-associate", "available", "deleting", "deleted"], "Message": str},
    total=False,
)

ClientVpnEndpointTypeDef = TypedDict(
    "ClientVpnEndpointTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Description": str,
        "Status": "ClientVpnEndpointStatusTypeDef",
        "CreationTime": str,
        "DeletionTime": str,
        "DnsName": str,
        "ClientCidrBlock": str,
        "DnsServers": List[str],
        "SplitTunnel": bool,
        "VpnProtocol": Literal["openvpn"],
        "TransportProtocol": Literal["tcp", "udp"],
        "VpnPort": int,
        "AssociatedTargetNetworks": List["AssociatedTargetNetworkTypeDef"],
        "ServerCertificateArn": str,
        "AuthenticationOptions": List["ClientVpnAuthenticationTypeDef"],
        "ConnectionLogOptions": "ConnectionLogResponseOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "SecurityGroupIds": List[str],
        "VpcId": str,
    },
    total=False,
)

ClientVpnRouteStatusTypeDef = TypedDict(
    "ClientVpnRouteStatusTypeDef",
    {"Code": Literal["creating", "active", "failed", "deleting"], "Message": str},
    total=False,
)

ClientVpnRouteTypeDef = TypedDict(
    "ClientVpnRouteTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidr": str,
        "TargetSubnet": str,
        "Type": str,
        "Origin": str,
        "Status": "ClientVpnRouteStatusTypeDef",
        "Description": str,
    },
    total=False,
)

CoipAddressUsageTypeDef = TypedDict(
    "CoipAddressUsageTypeDef",
    {"AllocationId": str, "AwsAccountId": str, "AwsService": str, "CoIp": str},
    total=False,
)

CoipPoolTypeDef = TypedDict(
    "CoipPoolTypeDef",
    {
        "PoolId": str,
        "PoolCidrs": List[str],
        "LocalGatewayRouteTableId": str,
        "Tags": List["TagTypeDef"],
        "PoolArn": str,
    },
    total=False,
)

ConnectionLogResponseOptionsTypeDef = TypedDict(
    "ConnectionLogResponseOptionsTypeDef",
    {"Enabled": bool, "CloudwatchLogGroup": str, "CloudwatchLogStream": str},
    total=False,
)

ConnectionNotificationTypeDef = TypedDict(
    "ConnectionNotificationTypeDef",
    {
        "ConnectionNotificationId": str,
        "ServiceId": str,
        "VpcEndpointId": str,
        "ConnectionNotificationType": Literal["Topic"],
        "ConnectionNotificationArn": str,
        "ConnectionEvents": List[str],
        "ConnectionNotificationState": Literal["Enabled", "Disabled"],
    },
    total=False,
)

ConversionTaskTypeDef = TypedDict(
    "ConversionTaskTypeDef",
    {
        "ConversionTaskId": str,
        "ExpirationTime": str,
        "ImportInstance": "ImportInstanceTaskDetailsTypeDef",
        "ImportVolume": "ImportVolumeTaskDetailsTypeDef",
        "State": Literal["active", "cancelling", "cancelled", "completed"],
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CpuOptionsTypeDef = TypedDict(
    "CpuOptionsTypeDef", {"CoreCount": int, "ThreadsPerCore": int}, total=False
)

CreateFleetErrorTypeDef = TypedDict(
    "CreateFleetErrorTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": Literal["spot", "on-demand"],
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

CreateFleetInstanceTypeDef = TypedDict(
    "CreateFleetInstanceTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": Literal["spot", "on-demand"],
        "InstanceIds": List[str],
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "Platform": Literal["Windows"],
    },
    total=False,
)

CreateVolumePermissionTypeDef = TypedDict(
    "CreateVolumePermissionTypeDef", {"Group": Literal["all"], "UserId": str}, total=False
)

CreditSpecificationRequestTypeDef = TypedDict(
    "CreditSpecificationRequestTypeDef", {"CpuCredits": str}
)

CreditSpecificationTypeDef = TypedDict(
    "CreditSpecificationTypeDef", {"CpuCredits": str}, total=False
)

CustomerGatewayTypeDef = TypedDict(
    "CustomerGatewayTypeDef",
    {
        "BgpAsn": str,
        "CustomerGatewayId": str,
        "IpAddress": str,
        "CertificateArn": str,
        "State": str,
        "Type": str,
        "DeviceName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

DeleteFleetErrorItemTypeDef = TypedDict(
    "DeleteFleetErrorItemTypeDef", {"Error": "DeleteFleetErrorTypeDef", "FleetId": str}, total=False
)

DeleteFleetErrorTypeDef = TypedDict(
    "DeleteFleetErrorTypeDef",
    {
        "Code": Literal[
            "fleetIdDoesNotExist", "fleetIdMalformed", "fleetNotInDeletableState", "unexpectedError"
        ],
        "Message": str,
    },
    total=False,
)

DeleteFleetSuccessItemTypeDef = TypedDict(
    "DeleteFleetSuccessItemTypeDef",
    {
        "CurrentFleetState": Literal[
            "submitted",
            "active",
            "deleted",
            "failed",
            "deleted_running",
            "deleted_terminating",
            "modifying",
        ],
        "PreviousFleetState": Literal[
            "submitted",
            "active",
            "deleted",
            "failed",
            "deleted_running",
            "deleted_terminating",
            "modifying",
        ],
        "FleetId": str,
    },
    total=False,
)

DeleteLaunchTemplateVersionsResponseErrorItemTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "VersionNumber": int,
        "ResponseError": "ResponseErrorTypeDef",
    },
    total=False,
)

DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "VersionNumber": int},
    total=False,
)

DeleteQueuedReservedInstancesErrorTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesErrorTypeDef",
    {
        "Code": Literal[
            "reserved-instances-id-invalid",
            "reserved-instances-not-in-queued-state",
            "unexpected-error",
        ],
        "Message": str,
    },
    total=False,
)

DescribeFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": str,
        "AvailabilityZone": str,
        "State": Literal["enabling", "optimizing", "enabled", "disabling", "disabled"],
        "StateTransitionReason": str,
        "OwnerId": str,
        "OwnerAlias": str,
        "EnablingTime": datetime,
        "OptimizingTime": datetime,
        "EnabledTime": datetime,
        "DisablingTime": datetime,
        "DisabledTime": datetime,
    },
    total=False,
)

DescribeFleetErrorTypeDef = TypedDict(
    "DescribeFleetErrorTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": Literal["spot", "on-demand"],
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

DescribeFleetsInstancesTypeDef = TypedDict(
    "DescribeFleetsInstancesTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": Literal["spot", "on-demand"],
        "InstanceIds": List[str],
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "Platform": Literal["Windows"],
    },
    total=False,
)

DhcpConfigurationTypeDef = TypedDict(
    "DhcpConfigurationTypeDef", {"Key": str, "Values": List["AttributeValueTypeDef"]}, total=False
)

DhcpOptionsTypeDef = TypedDict(
    "DhcpOptionsTypeDef",
    {
        "DhcpConfigurations": List["DhcpConfigurationTypeDef"],
        "DhcpOptionsId": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

DirectoryServiceAuthenticationRequestTypeDef = TypedDict(
    "DirectoryServiceAuthenticationRequestTypeDef", {"DirectoryId": str}, total=False
)

DirectoryServiceAuthenticationTypeDef = TypedDict(
    "DirectoryServiceAuthenticationTypeDef", {"DirectoryId": str}, total=False
)

DisableFastSnapshotRestoreErrorItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    {
        "SnapshotId": str,
        "FastSnapshotRestoreStateErrors": List["DisableFastSnapshotRestoreStateErrorItemTypeDef"],
    },
    total=False,
)

DisableFastSnapshotRestoreStateErrorItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    {"AvailabilityZone": str, "Error": "DisableFastSnapshotRestoreStateErrorTypeDef"},
    total=False,
)

DisableFastSnapshotRestoreStateErrorTypeDef = TypedDict(
    "DisableFastSnapshotRestoreStateErrorTypeDef", {"Code": str, "Message": str}, total=False
)

DisableFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": str,
        "AvailabilityZone": str,
        "State": Literal["enabling", "optimizing", "enabled", "disabling", "disabled"],
        "StateTransitionReason": str,
        "OwnerId": str,
        "OwnerAlias": str,
        "EnablingTime": datetime,
        "OptimizingTime": datetime,
        "EnabledTime": datetime,
        "DisablingTime": datetime,
        "DisabledTime": datetime,
    },
    total=False,
)

DiskImageDescriptionTypeDef = TypedDict(
    "DiskImageDescriptionTypeDef",
    {
        "Checksum": str,
        "Format": Literal["VMDK", "RAW", "VHD"],
        "ImportManifestUrl": str,
        "Size": int,
    },
    total=False,
)

DiskImageDetailTypeDef = TypedDict(
    "DiskImageDetailTypeDef",
    {"Bytes": int, "Format": Literal["VMDK", "RAW", "VHD"], "ImportManifestUrl": str},
)

DiskImageVolumeDescriptionTypeDef = TypedDict(
    "DiskImageVolumeDescriptionTypeDef", {"Id": str, "Size": int}, total=False
)

DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef", {"SizeInGB": int, "Count": int, "Type": Literal["hdd", "ssd"]}, total=False
)

DnsEntryTypeDef = TypedDict("DnsEntryTypeDef", {"DnsName": str, "HostedZoneId": str}, total=False)

EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "DeleteOnTermination": bool,
        "Iops": int,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": Literal["standard", "io1", "gp2", "sc1", "st1"],
        "KmsKeyId": str,
        "Encrypted": bool,
    },
    total=False,
)

EbsInfoTypeDef = TypedDict(
    "EbsInfoTypeDef",
    {
        "EbsOptimizedSupport": Literal["unsupported", "supported", "default"],
        "EncryptionSupport": Literal["unsupported", "supported"],
        "EbsOptimizedInfo": "EbsOptimizedInfoTypeDef",
        "NvmeSupport": Literal["unsupported", "supported", "required"],
    },
    total=False,
)

EbsInstanceBlockDeviceSpecificationTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    {"DeleteOnTermination": bool, "VolumeId": str},
    total=False,
)

EbsInstanceBlockDeviceTypeDef = TypedDict(
    "EbsInstanceBlockDeviceTypeDef",
    {
        "AttachTime": datetime,
        "DeleteOnTermination": bool,
        "Status": Literal["attaching", "attached", "detaching", "detached"],
        "VolumeId": str,
    },
    total=False,
)

EbsOptimizedInfoTypeDef = TypedDict(
    "EbsOptimizedInfoTypeDef",
    {
        "BaselineBandwidthInMbps": int,
        "BaselineThroughputInMBps": float,
        "BaselineIops": int,
        "MaximumBandwidthInMbps": int,
        "MaximumThroughputInMBps": float,
        "MaximumIops": int,
    },
    total=False,
)

EgressOnlyInternetGatewayTypeDef = TypedDict(
    "EgressOnlyInternetGatewayTypeDef",
    {
        "Attachments": List["InternetGatewayAttachmentTypeDef"],
        "EgressOnlyInternetGatewayId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ElasticGpuAssociationTypeDef = TypedDict(
    "ElasticGpuAssociationTypeDef",
    {
        "ElasticGpuId": str,
        "ElasticGpuAssociationId": str,
        "ElasticGpuAssociationState": str,
        "ElasticGpuAssociationTime": str,
    },
    total=False,
)

ElasticGpuHealthTypeDef = TypedDict(
    "ElasticGpuHealthTypeDef", {"Status": Literal["OK", "IMPAIRED"]}, total=False
)

ElasticGpuSpecificationResponseTypeDef = TypedDict(
    "ElasticGpuSpecificationResponseTypeDef", {"Type": str}, total=False
)

ElasticGpuSpecificationTypeDef = TypedDict("ElasticGpuSpecificationTypeDef", {"Type": str})

ElasticGpusTypeDef = TypedDict(
    "ElasticGpusTypeDef",
    {
        "ElasticGpuId": str,
        "AvailabilityZone": str,
        "ElasticGpuType": str,
        "ElasticGpuHealth": "ElasticGpuHealthTypeDef",
        "ElasticGpuState": Literal["ATTACHED"],
        "InstanceId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ElasticInferenceAcceleratorAssociationTypeDef = TypedDict(
    "ElasticInferenceAcceleratorAssociationTypeDef",
    {
        "ElasticInferenceAcceleratorArn": str,
        "ElasticInferenceAcceleratorAssociationId": str,
        "ElasticInferenceAcceleratorAssociationState": str,
        "ElasticInferenceAcceleratorAssociationTime": datetime,
    },
    total=False,
)

EnableFastSnapshotRestoreErrorItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    {
        "SnapshotId": str,
        "FastSnapshotRestoreStateErrors": List["EnableFastSnapshotRestoreStateErrorItemTypeDef"],
    },
    total=False,
)

EnableFastSnapshotRestoreStateErrorItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    {"AvailabilityZone": str, "Error": "EnableFastSnapshotRestoreStateErrorTypeDef"},
    total=False,
)

EnableFastSnapshotRestoreStateErrorTypeDef = TypedDict(
    "EnableFastSnapshotRestoreStateErrorTypeDef", {"Code": str, "Message": str}, total=False
)

EnableFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": str,
        "AvailabilityZone": str,
        "State": Literal["enabling", "optimizing", "enabled", "disabling", "disabled"],
        "StateTransitionReason": str,
        "OwnerId": str,
        "OwnerAlias": str,
        "EnablingTime": datetime,
        "OptimizingTime": datetime,
        "EnabledTime": datetime,
        "DisablingTime": datetime,
        "DisabledTime": datetime,
    },
    total=False,
)

EventInformationTypeDef = TypedDict(
    "EventInformationTypeDef",
    {"EventDescription": str, "EventSubType": str, "InstanceId": str},
    total=False,
)

ExportImageTaskTypeDef = TypedDict(
    "ExportImageTaskTypeDef",
    {
        "Description": str,
        "ExportImageTaskId": str,
        "ImageId": str,
        "Progress": str,
        "S3ExportLocation": "ExportTaskS3LocationTypeDef",
        "Status": str,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ExportTaskS3LocationTypeDef = TypedDict(
    "ExportTaskS3LocationTypeDef", {"S3Bucket": str, "S3Prefix": str}, total=False
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "Description": str,
        "ExportTaskId": str,
        "ExportToS3Task": "ExportToS3TaskTypeDef",
        "InstanceExportDetails": "InstanceExportDetailsTypeDef",
        "State": Literal["active", "cancelling", "cancelled", "completed"],
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ExportToS3TaskTypeDef = TypedDict(
    "ExportToS3TaskTypeDef",
    {
        "ContainerFormat": Literal["ova"],
        "DiskImageFormat": Literal["VMDK", "RAW", "VHD"],
        "S3Bucket": str,
        "S3Key": str,
    },
    total=False,
)

FailedQueuedPurchaseDeletionTypeDef = TypedDict(
    "FailedQueuedPurchaseDeletionTypeDef",
    {"Error": "DeleteQueuedReservedInstancesErrorTypeDef", "ReservedInstancesId": str},
    total=False,
)

FederatedAuthenticationRequestTypeDef = TypedDict(
    "FederatedAuthenticationRequestTypeDef", {"SAMLProviderArn": str}, total=False
)

FederatedAuthenticationTypeDef = TypedDict(
    "FederatedAuthenticationTypeDef", {"SamlProviderArn": str}, total=False
)

FleetDataTypeDef = TypedDict(
    "FleetDataTypeDef",
    {
        "ActivityStatus": Literal[
            "error", "pending_fulfillment", "pending_termination", "fulfilled"
        ],
        "CreateTime": datetime,
        "FleetId": str,
        "FleetState": Literal[
            "submitted",
            "active",
            "deleted",
            "failed",
            "deleted_running",
            "deleted_terminating",
            "modifying",
        ],
        "ClientToken": str,
        "ExcessCapacityTerminationPolicy": Literal["no-termination", "termination"],
        "FulfilledCapacity": float,
        "FulfilledOnDemandCapacity": float,
        "LaunchTemplateConfigs": List["FleetLaunchTemplateConfigTypeDef"],
        "TargetCapacitySpecification": "TargetCapacitySpecificationTypeDef",
        "TerminateInstancesWithExpiration": bool,
        "Type": Literal["request", "maintain", "instant"],
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "ReplaceUnhealthyInstances": bool,
        "SpotOptions": "SpotOptionsTypeDef",
        "OnDemandOptions": "OnDemandOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "Errors": List["DescribeFleetErrorTypeDef"],
        "Instances": List["DescribeFleetsInstancesTypeDef"],
    },
    total=False,
)

FleetLaunchTemplateConfigTypeDef = TypedDict(
    "FleetLaunchTemplateConfigTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationTypeDef",
        "Overrides": List["FleetLaunchTemplateOverridesTypeDef"],
    },
    total=False,
)

FleetLaunchTemplateOverridesRequestTypeDef = TypedDict(
    "FleetLaunchTemplateOverridesRequestTypeDef",
    {
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "MaxPrice": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "WeightedCapacity": float,
        "Priority": float,
        "Placement": "PlacementTypeDef",
    },
    total=False,
)

FleetLaunchTemplateOverridesTypeDef = TypedDict(
    "FleetLaunchTemplateOverridesTypeDef",
    {
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "MaxPrice": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "WeightedCapacity": float,
        "Priority": float,
        "Placement": "PlacementResponseTypeDef",
    },
    total=False,
)

FleetLaunchTemplateSpecificationRequestTypeDef = TypedDict(
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

FleetLaunchTemplateSpecificationTypeDef = TypedDict(
    "FleetLaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

FlowLogTypeDef = TypedDict(
    "FlowLogTypeDef",
    {
        "CreationTime": datetime,
        "DeliverLogsErrorMessage": str,
        "DeliverLogsPermissionArn": str,
        "DeliverLogsStatus": str,
        "FlowLogId": str,
        "FlowLogStatus": str,
        "LogGroupName": str,
        "ResourceId": str,
        "TrafficType": Literal["ACCEPT", "REJECT", "ALL"],
        "LogDestinationType": Literal["cloud-watch-logs", "s3"],
        "LogDestination": str,
        "LogFormat": str,
        "Tags": List["TagTypeDef"],
        "MaxAggregationInterval": int,
    },
    total=False,
)

FpgaDeviceInfoTypeDef = TypedDict(
    "FpgaDeviceInfoTypeDef",
    {"Name": str, "Manufacturer": str, "Count": int, "MemoryInfo": "FpgaDeviceMemoryInfoTypeDef"},
    total=False,
)

FpgaDeviceMemoryInfoTypeDef = TypedDict(
    "FpgaDeviceMemoryInfoTypeDef", {"SizeInMiB": int}, total=False
)

FpgaImageAttributeTypeDef = TypedDict(
    "FpgaImageAttributeTypeDef",
    {
        "FpgaImageId": str,
        "Name": str,
        "Description": str,
        "LoadPermissions": List["LoadPermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
    },
    total=False,
)

FpgaImageStateTypeDef = TypedDict(
    "FpgaImageStateTypeDef",
    {"Code": Literal["pending", "failed", "available", "unavailable"], "Message": str},
    total=False,
)

FpgaImageTypeDef = TypedDict(
    "FpgaImageTypeDef",
    {
        "FpgaImageId": str,
        "FpgaImageGlobalId": str,
        "Name": str,
        "Description": str,
        "ShellVersion": str,
        "PciId": "PciIdTypeDef",
        "State": "FpgaImageStateTypeDef",
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "OwnerId": str,
        "OwnerAlias": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "Tags": List["TagTypeDef"],
        "Public": bool,
        "DataRetentionSupport": bool,
    },
    total=False,
)

FpgaInfoTypeDef = TypedDict(
    "FpgaInfoTypeDef",
    {"Fpgas": List["FpgaDeviceInfoTypeDef"], "TotalFpgaMemoryInMiB": int},
    total=False,
)

GpuDeviceInfoTypeDef = TypedDict(
    "GpuDeviceInfoTypeDef",
    {"Name": str, "Manufacturer": str, "Count": int, "MemoryInfo": "GpuDeviceMemoryInfoTypeDef"},
    total=False,
)

GpuDeviceMemoryInfoTypeDef = TypedDict(
    "GpuDeviceMemoryInfoTypeDef", {"SizeInMiB": int}, total=False
)

GpuInfoTypeDef = TypedDict(
    "GpuInfoTypeDef",
    {"Gpus": List["GpuDeviceInfoTypeDef"], "TotalGpuMemoryInMiB": int},
    total=False,
)

GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef", {"GroupName": str, "GroupId": str}, total=False
)

HibernationOptionsTypeDef = TypedDict(
    "HibernationOptionsTypeDef", {"Configured": bool}, total=False
)

HistoryRecordEntryTypeDef = TypedDict(
    "HistoryRecordEntryTypeDef",
    {
        "EventInformation": "EventInformationTypeDef",
        "EventType": Literal["instance-change", "fleet-change", "service-error"],
        "Timestamp": datetime,
    },
    total=False,
)

HistoryRecordTypeDef = TypedDict(
    "HistoryRecordTypeDef",
    {
        "EventInformation": "EventInformationTypeDef",
        "EventType": Literal["instanceChange", "fleetRequestChange", "error", "information"],
        "Timestamp": datetime,
    },
    total=False,
)

HostInstanceTypeDef = TypedDict(
    "HostInstanceTypeDef", {"InstanceId": str, "InstanceType": str, "OwnerId": str}, total=False
)

HostOfferingTypeDef = TypedDict(
    "HostOfferingTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Duration": int,
        "HourlyPrice": str,
        "InstanceFamily": str,
        "OfferingId": str,
        "PaymentOption": Literal["AllUpfront", "PartialUpfront", "NoUpfront"],
        "UpfrontPrice": str,
    },
    total=False,
)

HostPropertiesTypeDef = TypedDict(
    "HostPropertiesTypeDef",
    {"Cores": int, "InstanceType": str, "InstanceFamily": str, "Sockets": int, "TotalVCpus": int},
    total=False,
)

HostReservationTypeDef = TypedDict(
    "HostReservationTypeDef",
    {
        "Count": int,
        "CurrencyCode": Literal["USD"],
        "Duration": int,
        "End": datetime,
        "HostIdSet": List[str],
        "HostReservationId": str,
        "HourlyPrice": str,
        "InstanceFamily": str,
        "OfferingId": str,
        "PaymentOption": Literal["AllUpfront", "PartialUpfront", "NoUpfront"],
        "Start": datetime,
        "State": Literal["payment-pending", "payment-failed", "active", "retired"],
        "UpfrontPrice": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "AutoPlacement": Literal["on", "off"],
        "AvailabilityZone": str,
        "AvailableCapacity": "AvailableCapacityTypeDef",
        "ClientToken": str,
        "HostId": str,
        "HostProperties": "HostPropertiesTypeDef",
        "HostReservationId": str,
        "Instances": List["HostInstanceTypeDef"],
        "State": Literal[
            "available",
            "under-assessment",
            "permanent-failure",
            "released",
            "released-permanent-failure",
            "pending",
        ],
        "AllocationTime": datetime,
        "ReleaseTime": datetime,
        "Tags": List["TagTypeDef"],
        "HostRecovery": Literal["on", "off"],
        "AllowsMultipleInstanceTypes": Literal["on", "off"],
        "OwnerId": str,
        "AvailabilityZoneId": str,
        "MemberOfServiceLinkedResourceGroup": bool,
    },
    total=False,
)

IKEVersionsListValueTypeDef = TypedDict("IKEVersionsListValueTypeDef", {"Value": str}, total=False)

IKEVersionsRequestListValueTypeDef = TypedDict(
    "IKEVersionsRequestListValueTypeDef", {"Value": str}, total=False
)

IamInstanceProfileAssociationTypeDef = TypedDict(
    "IamInstanceProfileAssociationTypeDef",
    {
        "AssociationId": str,
        "InstanceId": str,
        "IamInstanceProfile": "IamInstanceProfileTypeDef",
        "State": Literal["associating", "associated", "disassociating", "disassociated"],
        "Timestamp": datetime,
    },
    total=False,
)

IamInstanceProfileSpecificationTypeDef = TypedDict(
    "IamInstanceProfileSpecificationTypeDef", {"Arn": str, "Name": str}, total=False
)

IamInstanceProfileTypeDef = TypedDict(
    "IamInstanceProfileTypeDef", {"Arn": str, "Id": str}, total=False
)

IcmpTypeCodeTypeDef = TypedDict("IcmpTypeCodeTypeDef", {"Code": int, "Type": int}, total=False)

IdFormatTypeDef = TypedDict(
    "IdFormatTypeDef", {"Deadline": datetime, "Resource": str, "UseLongIds": bool}, total=False
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "Architecture": Literal["i386", "x86_64", "arm64"],
        "CreationDate": str,
        "ImageId": str,
        "ImageLocation": str,
        "ImageType": Literal["machine", "kernel", "ramdisk"],
        "Public": bool,
        "KernelId": str,
        "OwnerId": str,
        "Platform": Literal["Windows"],
        "PlatformDetails": str,
        "UsageOperation": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "RamdiskId": str,
        "State": Literal[
            "pending", "available", "invalid", "deregistered", "transient", "failed", "error"
        ],
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "EnaSupport": bool,
        "Hypervisor": Literal["ovm", "xen"],
        "ImageOwnerAlias": str,
        "Name": str,
        "RootDeviceName": str,
        "RootDeviceType": Literal["ebs", "instance-store"],
        "SriovNetSupport": str,
        "StateReason": "StateReasonTypeDef",
        "Tags": List["TagTypeDef"],
        "VirtualizationType": Literal["hvm", "paravirtual"],
    },
    total=False,
)

ImportImageLicenseConfigurationResponseTypeDef = TypedDict(
    "ImportImageLicenseConfigurationResponseTypeDef", {"LicenseConfigurationArn": str}, total=False
)

ImportImageTaskTypeDef = TypedDict(
    "ImportImageTaskTypeDef",
    {
        "Architecture": str,
        "Description": str,
        "Encrypted": bool,
        "Hypervisor": str,
        "ImageId": str,
        "ImportTaskId": str,
        "KmsKeyId": str,
        "LicenseType": str,
        "Platform": str,
        "Progress": str,
        "SnapshotDetails": List["SnapshotDetailTypeDef"],
        "Status": str,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
        "LicenseSpecifications": List["ImportImageLicenseConfigurationResponseTypeDef"],
    },
    total=False,
)

ImportInstanceTaskDetailsTypeDef = TypedDict(
    "ImportInstanceTaskDetailsTypeDef",
    {
        "Description": str,
        "InstanceId": str,
        "Platform": Literal["Windows"],
        "Volumes": List["ImportInstanceVolumeDetailItemTypeDef"],
    },
    total=False,
)

ImportInstanceVolumeDetailItemTypeDef = TypedDict(
    "ImportInstanceVolumeDetailItemTypeDef",
    {
        "AvailabilityZone": str,
        "BytesConverted": int,
        "Description": str,
        "Image": "DiskImageDescriptionTypeDef",
        "Status": str,
        "StatusMessage": str,
        "Volume": "DiskImageVolumeDescriptionTypeDef",
    },
    total=False,
)

ImportSnapshotTaskTypeDef = TypedDict(
    "ImportSnapshotTaskTypeDef",
    {
        "Description": str,
        "ImportTaskId": str,
        "SnapshotTaskDetail": "SnapshotTaskDetailTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ImportVolumeTaskDetailsTypeDef = TypedDict(
    "ImportVolumeTaskDetailsTypeDef",
    {
        "AvailabilityZone": str,
        "BytesConverted": int,
        "Description": str,
        "Image": "DiskImageDescriptionTypeDef",
        "Volume": "DiskImageVolumeDescriptionTypeDef",
    },
    total=False,
)

InferenceAcceleratorInfoTypeDef = TypedDict(
    "InferenceAcceleratorInfoTypeDef",
    {"Accelerators": List["InferenceDeviceInfoTypeDef"]},
    total=False,
)

InferenceDeviceInfoTypeDef = TypedDict(
    "InferenceDeviceInfoTypeDef", {"Count": int, "Name": str, "Manufacturer": str}, total=False
)

InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {"DeviceName": str, "Ebs": "EbsInstanceBlockDeviceTypeDef"},
    total=False,
)

InstanceCapacityTypeDef = TypedDict(
    "InstanceCapacityTypeDef",
    {"AvailableCapacity": int, "InstanceType": str, "TotalCapacity": int},
    total=False,
)

InstanceCountTypeDef = TypedDict(
    "InstanceCountTypeDef",
    {"InstanceCount": int, "State": Literal["available", "sold", "cancelled", "pending"]},
    total=False,
)

InstanceCreditSpecificationTypeDef = TypedDict(
    "InstanceCreditSpecificationTypeDef", {"InstanceId": str, "CpuCredits": str}, total=False
)

InstanceExportDetailsTypeDef = TypedDict(
    "InstanceExportDetailsTypeDef",
    {"InstanceId": str, "TargetEnvironment": Literal["citrix", "vmware", "microsoft"]},
    total=False,
)

InstanceFamilyCreditSpecificationTypeDef = TypedDict(
    "InstanceFamilyCreditSpecificationTypeDef",
    {"InstanceFamily": Literal["t2", "t3", "t3a"], "CpuCredits": str},
    total=False,
)

InstanceIpv6AddressRequestTypeDef = TypedDict(
    "InstanceIpv6AddressRequestTypeDef", {"Ipv6Address": str}, total=False
)

InstanceIpv6AddressTypeDef = TypedDict(
    "InstanceIpv6AddressTypeDef", {"Ipv6Address": str}, total=False
)

InstanceMetadataOptionsResponseTypeDef = TypedDict(
    "InstanceMetadataOptionsResponseTypeDef",
    {
        "State": Literal["pending", "applied"],
        "HttpTokens": Literal["optional", "required"],
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": Literal["disabled", "enabled"],
    },
    total=False,
)

InstanceMonitoringTypeDef = TypedDict(
    "InstanceMonitoringTypeDef", {"InstanceId": str, "Monitoring": "MonitoringTypeDef"}, total=False
)

InstanceNetworkInterfaceAssociationTypeDef = TypedDict(
    "InstanceNetworkInterfaceAssociationTypeDef",
    {"CarrierIp": str, "IpOwnerId": str, "PublicDnsName": str, "PublicIp": str},
    total=False,
)

InstanceNetworkInterfaceAttachmentTypeDef = TypedDict(
    "InstanceNetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": datetime,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "Status": Literal["attaching", "attached", "detaching", "detached"],
    },
    total=False,
)

InstanceNetworkInterfaceSpecificationTypeDef = TypedDict(
    "InstanceNetworkInterfaceSpecificationTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
        "AssociateCarrierIpAddress": bool,
        "InterfaceType": str,
    },
    total=False,
)

InstanceNetworkInterfaceTypeDef = TypedDict(
    "InstanceNetworkInterfaceTypeDef",
    {
        "Association": "InstanceNetworkInterfaceAssociationTypeDef",
        "Attachment": "InstanceNetworkInterfaceAttachmentTypeDef",
        "Description": str,
        "Groups": List["GroupIdentifierTypeDef"],
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "MacAddress": str,
        "NetworkInterfaceId": str,
        "OwnerId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["InstancePrivateIpAddressTypeDef"],
        "SourceDestCheck": bool,
        "Status": Literal["available", "associated", "attaching", "in-use", "detaching"],
        "SubnetId": str,
        "VpcId": str,
        "InterfaceType": str,
    },
    total=False,
)

InstancePrivateIpAddressTypeDef = TypedDict(
    "InstancePrivateIpAddressTypeDef",
    {
        "Association": "InstanceNetworkInterfaceAssociationTypeDef",
        "Primary": bool,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

InstanceStateChangeTypeDef = TypedDict(
    "InstanceStateChangeTypeDef",
    {
        "CurrentState": "InstanceStateTypeDef",
        "InstanceId": str,
        "PreviousState": "InstanceStateTypeDef",
    },
    total=False,
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "Code": int,
        "Name": Literal["pending", "running", "shutting-down", "terminated", "stopping", "stopped"],
    },
    total=False,
)

InstanceStatusDetailsTypeDef = TypedDict(
    "InstanceStatusDetailsTypeDef",
    {
        "ImpairedSince": datetime,
        "Name": Literal["reachability"],
        "Status": Literal["passed", "failed", "insufficient-data", "initializing"],
    },
    total=False,
)

InstanceStatusEventTypeDef = TypedDict(
    "InstanceStatusEventTypeDef",
    {
        "InstanceEventId": str,
        "Code": Literal[
            "instance-reboot",
            "system-reboot",
            "system-maintenance",
            "instance-retirement",
            "instance-stop",
        ],
        "Description": str,
        "NotAfter": datetime,
        "NotBefore": datetime,
        "NotBeforeDeadline": datetime,
    },
    total=False,
)

InstanceStatusSummaryTypeDef = TypedDict(
    "InstanceStatusSummaryTypeDef",
    {
        "Details": List["InstanceStatusDetailsTypeDef"],
        "Status": Literal["ok", "impaired", "insufficient-data", "not-applicable", "initializing"],
    },
    total=False,
)

InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "AvailabilityZone": str,
        "OutpostArn": str,
        "Events": List["InstanceStatusEventTypeDef"],
        "InstanceId": str,
        "InstanceState": "InstanceStateTypeDef",
        "InstanceStatus": "InstanceStatusSummaryTypeDef",
        "SystemStatus": "InstanceStatusSummaryTypeDef",
    },
    total=False,
)

InstanceStorageInfoTypeDef = TypedDict(
    "InstanceStorageInfoTypeDef",
    {"TotalSizeInGB": int, "Disks": List["DiskInfoTypeDef"]},
    total=False,
)

InstanceTagNotificationAttributeTypeDef = TypedDict(
    "InstanceTagNotificationAttributeTypeDef",
    {"InstanceTagKeys": List[str], "IncludeAllTagsOfInstance": bool},
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AmiLaunchIndex": int,
        "ImageId": str,
        "InstanceId": str,
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "KernelId": str,
        "KeyName": str,
        "LaunchTime": datetime,
        "Monitoring": "MonitoringTypeDef",
        "Placement": "PlacementTypeDef",
        "Platform": Literal["Windows"],
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "RamdiskId": str,
        "State": "InstanceStateTypeDef",
        "StateTransitionReason": str,
        "SubnetId": str,
        "VpcId": str,
        "Architecture": Literal["i386", "x86_64", "arm64"],
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "ClientToken": str,
        "EbsOptimized": bool,
        "EnaSupport": bool,
        "Hypervisor": Literal["ovm", "xen"],
        "IamInstanceProfile": "IamInstanceProfileTypeDef",
        "InstanceLifecycle": Literal["spot", "scheduled"],
        "ElasticGpuAssociations": List["ElasticGpuAssociationTypeDef"],
        "ElasticInferenceAcceleratorAssociations": List[
            "ElasticInferenceAcceleratorAssociationTypeDef"
        ],
        "NetworkInterfaces": List["InstanceNetworkInterfaceTypeDef"],
        "OutpostArn": str,
        "RootDeviceName": str,
        "RootDeviceType": Literal["ebs", "instance-store"],
        "SecurityGroups": List["GroupIdentifierTypeDef"],
        "SourceDestCheck": bool,
        "SpotInstanceRequestId": str,
        "SriovNetSupport": str,
        "StateReason": "StateReasonTypeDef",
        "Tags": List["TagTypeDef"],
        "VirtualizationType": Literal["hvm", "paravirtual"],
        "CpuOptions": "CpuOptionsTypeDef",
        "CapacityReservationId": str,
        "CapacityReservationSpecification": "CapacityReservationSpecificationResponseTypeDef",
        "HibernationOptions": "HibernationOptionsTypeDef",
        "Licenses": List["LicenseConfigurationTypeDef"],
        "MetadataOptions": "InstanceMetadataOptionsResponseTypeDef",
    },
    total=False,
)

InstanceTypeInfoTypeDef = TypedDict(
    "InstanceTypeInfoTypeDef",
    {
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "CurrentGeneration": bool,
        "FreeTierEligible": bool,
        "SupportedUsageClasses": List[Literal["spot", "on-demand"]],
        "SupportedRootDeviceTypes": List[Literal["ebs", "instance-store"]],
        "SupportedVirtualizationTypes": List[Literal["hvm", "paravirtual"]],
        "BareMetal": bool,
        "Hypervisor": Literal["nitro", "xen"],
        "ProcessorInfo": "ProcessorInfoTypeDef",
        "VCpuInfo": "VCpuInfoTypeDef",
        "MemoryInfo": "MemoryInfoTypeDef",
        "InstanceStorageSupported": bool,
        "InstanceStorageInfo": "InstanceStorageInfoTypeDef",
        "EbsInfo": "EbsInfoTypeDef",
        "NetworkInfo": "NetworkInfoTypeDef",
        "GpuInfo": "GpuInfoTypeDef",
        "FpgaInfo": "FpgaInfoTypeDef",
        "PlacementGroupInfo": "PlacementGroupInfoTypeDef",
        "InferenceAcceleratorInfo": "InferenceAcceleratorInfoTypeDef",
        "HibernationSupported": bool,
        "BurstablePerformanceSupported": bool,
        "DedicatedHostsSupported": bool,
        "AutoRecoverySupported": bool,
    },
    total=False,
)

InstanceTypeOfferingTypeDef = TypedDict(
    "InstanceTypeOfferingTypeDef",
    {
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "LocationType": Literal["region", "availability-zone", "availability-zone-id"],
        "Location": str,
    },
    total=False,
)

InstanceUsageTypeDef = TypedDict(
    "InstanceUsageTypeDef", {"AccountId": str, "UsedInstanceCount": int}, total=False
)

InternetGatewayAttachmentTypeDef = TypedDict(
    "InternetGatewayAttachmentTypeDef",
    {"State": Literal["attaching", "attached", "detaching", "detached"], "VpcId": str},
    total=False,
)

InternetGatewayTypeDef = TypedDict(
    "InternetGatewayTypeDef",
    {
        "Attachments": List["InternetGatewayAttachmentTypeDef"],
        "InternetGatewayId": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef",
    {
        "FromPort": int,
        "IpProtocol": str,
        "IpRanges": List["IpRangeTypeDef"],
        "Ipv6Ranges": List["Ipv6RangeTypeDef"],
        "PrefixListIds": List["PrefixListIdTypeDef"],
        "ToPort": int,
        "UserIdGroupPairs": List["UserIdGroupPairTypeDef"],
    },
    total=False,
)

IpRangeTypeDef = TypedDict("IpRangeTypeDef", {"CidrIp": str, "Description": str}, total=False)

Ipv6CidrAssociationTypeDef = TypedDict(
    "Ipv6CidrAssociationTypeDef", {"Ipv6Cidr": str, "AssociatedResource": str}, total=False
)

Ipv6CidrBlockTypeDef = TypedDict("Ipv6CidrBlockTypeDef", {"Ipv6CidrBlock": str}, total=False)

Ipv6PoolTypeDef = TypedDict(
    "Ipv6PoolTypeDef",
    {
        "PoolId": str,
        "Description": str,
        "PoolCidrBlocks": List["PoolCidrBlockTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

Ipv6RangeTypeDef = TypedDict("Ipv6RangeTypeDef", {"CidrIpv6": str, "Description": str}, total=False)

KeyPairInfoTypeDef = TypedDict(
    "KeyPairInfoTypeDef",
    {"KeyPairId": str, "KeyFingerprint": str, "KeyName": str, "Tags": List["TagTypeDef"]},
    total=False,
)

LastErrorTypeDef = TypedDict("LastErrorTypeDef", {"Message": str, "Code": str}, total=False)

LaunchPermissionTypeDef = TypedDict(
    "LaunchPermissionTypeDef", {"Group": Literal["all"], "UserId": str}, total=False
)

LaunchSpecificationTypeDef = TypedDict(
    "LaunchSpecificationTypeDef",
    {
        "UserData": str,
        "SecurityGroups": List["GroupIdentifierTypeDef"],
        "AddressingType": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "ImageId": str,
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "KernelId": str,
        "KeyName": str,
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "Placement": "SpotPlacementTypeDef",
        "RamdiskId": str,
        "SubnetId": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
    },
    total=False,
)

LaunchTemplateAndOverridesResponseTypeDef = TypedDict(
    "LaunchTemplateAndOverridesResponseTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationTypeDef",
        "Overrides": "FleetLaunchTemplateOverridesTypeDef",
    },
    total=False,
)

LaunchTemplateBlockDeviceMappingRequestTypeDef = TypedDict(
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    {
        "DeviceName": str,
        "VirtualName": str,
        "Ebs": "LaunchTemplateEbsBlockDeviceRequestTypeDef",
        "NoDevice": str,
    },
    total=False,
)

LaunchTemplateBlockDeviceMappingTypeDef = TypedDict(
    "LaunchTemplateBlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "VirtualName": str,
        "Ebs": "LaunchTemplateEbsBlockDeviceTypeDef",
        "NoDevice": str,
    },
    total=False,
)

LaunchTemplateCapacityReservationSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    {
        "CapacityReservationPreference": Literal["open", "none"],
        "CapacityReservationTarget": "CapacityReservationTargetTypeDef",
    },
    total=False,
)

LaunchTemplateCapacityReservationSpecificationResponseTypeDef = TypedDict(
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    {
        "CapacityReservationPreference": Literal["open", "none"],
        "CapacityReservationTarget": "CapacityReservationTargetResponseTypeDef",
    },
    total=False,
)

LaunchTemplateConfigTypeDef = TypedDict(
    "LaunchTemplateConfigTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationTypeDef",
        "Overrides": List["LaunchTemplateOverridesTypeDef"],
    },
    total=False,
)

LaunchTemplateCpuOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateCpuOptionsRequestTypeDef", {"CoreCount": int, "ThreadsPerCore": int}, total=False
)

LaunchTemplateCpuOptionsTypeDef = TypedDict(
    "LaunchTemplateCpuOptionsTypeDef", {"CoreCount": int, "ThreadsPerCore": int}, total=False
)

LaunchTemplateEbsBlockDeviceRequestTypeDef = TypedDict(
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    {
        "Encrypted": bool,
        "DeleteOnTermination": bool,
        "Iops": int,
        "KmsKeyId": str,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": Literal["standard", "io1", "gp2", "sc1", "st1"],
    },
    total=False,
)

LaunchTemplateEbsBlockDeviceTypeDef = TypedDict(
    "LaunchTemplateEbsBlockDeviceTypeDef",
    {
        "Encrypted": bool,
        "DeleteOnTermination": bool,
        "Iops": int,
        "KmsKeyId": str,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": Literal["standard", "io1", "gp2", "sc1", "st1"],
    },
    total=False,
)

LaunchTemplateElasticInferenceAcceleratorResponseTypeDef = TypedDict(
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    {"Type": str, "Count": int},
    total=False,
)

_RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef = TypedDict(
    "_RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef", {"Type": str}
)
_OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef = TypedDict(
    "_OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef", {"Count": int}, total=False
)


class LaunchTemplateElasticInferenceAcceleratorTypeDef(
    _RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef,
    _OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef,
):
    pass


LaunchTemplateHibernationOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateHibernationOptionsRequestTypeDef", {"Configured": bool}, total=False
)

LaunchTemplateHibernationOptionsTypeDef = TypedDict(
    "LaunchTemplateHibernationOptionsTypeDef", {"Configured": bool}, total=False
)

LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    {"Arn": str, "Name": str},
    total=False,
)

LaunchTemplateIamInstanceProfileSpecificationTypeDef = TypedDict(
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef", {"Arn": str, "Name": str}, total=False
)

LaunchTemplateInstanceMarketOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    {"MarketType": Literal["spot"], "SpotOptions": "LaunchTemplateSpotMarketOptionsRequestTypeDef"},
    total=False,
)

LaunchTemplateInstanceMarketOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    {"MarketType": Literal["spot"], "SpotOptions": "LaunchTemplateSpotMarketOptionsTypeDef"},
    total=False,
)

LaunchTemplateInstanceMetadataOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": Literal["optional", "required"],
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": Literal["disabled", "enabled"],
    },
    total=False,
)

LaunchTemplateInstanceMetadataOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    {
        "State": Literal["pending", "applied"],
        "HttpTokens": Literal["optional", "required"],
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": Literal["disabled", "enabled"],
    },
    total=False,
)

LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    {
        "AssociateCarrierIpAddress": bool,
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "InterfaceType": str,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressRequestTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
    },
    total=False,
)

LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef = TypedDict(
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    {
        "AssociateCarrierIpAddress": bool,
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "InterfaceType": str,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
    },
    total=False,
)

LaunchTemplateLicenseConfigurationRequestTypeDef = TypedDict(
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    {"LicenseConfigurationArn": str},
    total=False,
)

LaunchTemplateLicenseConfigurationTypeDef = TypedDict(
    "LaunchTemplateLicenseConfigurationTypeDef", {"LicenseConfigurationArn": str}, total=False
)

LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef",
    {
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "SpotPrice": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "WeightedCapacity": float,
        "Priority": float,
    },
    total=False,
)

LaunchTemplatePlacementRequestTypeDef = TypedDict(
    "LaunchTemplatePlacementRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "HostId": str,
        "Tenancy": Literal["default", "dedicated", "host"],
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
        "PartitionNumber": int,
    },
    total=False,
)

LaunchTemplatePlacementTypeDef = TypedDict(
    "LaunchTemplatePlacementTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "HostId": str,
        "Tenancy": Literal["default", "dedicated", "host"],
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
        "PartitionNumber": int,
    },
    total=False,
)

LaunchTemplateSpotMarketOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    {
        "MaxPrice": str,
        "SpotInstanceType": Literal["one-time", "persistent"],
        "BlockDurationMinutes": int,
        "ValidUntil": datetime,
        "InstanceInterruptionBehavior": Literal["hibernate", "stop", "terminate"],
    },
    total=False,
)

LaunchTemplateSpotMarketOptionsTypeDef = TypedDict(
    "LaunchTemplateSpotMarketOptionsTypeDef",
    {
        "MaxPrice": str,
        "SpotInstanceType": Literal["one-time", "persistent"],
        "BlockDurationMinutes": int,
        "ValidUntil": datetime,
        "InstanceInterruptionBehavior": Literal["hibernate", "stop", "terminate"],
    },
    total=False,
)

LaunchTemplateTagSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateTagSpecificationRequestTypeDef",
    {
        "ResourceType": Literal[
            "client-vpn-endpoint",
            "customer-gateway",
            "dedicated-host",
            "dhcp-options",
            "elastic-ip",
            "elastic-gpu",
            "export-image-task",
            "export-instance-task",
            "fleet",
            "fpga-image",
            "host-reservation",
            "image",
            "import-image-task",
            "import-snapshot-task",
            "instance",
            "internet-gateway",
            "key-pair",
            "launch-template",
            "local-gateway-route-table-vpc-association",
            "natgateway",
            "network-acl",
            "network-interface",
            "placement-group",
            "reserved-instances",
            "route-table",
            "security-group",
            "snapshot",
            "spot-fleet-request",
            "spot-instances-request",
            "subnet",
            "traffic-mirror-filter",
            "traffic-mirror-session",
            "traffic-mirror-target",
            "transit-gateway",
            "transit-gateway-attachment",
            "transit-gateway-multicast-domain",
            "transit-gateway-route-table",
            "volume",
            "vpc",
            "vpc-peering-connection",
            "vpn-connection",
            "vpn-gateway",
            "vpc-flow-log",
        ],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LaunchTemplateTagSpecificationTypeDef = TypedDict(
    "LaunchTemplateTagSpecificationTypeDef",
    {
        "ResourceType": Literal[
            "client-vpn-endpoint",
            "customer-gateway",
            "dedicated-host",
            "dhcp-options",
            "elastic-ip",
            "elastic-gpu",
            "export-image-task",
            "export-instance-task",
            "fleet",
            "fpga-image",
            "host-reservation",
            "image",
            "import-image-task",
            "import-snapshot-task",
            "instance",
            "internet-gateway",
            "key-pair",
            "launch-template",
            "local-gateway-route-table-vpc-association",
            "natgateway",
            "network-acl",
            "network-interface",
            "placement-group",
            "reserved-instances",
            "route-table",
            "security-group",
            "snapshot",
            "spot-fleet-request",
            "spot-instances-request",
            "subnet",
            "traffic-mirror-filter",
            "traffic-mirror-session",
            "traffic-mirror-target",
            "transit-gateway",
            "transit-gateway-attachment",
            "transit-gateway-multicast-domain",
            "transit-gateway-route-table",
            "volume",
            "vpc",
            "vpc-peering-connection",
            "vpn-connection",
            "vpn-gateway",
            "vpc-flow-log",
        ],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "CreateTime": datetime,
        "CreatedBy": str,
        "DefaultVersionNumber": int,
        "LatestVersionNumber": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LaunchTemplateVersionTypeDef = TypedDict(
    "LaunchTemplateVersionTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "VersionNumber": int,
        "VersionDescription": str,
        "CreateTime": datetime,
        "CreatedBy": str,
        "DefaultVersion": bool,
        "LaunchTemplateData": "ResponseLaunchTemplateDataTypeDef",
    },
    total=False,
)

LaunchTemplatesMonitoringRequestTypeDef = TypedDict(
    "LaunchTemplatesMonitoringRequestTypeDef", {"Enabled": bool}, total=False
)

LaunchTemplatesMonitoringTypeDef = TypedDict(
    "LaunchTemplatesMonitoringTypeDef", {"Enabled": bool}, total=False
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef", {"LicenseConfigurationArn": str}, total=False
)

LoadBalancersConfigTypeDef = TypedDict(
    "LoadBalancersConfigTypeDef",
    {
        "ClassicLoadBalancersConfig": "ClassicLoadBalancersConfigTypeDef",
        "TargetGroupsConfig": "TargetGroupsConfigTypeDef",
    },
    total=False,
)

LoadPermissionRequestTypeDef = TypedDict(
    "LoadPermissionRequestTypeDef", {"Group": Literal["all"], "UserId": str}, total=False
)

LoadPermissionTypeDef = TypedDict(
    "LoadPermissionTypeDef", {"UserId": str, "Group": Literal["all"]}, total=False
)

LocalGatewayRouteTableTypeDef = TypedDict(
    "LocalGatewayRouteTableTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "LocalGatewayId": str,
        "OutpostArn": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef = TypedDict(
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "LocalGatewayId": str,
        "LocalGatewayRouteTableId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayRouteTableVpcAssociationTypeDef = TypedDict(
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationId": str,
        "LocalGatewayRouteTableId": str,
        "LocalGatewayId": str,
        "VpcId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayRouteTypeDef = TypedDict(
    "LocalGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "Type": Literal["static", "propagated"],
        "State": Literal["pending", "active", "blackhole", "deleting", "deleted"],
        "LocalGatewayRouteTableId": str,
    },
    total=False,
)

LocalGatewayTypeDef = TypedDict(
    "LocalGatewayTypeDef",
    {
        "LocalGatewayId": str,
        "OutpostArn": str,
        "OwnerId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayVirtualInterfaceGroupTypeDef = TypedDict(
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroupId": str,
        "LocalGatewayVirtualInterfaceIds": List[str],
        "LocalGatewayId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayVirtualInterfaceTypeDef = TypedDict(
    "LocalGatewayVirtualInterfaceTypeDef",
    {
        "LocalGatewayVirtualInterfaceId": str,
        "LocalGatewayId": str,
        "Vlan": int,
        "LocalAddress": str,
        "PeerAddress": str,
        "LocalBgpAsn": int,
        "PeerBgpAsn": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ManagedPrefixListTypeDef = TypedDict(
    "ManagedPrefixListTypeDef",
    {
        "PrefixListId": str,
        "AddressFamily": str,
        "State": Literal[
            "create-in-progress",
            "create-complete",
            "create-failed",
            "modify-in-progress",
            "modify-complete",
            "modify-failed",
            "restore-in-progress",
            "restore-complete",
            "restore-failed",
            "delete-in-progress",
            "delete-complete",
            "delete-failed",
        ],
        "StateMessage": str,
        "PrefixListArn": str,
        "PrefixListName": str,
        "MaxEntries": int,
        "Version": int,
        "Tags": List["TagTypeDef"],
        "OwnerId": str,
    },
    total=False,
)

MemoryInfoTypeDef = TypedDict("MemoryInfoTypeDef", {"SizeInMiB": int}, total=False)

MonitoringTypeDef = TypedDict(
    "MonitoringTypeDef",
    {"State": Literal["disabled", "disabling", "enabled", "pending"]},
    total=False,
)

MovingAddressStatusTypeDef = TypedDict(
    "MovingAddressStatusTypeDef",
    {"MoveStatus": Literal["movingToVpc", "restoringToClassic"], "PublicIp": str},
    total=False,
)

NatGatewayAddressTypeDef = TypedDict(
    "NatGatewayAddressTypeDef",
    {"AllocationId": str, "NetworkInterfaceId": str, "PrivateIp": str, "PublicIp": str},
    total=False,
)

NatGatewayTypeDef = TypedDict(
    "NatGatewayTypeDef",
    {
        "CreateTime": datetime,
        "DeleteTime": datetime,
        "FailureCode": str,
        "FailureMessage": str,
        "NatGatewayAddresses": List["NatGatewayAddressTypeDef"],
        "NatGatewayId": str,
        "ProvisionedBandwidth": "ProvisionedBandwidthTypeDef",
        "State": Literal["pending", "failed", "available", "deleting", "deleted"],
        "SubnetId": str,
        "VpcId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

NetworkAclAssociationTypeDef = TypedDict(
    "NetworkAclAssociationTypeDef",
    {"NetworkAclAssociationId": str, "NetworkAclId": str, "SubnetId": str},
    total=False,
)

NetworkAclEntryTypeDef = TypedDict(
    "NetworkAclEntryTypeDef",
    {
        "CidrBlock": str,
        "Egress": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
        "Protocol": str,
        "RuleAction": Literal["allow", "deny"],
        "RuleNumber": int,
    },
    total=False,
)

NetworkAclTypeDef = TypedDict(
    "NetworkAclTypeDef",
    {
        "Associations": List["NetworkAclAssociationTypeDef"],
        "Entries": List["NetworkAclEntryTypeDef"],
        "IsDefault": bool,
        "NetworkAclId": str,
        "Tags": List["TagTypeDef"],
        "VpcId": str,
        "OwnerId": str,
    },
    total=False,
)

NetworkInfoTypeDef = TypedDict(
    "NetworkInfoTypeDef",
    {
        "NetworkPerformance": str,
        "MaximumNetworkInterfaces": int,
        "Ipv4AddressesPerInterface": int,
        "Ipv6AddressesPerInterface": int,
        "Ipv6Supported": bool,
        "EnaSupport": Literal["unsupported", "supported", "required"],
        "EfaSupported": bool,
    },
    total=False,
)

NetworkInterfaceAssociationTypeDef = TypedDict(
    "NetworkInterfaceAssociationTypeDef",
    {
        "AllocationId": str,
        "AssociationId": str,
        "IpOwnerId": str,
        "PublicDnsName": str,
        "PublicIp": str,
        "CustomerOwnedIp": str,
        "CarrierIp": str,
    },
    total=False,
)

NetworkInterfaceAttachmentTypeDef = TypedDict(
    "NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": datetime,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": Literal["attaching", "attached", "detaching", "detached"],
    },
    total=False,
)

NetworkInterfaceIpv6AddressTypeDef = TypedDict(
    "NetworkInterfaceIpv6AddressTypeDef", {"Ipv6Address": str}, total=False
)

NetworkInterfacePermissionStateTypeDef = TypedDict(
    "NetworkInterfacePermissionStateTypeDef",
    {"State": Literal["pending", "granted", "revoking", "revoked"], "StatusMessage": str},
    total=False,
)

NetworkInterfacePermissionTypeDef = TypedDict(
    "NetworkInterfacePermissionTypeDef",
    {
        "NetworkInterfacePermissionId": str,
        "NetworkInterfaceId": str,
        "AwsAccountId": str,
        "AwsService": str,
        "Permission": Literal["INSTANCE-ATTACH", "EIP-ASSOCIATE"],
        "PermissionState": "NetworkInterfacePermissionStateTypeDef",
    },
    total=False,
)

NetworkInterfacePrivateIpAddressTypeDef = TypedDict(
    "NetworkInterfacePrivateIpAddressTypeDef",
    {
        "Association": "NetworkInterfaceAssociationTypeDef",
        "Primary": bool,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Association": "NetworkInterfaceAssociationTypeDef",
        "Attachment": "NetworkInterfaceAttachmentTypeDef",
        "AvailabilityZone": str,
        "Description": str,
        "Groups": List["GroupIdentifierTypeDef"],
        "InterfaceType": Literal["interface", "natGateway", "efa"],
        "Ipv6Addresses": List["NetworkInterfaceIpv6AddressTypeDef"],
        "MacAddress": str,
        "NetworkInterfaceId": str,
        "OutpostArn": str,
        "OwnerId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["NetworkInterfacePrivateIpAddressTypeDef"],
        "RequesterId": str,
        "RequesterManaged": bool,
        "SourceDestCheck": bool,
        "Status": Literal["available", "associated", "attaching", "in-use", "detaching"],
        "SubnetId": str,
        "TagSet": List["TagTypeDef"],
        "VpcId": str,
    },
    total=False,
)

OnDemandOptionsTypeDef = TypedDict(
    "OnDemandOptionsTypeDef",
    {
        "AllocationStrategy": Literal["lowest-price", "prioritized"],
        "CapacityReservationOptions": "CapacityReservationOptionsTypeDef",
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

PciIdTypeDef = TypedDict(
    "PciIdTypeDef",
    {"DeviceId": str, "VendorId": str, "SubsystemId": str, "SubsystemVendorId": str},
    total=False,
)

PeeringAttachmentStatusTypeDef = TypedDict(
    "PeeringAttachmentStatusTypeDef", {"Code": str, "Message": str}, total=False
)

PeeringConnectionOptionsTypeDef = TypedDict(
    "PeeringConnectionOptionsTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
    total=False,
)

PeeringTgwInfoTypeDef = TypedDict(
    "PeeringTgwInfoTypeDef", {"TransitGatewayId": str, "OwnerId": str, "Region": str}, total=False
)

Phase1DHGroupNumbersListValueTypeDef = TypedDict(
    "Phase1DHGroupNumbersListValueTypeDef", {"Value": int}, total=False
)

Phase1DHGroupNumbersRequestListValueTypeDef = TypedDict(
    "Phase1DHGroupNumbersRequestListValueTypeDef", {"Value": int}, total=False
)

Phase1EncryptionAlgorithmsListValueTypeDef = TypedDict(
    "Phase1EncryptionAlgorithmsListValueTypeDef", {"Value": str}, total=False
)

Phase1EncryptionAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef", {"Value": str}, total=False
)

Phase1IntegrityAlgorithmsListValueTypeDef = TypedDict(
    "Phase1IntegrityAlgorithmsListValueTypeDef", {"Value": str}, total=False
)

Phase1IntegrityAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef", {"Value": str}, total=False
)

Phase2DHGroupNumbersListValueTypeDef = TypedDict(
    "Phase2DHGroupNumbersListValueTypeDef", {"Value": int}, total=False
)

Phase2DHGroupNumbersRequestListValueTypeDef = TypedDict(
    "Phase2DHGroupNumbersRequestListValueTypeDef", {"Value": int}, total=False
)

Phase2EncryptionAlgorithmsListValueTypeDef = TypedDict(
    "Phase2EncryptionAlgorithmsListValueTypeDef", {"Value": str}, total=False
)

Phase2EncryptionAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef", {"Value": str}, total=False
)

Phase2IntegrityAlgorithmsListValueTypeDef = TypedDict(
    "Phase2IntegrityAlgorithmsListValueTypeDef", {"Value": str}, total=False
)

Phase2IntegrityAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef", {"Value": str}, total=False
)

PlacementGroupInfoTypeDef = TypedDict(
    "PlacementGroupInfoTypeDef",
    {"SupportedStrategies": List[Literal["cluster", "partition", "spread"]]},
    total=False,
)

PlacementGroupTypeDef = TypedDict(
    "PlacementGroupTypeDef",
    {
        "GroupName": str,
        "State": Literal["pending", "available", "deleting", "deleted"],
        "Strategy": Literal["cluster", "spread", "partition"],
        "PartitionCount": int,
        "GroupId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

PlacementResponseTypeDef = TypedDict("PlacementResponseTypeDef", {"GroupName": str}, total=False)

PlacementTypeDef = TypedDict(
    "PlacementTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "PartitionNumber": int,
        "HostId": str,
        "Tenancy": Literal["default", "dedicated", "host"],
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
    },
    total=False,
)

PoolCidrBlockTypeDef = TypedDict("PoolCidrBlockTypeDef", {"Cidr": str}, total=False)

PortRangeTypeDef = TypedDict("PortRangeTypeDef", {"From": int, "To": int}, total=False)

PrefixListAssociationTypeDef = TypedDict(
    "PrefixListAssociationTypeDef", {"ResourceId": str, "ResourceOwner": str}, total=False
)

PrefixListEntryTypeDef = TypedDict(
    "PrefixListEntryTypeDef", {"Cidr": str, "Description": str}, total=False
)

PrefixListIdTypeDef = TypedDict(
    "PrefixListIdTypeDef", {"Description": str, "PrefixListId": str}, total=False
)

PrefixListTypeDef = TypedDict(
    "PrefixListTypeDef",
    {"Cidrs": List[str], "PrefixListId": str, "PrefixListName": str},
    total=False,
)

PriceScheduleTypeDef = TypedDict(
    "PriceScheduleTypeDef",
    {"Active": bool, "CurrencyCode": Literal["USD"], "Price": float, "Term": int},
    total=False,
)

PricingDetailTypeDef = TypedDict(
    "PricingDetailTypeDef", {"Count": int, "Price": float}, total=False
)

PrincipalIdFormatTypeDef = TypedDict(
    "PrincipalIdFormatTypeDef", {"Arn": str, "Statuses": List["IdFormatTypeDef"]}, total=False
)

PrivateDnsNameConfigurationTypeDef = TypedDict(
    "PrivateDnsNameConfigurationTypeDef",
    {
        "State": Literal["pendingVerification", "verified", "failed"],
        "Type": str,
        "Value": str,
        "Name": str,
    },
    total=False,
)

PrivateIpAddressSpecificationTypeDef = TypedDict(
    "PrivateIpAddressSpecificationTypeDef", {"Primary": bool, "PrivateIpAddress": str}, total=False
)

ProcessorInfoTypeDef = TypedDict(
    "ProcessorInfoTypeDef",
    {
        "SupportedArchitectures": List[Literal["i386", "x86_64", "arm64"]],
        "SustainedClockSpeedInGhz": float,
    },
    total=False,
)

ProductCodeTypeDef = TypedDict(
    "ProductCodeTypeDef",
    {"ProductCodeId": str, "ProductCodeType": Literal["devpay", "marketplace"]},
    total=False,
)

PropagatingVgwTypeDef = TypedDict("PropagatingVgwTypeDef", {"GatewayId": str}, total=False)

ProvisionedBandwidthTypeDef = TypedDict(
    "ProvisionedBandwidthTypeDef",
    {
        "ProvisionTime": datetime,
        "Provisioned": str,
        "RequestTime": datetime,
        "Requested": str,
        "Status": str,
    },
    total=False,
)

PublicIpv4PoolRangeTypeDef = TypedDict(
    "PublicIpv4PoolRangeTypeDef",
    {"FirstAddress": str, "LastAddress": str, "AddressCount": int, "AvailableAddressCount": int},
    total=False,
)

PublicIpv4PoolTypeDef = TypedDict(
    "PublicIpv4PoolTypeDef",
    {
        "PoolId": str,
        "Description": str,
        "PoolAddressRanges": List["PublicIpv4PoolRangeTypeDef"],
        "TotalAddressCount": int,
        "TotalAvailableAddressCount": int,
        "NetworkBorderGroup": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

PurchaseTypeDef = TypedDict(
    "PurchaseTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Duration": int,
        "HostIdSet": List[str],
        "HostReservationId": str,
        "HourlyPrice": str,
        "InstanceFamily": str,
        "PaymentOption": Literal["AllUpfront", "PartialUpfront", "NoUpfront"],
        "UpfrontPrice": str,
    },
    total=False,
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef", {"Amount": float, "Frequency": Literal["Hourly"]}, total=False
)

RegionTypeDef = TypedDict(
    "RegionTypeDef", {"Endpoint": str, "RegionName": str, "OptInStatus": str}, total=False
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "Instances": List["InstanceTypeDef"],
        "OwnerId": str,
        "RequesterId": str,
        "ReservationId": str,
    },
    total=False,
)

ReservationValueTypeDef = TypedDict(
    "ReservationValueTypeDef",
    {"HourlyPrice": str, "RemainingTotalValue": str, "RemainingUpfrontValue": str},
    total=False,
)

ReservedInstanceReservationValueTypeDef = TypedDict(
    "ReservedInstanceReservationValueTypeDef",
    {"ReservationValue": "ReservationValueTypeDef", "ReservedInstanceId": str},
    total=False,
)

ReservedInstancesConfigurationTypeDef = TypedDict(
    "ReservedInstancesConfigurationTypeDef",
    {
        "AvailabilityZone": str,
        "InstanceCount": int,
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "Platform": str,
        "Scope": Literal["Availability Zone", "Region"],
    },
    total=False,
)

ReservedInstancesIdTypeDef = TypedDict(
    "ReservedInstancesIdTypeDef", {"ReservedInstancesId": str}, total=False
)

ReservedInstancesListingTypeDef = TypedDict(
    "ReservedInstancesListingTypeDef",
    {
        "ClientToken": str,
        "CreateDate": datetime,
        "InstanceCounts": List["InstanceCountTypeDef"],
        "PriceSchedules": List["PriceScheduleTypeDef"],
        "ReservedInstancesId": str,
        "ReservedInstancesListingId": str,
        "Status": Literal["active", "pending", "cancelled", "closed"],
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
        "UpdateDate": datetime,
    },
    total=False,
)

ReservedInstancesModificationResultTypeDef = TypedDict(
    "ReservedInstancesModificationResultTypeDef",
    {"ReservedInstancesId": str, "TargetConfiguration": "ReservedInstancesConfigurationTypeDef"},
    total=False,
)

ReservedInstancesModificationTypeDef = TypedDict(
    "ReservedInstancesModificationTypeDef",
    {
        "ClientToken": str,
        "CreateDate": datetime,
        "EffectiveDate": datetime,
        "ModificationResults": List["ReservedInstancesModificationResultTypeDef"],
        "ReservedInstancesIds": List["ReservedInstancesIdTypeDef"],
        "ReservedInstancesModificationId": str,
        "Status": str,
        "StatusMessage": str,
        "UpdateDate": datetime,
    },
    total=False,
)

ReservedInstancesOfferingTypeDef = TypedDict(
    "ReservedInstancesOfferingTypeDef",
    {
        "AvailabilityZone": str,
        "Duration": int,
        "FixedPrice": float,
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "ProductDescription": Literal[
            "Linux/UNIX", "Linux/UNIX (Amazon VPC)", "Windows", "Windows (Amazon VPC)"
        ],
        "ReservedInstancesOfferingId": str,
        "UsagePrice": float,
        "CurrencyCode": Literal["USD"],
        "InstanceTenancy": Literal["default", "dedicated", "host"],
        "Marketplace": bool,
        "OfferingClass": Literal["standard", "convertible"],
        "OfferingType": Literal[
            "Heavy Utilization",
            "Medium Utilization",
            "Light Utilization",
            "No Upfront",
            "Partial Upfront",
            "All Upfront",
        ],
        "PricingDetails": List["PricingDetailTypeDef"],
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "Scope": Literal["Availability Zone", "Region"],
    },
    total=False,
)

ReservedInstancesTypeDef = TypedDict(
    "ReservedInstancesTypeDef",
    {
        "AvailabilityZone": str,
        "Duration": int,
        "End": datetime,
        "FixedPrice": float,
        "InstanceCount": int,
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "ProductDescription": Literal[
            "Linux/UNIX", "Linux/UNIX (Amazon VPC)", "Windows", "Windows (Amazon VPC)"
        ],
        "ReservedInstancesId": str,
        "Start": datetime,
        "State": Literal[
            "payment-pending", "active", "payment-failed", "retired", "queued", "queued-deleted"
        ],
        "UsagePrice": float,
        "CurrencyCode": Literal["USD"],
        "InstanceTenancy": Literal["default", "dedicated", "host"],
        "OfferingClass": Literal["standard", "convertible"],
        "OfferingType": Literal[
            "Heavy Utilization",
            "Medium Utilization",
            "Light Utilization",
            "No Upfront",
            "Partial Upfront",
            "All Upfront",
        ],
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "Scope": Literal["Availability Zone", "Region"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ResponseErrorTypeDef = TypedDict(
    "ResponseErrorTypeDef",
    {
        "Code": Literal[
            "launchTemplateIdDoesNotExist",
            "launchTemplateIdMalformed",
            "launchTemplateNameDoesNotExist",
            "launchTemplateNameMalformed",
            "launchTemplateVersionDoesNotExist",
            "unexpectedError",
        ],
        "Message": str,
    },
    total=False,
)

ResponseLaunchTemplateDataTypeDef = TypedDict(
    "ResponseLaunchTemplateDataTypeDef",
    {
        "KernelId": str,
        "EbsOptimized": bool,
        "IamInstanceProfile": "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
        "BlockDeviceMappings": List["LaunchTemplateBlockDeviceMappingTypeDef"],
        "NetworkInterfaces": List["LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef"],
        "ImageId": str,
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "KeyName": str,
        "Monitoring": "LaunchTemplatesMonitoringTypeDef",
        "Placement": "LaunchTemplatePlacementTypeDef",
        "RamDiskId": str,
        "DisableApiTermination": bool,
        "InstanceInitiatedShutdownBehavior": Literal["stop", "terminate"],
        "UserData": str,
        "TagSpecifications": List["LaunchTemplateTagSpecificationTypeDef"],
        "ElasticGpuSpecifications": List["ElasticGpuSpecificationResponseTypeDef"],
        "ElasticInferenceAccelerators": List[
            "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef"
        ],
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "InstanceMarketOptions": "LaunchTemplateInstanceMarketOptionsTypeDef",
        "CreditSpecification": "CreditSpecificationTypeDef",
        "CpuOptions": "LaunchTemplateCpuOptionsTypeDef",
        "CapacityReservationSpecification": "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
        "LicenseSpecifications": List["LaunchTemplateLicenseConfigurationTypeDef"],
        "HibernationOptions": "LaunchTemplateHibernationOptionsTypeDef",
        "MetadataOptions": "LaunchTemplateInstanceMetadataOptionsTypeDef",
    },
    total=False,
)

RouteTableAssociationStateTypeDef = TypedDict(
    "RouteTableAssociationStateTypeDef",
    {
        "State": Literal["associating", "associated", "disassociating", "disassociated", "failed"],
        "StatusMessage": str,
    },
    total=False,
)

RouteTableAssociationTypeDef = TypedDict(
    "RouteTableAssociationTypeDef",
    {
        "Main": bool,
        "RouteTableAssociationId": str,
        "RouteTableId": str,
        "SubnetId": str,
        "GatewayId": str,
        "AssociationState": "RouteTableAssociationStateTypeDef",
    },
    total=False,
)

RouteTableTypeDef = TypedDict(
    "RouteTableTypeDef",
    {
        "Associations": List["RouteTableAssociationTypeDef"],
        "PropagatingVgws": List["PropagatingVgwTypeDef"],
        "RouteTableId": str,
        "Routes": List["RouteTypeDef"],
        "Tags": List["TagTypeDef"],
        "VpcId": str,
        "OwnerId": str,
    },
    total=False,
)

RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "Origin": Literal["CreateRouteTable", "CreateRoute", "EnableVgwRoutePropagation"],
        "State": Literal["active", "blackhole"],
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

RunInstancesMonitoringEnabledTypeDef = TypedDict(
    "RunInstancesMonitoringEnabledTypeDef", {"Enabled": bool}
)

S3StorageTypeDef = TypedDict(
    "S3StorageTypeDef",
    {
        "AWSAccessKeyId": str,
        "Bucket": str,
        "Prefix": str,
        "UploadPolicy": bytes,
        "UploadPolicySignature": str,
    },
    total=False,
)

ScheduledInstanceAvailabilityTypeDef = TypedDict(
    "ScheduledInstanceAvailabilityTypeDef",
    {
        "AvailabilityZone": str,
        "AvailableInstanceCount": int,
        "FirstSlotStartTime": datetime,
        "HourlyPrice": str,
        "InstanceType": str,
        "MaxTermDurationInDays": int,
        "MinTermDurationInDays": int,
        "NetworkPlatform": str,
        "Platform": str,
        "PurchaseToken": str,
        "Recurrence": "ScheduledInstanceRecurrenceTypeDef",
        "SlotDurationInHours": int,
        "TotalScheduledInstanceHours": int,
    },
    total=False,
)

ScheduledInstanceRecurrenceTypeDef = TypedDict(
    "ScheduledInstanceRecurrenceTypeDef",
    {
        "Frequency": str,
        "Interval": int,
        "OccurrenceDaySet": List[int],
        "OccurrenceRelativeToEnd": bool,
        "OccurrenceUnit": str,
    },
    total=False,
)

ScheduledInstanceTypeDef = TypedDict(
    "ScheduledInstanceTypeDef",
    {
        "AvailabilityZone": str,
        "CreateDate": datetime,
        "HourlyPrice": str,
        "InstanceCount": int,
        "InstanceType": str,
        "NetworkPlatform": str,
        "NextSlotStartTime": datetime,
        "Platform": str,
        "PreviousSlotEndTime": datetime,
        "Recurrence": "ScheduledInstanceRecurrenceTypeDef",
        "ScheduledInstanceId": str,
        "SlotDurationInHours": int,
        "TermEndDate": datetime,
        "TermStartDate": datetime,
        "TotalScheduledInstanceHours": int,
    },
    total=False,
)

ScheduledInstancesBlockDeviceMappingTypeDef = TypedDict(
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    {"DeviceName": str, "Ebs": "ScheduledInstancesEbsTypeDef", "NoDevice": str, "VirtualName": str},
    total=False,
)

ScheduledInstancesEbsTypeDef = TypedDict(
    "ScheduledInstancesEbsTypeDef",
    {
        "DeleteOnTermination": bool,
        "Encrypted": bool,
        "Iops": int,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
    },
    total=False,
)

ScheduledInstancesIamInstanceProfileTypeDef = TypedDict(
    "ScheduledInstancesIamInstanceProfileTypeDef", {"Arn": str, "Name": str}, total=False
)

ScheduledInstancesIpv6AddressTypeDef = TypedDict(
    "ScheduledInstancesIpv6AddressTypeDef", {"Ipv6Address": str}, total=False
)

ScheduledInstancesMonitoringTypeDef = TypedDict(
    "ScheduledInstancesMonitoringTypeDef", {"Enabled": bool}, total=False
)

ScheduledInstancesNetworkInterfaceTypeDef = TypedDict(
    "ScheduledInstancesNetworkInterfaceTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["ScheduledInstancesIpv6AddressTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddressConfigs": List["ScheduledInstancesPrivateIpAddressConfigTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
    },
    total=False,
)

ScheduledInstancesPlacementTypeDef = TypedDict(
    "ScheduledInstancesPlacementTypeDef", {"AvailabilityZone": str, "GroupName": str}, total=False
)

ScheduledInstancesPrivateIpAddressConfigTypeDef = TypedDict(
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    {"Primary": bool, "PrivateIpAddress": str},
    total=False,
)

SecurityGroupIdentifierTypeDef = TypedDict(
    "SecurityGroupIdentifierTypeDef", {"GroupId": str, "GroupName": str}, total=False
)

SecurityGroupReferenceTypeDef = TypedDict(
    "SecurityGroupReferenceTypeDef",
    {"GroupId": str, "ReferencingVpcId": str, "VpcPeeringConnectionId": str},
    total=False,
)

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "Description": str,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "OwnerId": str,
        "GroupId": str,
        "IpPermissionsEgress": List["IpPermissionTypeDef"],
        "Tags": List["TagTypeDef"],
        "VpcId": str,
    },
    total=False,
)

ServiceConfigurationTypeDef = TypedDict(
    "ServiceConfigurationTypeDef",
    {
        "ServiceType": List["ServiceTypeDetailTypeDef"],
        "ServiceId": str,
        "ServiceName": str,
        "ServiceState": Literal["Pending", "Available", "Deleting", "Deleted", "Failed"],
        "AvailabilityZones": List[str],
        "AcceptanceRequired": bool,
        "ManagesVpcEndpoints": bool,
        "NetworkLoadBalancerArns": List[str],
        "BaseEndpointDnsNames": List[str],
        "PrivateDnsName": str,
        "PrivateDnsNameConfiguration": "PrivateDnsNameConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ServiceDetailTypeDef = TypedDict(
    "ServiceDetailTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceType": List["ServiceTypeDetailTypeDef"],
        "AvailabilityZones": List[str],
        "Owner": str,
        "BaseEndpointDnsNames": List[str],
        "PrivateDnsName": str,
        "VpcEndpointPolicySupported": bool,
        "AcceptanceRequired": bool,
        "ManagesVpcEndpoints": bool,
        "Tags": List["TagTypeDef"],
        "PrivateDnsNameVerificationState": Literal["pendingVerification", "verified", "failed"],
    },
    total=False,
)

ServiceTypeDetailTypeDef = TypedDict(
    "ServiceTypeDetailTypeDef", {"ServiceType": Literal["Interface", "Gateway"]}, total=False
)

SnapshotDetailTypeDef = TypedDict(
    "SnapshotDetailTypeDef",
    {
        "Description": str,
        "DeviceName": str,
        "DiskImageSize": float,
        "Format": str,
        "Progress": str,
        "SnapshotId": str,
        "Status": str,
        "StatusMessage": str,
        "Url": str,
        "UserBucket": "UserBucketDetailsTypeDef",
    },
    total=False,
)

SnapshotInfoTypeDef = TypedDict(
    "SnapshotInfoTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "Encrypted": bool,
        "VolumeId": str,
        "State": Literal["pending", "completed", "error"],
        "VolumeSize": int,
        "StartTime": datetime,
        "Progress": str,
        "OwnerId": str,
        "SnapshotId": str,
    },
    total=False,
)

SnapshotTaskDetailTypeDef = TypedDict(
    "SnapshotTaskDetailTypeDef",
    {
        "Description": str,
        "DiskImageSize": float,
        "Encrypted": bool,
        "Format": str,
        "KmsKeyId": str,
        "Progress": str,
        "SnapshotId": str,
        "Status": str,
        "StatusMessage": str,
        "Url": str,
        "UserBucket": "UserBucketDetailsTypeDef",
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DataEncryptionKeyId": str,
        "Description": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OwnerId": str,
        "Progress": str,
        "SnapshotId": str,
        "StartTime": datetime,
        "State": Literal["pending", "completed", "error"],
        "StateMessage": str,
        "VolumeId": str,
        "VolumeSize": int,
        "OwnerAlias": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SpotDatafeedSubscriptionTypeDef = TypedDict(
    "SpotDatafeedSubscriptionTypeDef",
    {
        "Bucket": str,
        "Fault": "SpotInstanceStateFaultTypeDef",
        "OwnerId": str,
        "Prefix": str,
        "State": Literal["Active", "Inactive"],
    },
    total=False,
)

SpotFleetLaunchSpecificationTypeDef = TypedDict(
    "SpotFleetLaunchSpecificationTypeDef",
    {
        "SecurityGroups": List["GroupIdentifierTypeDef"],
        "AddressingType": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "ImageId": str,
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "SpotFleetMonitoringTypeDef",
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "Placement": "SpotPlacementTypeDef",
        "RamdiskId": str,
        "SpotPrice": str,
        "SubnetId": str,
        "UserData": str,
        "WeightedCapacity": float,
        "TagSpecifications": List["SpotFleetTagSpecificationTypeDef"],
    },
    total=False,
)

SpotFleetMonitoringTypeDef = TypedDict("SpotFleetMonitoringTypeDef", {"Enabled": bool}, total=False)

_RequiredSpotFleetRequestConfigDataTypeDef = TypedDict(
    "_RequiredSpotFleetRequestConfigDataTypeDef", {"IamFleetRole": str, "TargetCapacity": int}
)
_OptionalSpotFleetRequestConfigDataTypeDef = TypedDict(
    "_OptionalSpotFleetRequestConfigDataTypeDef",
    {
        "AllocationStrategy": Literal["lowestPrice", "diversified", "capacityOptimized"],
        "OnDemandAllocationStrategy": Literal["lowestPrice", "prioritized"],
        "ClientToken": str,
        "ExcessCapacityTerminationPolicy": Literal["noTermination", "default"],
        "FulfilledCapacity": float,
        "OnDemandFulfilledCapacity": float,
        "LaunchSpecifications": List["SpotFleetLaunchSpecificationTypeDef"],
        "LaunchTemplateConfigs": List["LaunchTemplateConfigTypeDef"],
        "SpotPrice": str,
        "OnDemandTargetCapacity": int,
        "OnDemandMaxTotalPrice": str,
        "SpotMaxTotalPrice": str,
        "TerminateInstancesWithExpiration": bool,
        "Type": Literal["request", "maintain", "instant"],
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "ReplaceUnhealthyInstances": bool,
        "InstanceInterruptionBehavior": Literal["hibernate", "stop", "terminate"],
        "LoadBalancersConfig": "LoadBalancersConfigTypeDef",
        "InstancePoolsToUseCount": int,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class SpotFleetRequestConfigDataTypeDef(
    _RequiredSpotFleetRequestConfigDataTypeDef, _OptionalSpotFleetRequestConfigDataTypeDef
):
    pass


SpotFleetRequestConfigTypeDef = TypedDict(
    "SpotFleetRequestConfigTypeDef",
    {
        "ActivityStatus": Literal[
            "error", "pending_fulfillment", "pending_termination", "fulfilled"
        ],
        "CreateTime": datetime,
        "SpotFleetRequestConfig": "SpotFleetRequestConfigDataTypeDef",
        "SpotFleetRequestId": str,
        "SpotFleetRequestState": Literal[
            "submitted",
            "active",
            "cancelled",
            "failed",
            "cancelled_running",
            "cancelled_terminating",
            "modifying",
        ],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SpotFleetTagSpecificationTypeDef = TypedDict(
    "SpotFleetTagSpecificationTypeDef",
    {
        "ResourceType": Literal[
            "client-vpn-endpoint",
            "customer-gateway",
            "dedicated-host",
            "dhcp-options",
            "elastic-ip",
            "elastic-gpu",
            "export-image-task",
            "export-instance-task",
            "fleet",
            "fpga-image",
            "host-reservation",
            "image",
            "import-image-task",
            "import-snapshot-task",
            "instance",
            "internet-gateway",
            "key-pair",
            "launch-template",
            "local-gateway-route-table-vpc-association",
            "natgateway",
            "network-acl",
            "network-interface",
            "placement-group",
            "reserved-instances",
            "route-table",
            "security-group",
            "snapshot",
            "spot-fleet-request",
            "spot-instances-request",
            "subnet",
            "traffic-mirror-filter",
            "traffic-mirror-session",
            "traffic-mirror-target",
            "transit-gateway",
            "transit-gateway-attachment",
            "transit-gateway-multicast-domain",
            "transit-gateway-route-table",
            "volume",
            "vpc",
            "vpc-peering-connection",
            "vpn-connection",
            "vpn-gateway",
            "vpc-flow-log",
        ],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SpotInstanceRequestTypeDef = TypedDict(
    "SpotInstanceRequestTypeDef",
    {
        "ActualBlockHourlyPrice": str,
        "AvailabilityZoneGroup": str,
        "BlockDurationMinutes": int,
        "CreateTime": datetime,
        "Fault": "SpotInstanceStateFaultTypeDef",
        "InstanceId": str,
        "LaunchGroup": str,
        "LaunchSpecification": "LaunchSpecificationTypeDef",
        "LaunchedAvailabilityZone": str,
        "ProductDescription": Literal[
            "Linux/UNIX", "Linux/UNIX (Amazon VPC)", "Windows", "Windows (Amazon VPC)"
        ],
        "SpotInstanceRequestId": str,
        "SpotPrice": str,
        "State": Literal["open", "active", "closed", "cancelled", "failed"],
        "Status": "SpotInstanceStatusTypeDef",
        "Tags": List["TagTypeDef"],
        "Type": Literal["one-time", "persistent"],
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "InstanceInterruptionBehavior": Literal["hibernate", "stop", "terminate"],
    },
    total=False,
)

SpotInstanceStateFaultTypeDef = TypedDict(
    "SpotInstanceStateFaultTypeDef", {"Code": str, "Message": str}, total=False
)

SpotInstanceStatusTypeDef = TypedDict(
    "SpotInstanceStatusTypeDef", {"Code": str, "Message": str, "UpdateTime": datetime}, total=False
)

SpotMarketOptionsTypeDef = TypedDict(
    "SpotMarketOptionsTypeDef",
    {
        "MaxPrice": str,
        "SpotInstanceType": Literal["one-time", "persistent"],
        "BlockDurationMinutes": int,
        "ValidUntil": datetime,
        "InstanceInterruptionBehavior": Literal["hibernate", "stop", "terminate"],
    },
    total=False,
)

SpotOptionsTypeDef = TypedDict(
    "SpotOptionsTypeDef",
    {
        "AllocationStrategy": Literal["lowest-price", "diversified", "capacity-optimized"],
        "InstanceInterruptionBehavior": Literal["hibernate", "stop", "terminate"],
        "InstancePoolsToUseCount": int,
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

SpotPlacementTypeDef = TypedDict(
    "SpotPlacementTypeDef",
    {"AvailabilityZone": str, "GroupName": str, "Tenancy": Literal["default", "dedicated", "host"]},
    total=False,
)

SpotPriceTypeDef = TypedDict(
    "SpotPriceTypeDef",
    {
        "AvailabilityZone": str,
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "ProductDescription": Literal[
            "Linux/UNIX", "Linux/UNIX (Amazon VPC)", "Windows", "Windows (Amazon VPC)"
        ],
        "SpotPrice": str,
        "Timestamp": datetime,
    },
    total=False,
)

StaleIpPermissionTypeDef = TypedDict(
    "StaleIpPermissionTypeDef",
    {
        "FromPort": int,
        "IpProtocol": str,
        "IpRanges": List[str],
        "PrefixListIds": List[str],
        "ToPort": int,
        "UserIdGroupPairs": List["UserIdGroupPairTypeDef"],
    },
    total=False,
)

StaleSecurityGroupTypeDef = TypedDict(
    "StaleSecurityGroupTypeDef",
    {
        "Description": str,
        "GroupId": str,
        "GroupName": str,
        "StaleIpPermissions": List["StaleIpPermissionTypeDef"],
        "StaleIpPermissionsEgress": List["StaleIpPermissionTypeDef"],
        "VpcId": str,
    },
    total=False,
)

StateReasonTypeDef = TypedDict("StateReasonTypeDef", {"Code": str, "Message": str}, total=False)

StorageTypeDef = TypedDict("StorageTypeDef", {"S3": "S3StorageTypeDef"}, total=False)

SubnetAssociationTypeDef = TypedDict(
    "SubnetAssociationTypeDef",
    {
        "SubnetId": str,
        "State": Literal["associating", "associated", "disassociating", "disassociated"],
    },
    total=False,
)

SubnetCidrBlockStateTypeDef = TypedDict(
    "SubnetCidrBlockStateTypeDef",
    {
        "State": Literal[
            "associating", "associated", "disassociating", "disassociated", "failing", "failed"
        ],
        "StatusMessage": str,
    },
    total=False,
)

SubnetIpv6CidrBlockAssociationTypeDef = TypedDict(
    "SubnetIpv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "Ipv6CidrBlock": str,
        "Ipv6CidrBlockState": "SubnetCidrBlockStateTypeDef",
    },
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "AvailableIpAddressCount": int,
        "CidrBlock": str,
        "DefaultForAz": bool,
        "MapPublicIpOnLaunch": bool,
        "MapCustomerOwnedIpOnLaunch": bool,
        "CustomerOwnedIpv4Pool": str,
        "State": Literal["pending", "available"],
        "SubnetId": str,
        "VpcId": str,
        "OwnerId": str,
        "AssignIpv6AddressOnCreation": bool,
        "Ipv6CidrBlockAssociationSet": List["SubnetIpv6CidrBlockAssociationTypeDef"],
        "Tags": List["TagTypeDef"],
        "SubnetArn": str,
        "OutpostArn": str,
    },
    total=False,
)

SuccessfulInstanceCreditSpecificationItemTypeDef = TypedDict(
    "SuccessfulInstanceCreditSpecificationItemTypeDef", {"InstanceId": str}, total=False
)

SuccessfulQueuedPurchaseDeletionTypeDef = TypedDict(
    "SuccessfulQueuedPurchaseDeletionTypeDef", {"ReservedInstancesId": str}, total=False
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "Key": str,
        "ResourceId": str,
        "ResourceType": Literal[
            "client-vpn-endpoint",
            "customer-gateway",
            "dedicated-host",
            "dhcp-options",
            "elastic-ip",
            "elastic-gpu",
            "export-image-task",
            "export-instance-task",
            "fleet",
            "fpga-image",
            "host-reservation",
            "image",
            "import-image-task",
            "import-snapshot-task",
            "instance",
            "internet-gateway",
            "key-pair",
            "launch-template",
            "local-gateway-route-table-vpc-association",
            "natgateway",
            "network-acl",
            "network-interface",
            "placement-group",
            "reserved-instances",
            "route-table",
            "security-group",
            "snapshot",
            "spot-fleet-request",
            "spot-instances-request",
            "subnet",
            "traffic-mirror-filter",
            "traffic-mirror-session",
            "traffic-mirror-target",
            "transit-gateway",
            "transit-gateway-attachment",
            "transit-gateway-multicast-domain",
            "transit-gateway-route-table",
            "volume",
            "vpc",
            "vpc-peering-connection",
            "vpn-connection",
            "vpn-gateway",
            "vpc-flow-log",
        ],
        "Value": str,
    },
    total=False,
)

TagSpecificationTypeDef = TypedDict(
    "TagSpecificationTypeDef",
    {
        "ResourceType": Literal[
            "client-vpn-endpoint",
            "customer-gateway",
            "dedicated-host",
            "dhcp-options",
            "elastic-ip",
            "elastic-gpu",
            "export-image-task",
            "export-instance-task",
            "fleet",
            "fpga-image",
            "host-reservation",
            "image",
            "import-image-task",
            "import-snapshot-task",
            "instance",
            "internet-gateway",
            "key-pair",
            "launch-template",
            "local-gateway-route-table-vpc-association",
            "natgateway",
            "network-acl",
            "network-interface",
            "placement-group",
            "reserved-instances",
            "route-table",
            "security-group",
            "snapshot",
            "spot-fleet-request",
            "spot-instances-request",
            "subnet",
            "traffic-mirror-filter",
            "traffic-mirror-session",
            "traffic-mirror-target",
            "transit-gateway",
            "transit-gateway-attachment",
            "transit-gateway-multicast-domain",
            "transit-gateway-route-table",
            "volume",
            "vpc",
            "vpc-peering-connection",
            "vpn-connection",
            "vpn-gateway",
            "vpc-flow-log",
        ],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TargetCapacitySpecificationTypeDef = TypedDict(
    "TargetCapacitySpecificationTypeDef",
    {
        "TotalTargetCapacity": int,
        "OnDemandTargetCapacity": int,
        "SpotTargetCapacity": int,
        "DefaultTargetCapacityType": Literal["spot", "on-demand"],
    },
    total=False,
)

TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef", {"InstanceCount": int, "OfferingId": str}, total=False
)

TargetGroupTypeDef = TypedDict("TargetGroupTypeDef", {"Arn": str}, total=False)

TargetGroupsConfigTypeDef = TypedDict(
    "TargetGroupsConfigTypeDef", {"TargetGroups": List["TargetGroupTypeDef"]}, total=False
)

TargetNetworkTypeDef = TypedDict(
    "TargetNetworkTypeDef",
    {
        "AssociationId": str,
        "VpcId": str,
        "TargetNetworkId": str,
        "ClientVpnEndpointId": str,
        "Status": "AssociationStatusTypeDef",
        "SecurityGroups": List[str],
    },
    total=False,
)

TargetReservationValueTypeDef = TypedDict(
    "TargetReservationValueTypeDef",
    {
        "ReservationValue": "ReservationValueTypeDef",
        "TargetConfiguration": "TargetConfigurationTypeDef",
    },
    total=False,
)

TerminateConnectionStatusTypeDef = TypedDict(
    "TerminateConnectionStatusTypeDef",
    {
        "ConnectionId": str,
        "PreviousStatus": "ClientVpnConnectionStatusTypeDef",
        "CurrentStatus": "ClientVpnConnectionStatusTypeDef",
    },
    total=False,
)

TrafficMirrorFilterRuleTypeDef = TypedDict(
    "TrafficMirrorFilterRuleTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "TrafficMirrorFilterId": str,
        "TrafficDirection": Literal["ingress", "egress"],
        "RuleNumber": int,
        "RuleAction": Literal["accept", "reject"],
        "Protocol": int,
        "DestinationPortRange": "TrafficMirrorPortRangeTypeDef",
        "SourcePortRange": "TrafficMirrorPortRangeTypeDef",
        "DestinationCidrBlock": str,
        "SourceCidrBlock": str,
        "Description": str,
    },
    total=False,
)

TrafficMirrorFilterTypeDef = TypedDict(
    "TrafficMirrorFilterTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "IngressFilterRules": List["TrafficMirrorFilterRuleTypeDef"],
        "EgressFilterRules": List["TrafficMirrorFilterRuleTypeDef"],
        "NetworkServices": List[Literal["amazon-dns"]],
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TrafficMirrorPortRangeTypeDef = TypedDict(
    "TrafficMirrorPortRangeTypeDef", {"FromPort": int, "ToPort": int}, total=False
)

TrafficMirrorSessionTypeDef = TypedDict(
    "TrafficMirrorSessionTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "TrafficMirrorTargetId": str,
        "TrafficMirrorFilterId": str,
        "NetworkInterfaceId": str,
        "OwnerId": str,
        "PacketLength": int,
        "SessionNumber": int,
        "VirtualNetworkId": int,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TrafficMirrorTargetTypeDef = TypedDict(
    "TrafficMirrorTargetTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "NetworkInterfaceId": str,
        "NetworkLoadBalancerArn": str,
        "Type": Literal["network-interface", "network-load-balancer"],
        "Description": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayAssociationTypeDef = TypedDict(
    "TransitGatewayAssociationTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": Literal["vpc", "vpn", "direct-connect-gateway", "tgw-peering"],
        "State": Literal["associating", "associated", "disassociating", "disassociated"],
    },
    total=False,
)

TransitGatewayAttachmentAssociationTypeDef = TypedDict(
    "TransitGatewayAttachmentAssociationTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "State": Literal["associating", "associated", "disassociating", "disassociated"],
    },
    total=False,
)

TransitGatewayAttachmentPropagationTypeDef = TypedDict(
    "TransitGatewayAttachmentPropagationTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "State": Literal["enabling", "enabled", "disabling", "disabled"],
    },
    total=False,
)

TransitGatewayAttachmentTypeDef = TypedDict(
    "TransitGatewayAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "TransitGatewayId": str,
        "TransitGatewayOwnerId": str,
        "ResourceOwnerId": str,
        "ResourceType": Literal["vpc", "vpn", "direct-connect-gateway", "tgw-peering"],
        "ResourceId": str,
        "State": Literal[
            "initiating",
            "pendingAcceptance",
            "rollingBack",
            "pending",
            "available",
            "modifying",
            "deleting",
            "deleted",
            "failed",
            "rejected",
            "rejecting",
            "failing",
        ],
        "Association": "TransitGatewayAttachmentAssociationTypeDef",
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayMulticastDeregisteredGroupMembersTypeDef = TypedDict(
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "DeregisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayMulticastDeregisteredGroupSourcesTypeDef = TypedDict(
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "DeregisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayMulticastDomainAssociationTypeDef = TypedDict(
    "TransitGatewayMulticastDomainAssociationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": Literal["vpc", "vpn", "direct-connect-gateway", "tgw-peering"],
        "Subnet": "SubnetAssociationTypeDef",
    },
    total=False,
)

TransitGatewayMulticastDomainAssociationsTypeDef = TypedDict(
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": Literal["vpc", "vpn", "direct-connect-gateway", "tgw-peering"],
        "Subnets": List["SubnetAssociationTypeDef"],
    },
    total=False,
)

TransitGatewayMulticastDomainTypeDef = TypedDict(
    "TransitGatewayMulticastDomainTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayId": str,
        "State": Literal["pending", "available", "deleting", "deleted"],
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayMulticastGroupTypeDef = TypedDict(
    "TransitGatewayMulticastGroupTypeDef",
    {
        "GroupIpAddress": str,
        "TransitGatewayAttachmentId": str,
        "SubnetId": str,
        "ResourceId": str,
        "ResourceType": Literal["vpc", "vpn", "direct-connect-gateway", "tgw-peering"],
        "NetworkInterfaceId": str,
        "GroupMember": bool,
        "GroupSource": bool,
        "MemberType": Literal["static", "igmp"],
        "SourceType": Literal["static", "igmp"],
    },
    total=False,
)

TransitGatewayMulticastRegisteredGroupMembersTypeDef = TypedDict(
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "RegisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayMulticastRegisteredGroupSourcesTypeDef = TypedDict(
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "RegisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayOptionsTypeDef = TypedDict(
    "TransitGatewayOptionsTypeDef",
    {
        "AmazonSideAsn": int,
        "AutoAcceptSharedAttachments": Literal["enable", "disable"],
        "DefaultRouteTableAssociation": Literal["enable", "disable"],
        "AssociationDefaultRouteTableId": str,
        "DefaultRouteTablePropagation": Literal["enable", "disable"],
        "PropagationDefaultRouteTableId": str,
        "VpnEcmpSupport": Literal["enable", "disable"],
        "DnsSupport": Literal["enable", "disable"],
        "MulticastSupport": Literal["enable", "disable"],
    },
    total=False,
)

TransitGatewayPeeringAttachmentTypeDef = TypedDict(
    "TransitGatewayPeeringAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "RequesterTgwInfo": "PeeringTgwInfoTypeDef",
        "AccepterTgwInfo": "PeeringTgwInfoTypeDef",
        "Status": "PeeringAttachmentStatusTypeDef",
        "State": Literal[
            "initiating",
            "pendingAcceptance",
            "rollingBack",
            "pending",
            "available",
            "modifying",
            "deleting",
            "deleted",
            "failed",
            "rejected",
            "rejecting",
            "failing",
        ],
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayPropagationTypeDef = TypedDict(
    "TransitGatewayPropagationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": Literal["vpc", "vpn", "direct-connect-gateway", "tgw-peering"],
        "TransitGatewayRouteTableId": str,
        "State": Literal["enabling", "enabled", "disabling", "disabled"],
    },
    total=False,
)

TransitGatewayRouteAttachmentTypeDef = TypedDict(
    "TransitGatewayRouteAttachmentTypeDef",
    {
        "ResourceId": str,
        "TransitGatewayAttachmentId": str,
        "ResourceType": Literal["vpc", "vpn", "direct-connect-gateway", "tgw-peering"],
    },
    total=False,
)

TransitGatewayRouteTableAssociationTypeDef = TypedDict(
    "TransitGatewayRouteTableAssociationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": Literal["vpc", "vpn", "direct-connect-gateway", "tgw-peering"],
        "State": Literal["associating", "associated", "disassociating", "disassociated"],
    },
    total=False,
)

TransitGatewayRouteTablePropagationTypeDef = TypedDict(
    "TransitGatewayRouteTablePropagationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": Literal["vpc", "vpn", "direct-connect-gateway", "tgw-peering"],
        "State": Literal["enabling", "enabled", "disabling", "disabled"],
    },
    total=False,
)

TransitGatewayRouteTableTypeDef = TypedDict(
    "TransitGatewayRouteTableTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayId": str,
        "State": Literal["pending", "available", "deleting", "deleted"],
        "DefaultAssociationRouteTable": bool,
        "DefaultPropagationRouteTable": bool,
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayRouteTypeDef = TypedDict(
    "TransitGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "TransitGatewayAttachments": List["TransitGatewayRouteAttachmentTypeDef"],
        "Type": Literal["static", "propagated"],
        "State": Literal["pending", "active", "blackhole", "deleting", "deleted"],
    },
    total=False,
)

TransitGatewayTypeDef = TypedDict(
    "TransitGatewayTypeDef",
    {
        "TransitGatewayId": str,
        "TransitGatewayArn": str,
        "State": Literal["pending", "available", "modifying", "deleting", "deleted"],
        "OwnerId": str,
        "Description": str,
        "CreationTime": datetime,
        "Options": "TransitGatewayOptionsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayVpcAttachmentOptionsTypeDef = TypedDict(
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    {"DnsSupport": Literal["enable", "disable"], "Ipv6Support": Literal["enable", "disable"]},
    total=False,
)

TransitGatewayVpcAttachmentTypeDef = TypedDict(
    "TransitGatewayVpcAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "TransitGatewayId": str,
        "VpcId": str,
        "VpcOwnerId": str,
        "State": Literal[
            "initiating",
            "pendingAcceptance",
            "rollingBack",
            "pending",
            "available",
            "modifying",
            "deleting",
            "deleted",
            "failed",
            "rejected",
            "rejecting",
            "failing",
        ],
        "SubnetIds": List[str],
        "CreationTime": datetime,
        "Options": "TransitGatewayVpcAttachmentOptionsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TunnelOptionTypeDef = TypedDict(
    "TunnelOptionTypeDef",
    {
        "OutsideIpAddress": str,
        "TunnelInsideCidr": str,
        "TunnelInsideIpv6Cidr": str,
        "PreSharedKey": str,
        "Phase1LifetimeSeconds": int,
        "Phase2LifetimeSeconds": int,
        "RekeyMarginTimeSeconds": int,
        "RekeyFuzzPercentage": int,
        "ReplayWindowSize": int,
        "DpdTimeoutSeconds": int,
        "Phase1EncryptionAlgorithms": List["Phase1EncryptionAlgorithmsListValueTypeDef"],
        "Phase2EncryptionAlgorithms": List["Phase2EncryptionAlgorithmsListValueTypeDef"],
        "Phase1IntegrityAlgorithms": List["Phase1IntegrityAlgorithmsListValueTypeDef"],
        "Phase2IntegrityAlgorithms": List["Phase2IntegrityAlgorithmsListValueTypeDef"],
        "Phase1DHGroupNumbers": List["Phase1DHGroupNumbersListValueTypeDef"],
        "Phase2DHGroupNumbers": List["Phase2DHGroupNumbersListValueTypeDef"],
        "IkeVersions": List["IKEVersionsListValueTypeDef"],
    },
    total=False,
)

UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef = TypedDict(
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    {
        "Code": Literal[
            "InvalidInstanceID.Malformed",
            "InvalidInstanceID.NotFound",
            "IncorrectInstanceState",
            "InstanceCreditSpecification.NotSupported",
        ],
        "Message": str,
    },
    total=False,
)

UnsuccessfulInstanceCreditSpecificationItemTypeDef = TypedDict(
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    {"InstanceId": str, "Error": "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef"},
    total=False,
)

UnsuccessfulItemErrorTypeDef = TypedDict(
    "UnsuccessfulItemErrorTypeDef", {"Code": str, "Message": str}, total=False
)

UnsuccessfulItemTypeDef = TypedDict(
    "UnsuccessfulItemTypeDef",
    {"Error": "UnsuccessfulItemErrorTypeDef", "ResourceId": str},
    total=False,
)

UserBucketDetailsTypeDef = TypedDict(
    "UserBucketDetailsTypeDef", {"S3Bucket": str, "S3Key": str}, total=False
)

UserBucketTypeDef = TypedDict("UserBucketTypeDef", {"S3Bucket": str, "S3Key": str}, total=False)

UserDataTypeDef = TypedDict("UserDataTypeDef", {"Data": str}, total=False)

UserIdGroupPairTypeDef = TypedDict(
    "UserIdGroupPairTypeDef",
    {
        "Description": str,
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

VCpuInfoTypeDef = TypedDict(
    "VCpuInfoTypeDef",
    {
        "DefaultVCpus": int,
        "DefaultCores": int,
        "DefaultThreadsPerCore": int,
        "ValidCores": List[int],
        "ValidThreadsPerCore": List[int],
    },
    total=False,
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef", {"Code": str, "Message": str}, total=False
)

ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef", {"Errors": List["ValidationErrorTypeDef"]}, total=False
)

VgwTelemetryTypeDef = TypedDict(
    "VgwTelemetryTypeDef",
    {
        "AcceptedRouteCount": int,
        "LastStatusChange": datetime,
        "OutsideIpAddress": str,
        "Status": Literal["UP", "DOWN"],
        "StatusMessage": str,
        "CertificateArn": str,
    },
    total=False,
)

VolumeAttachmentTypeDef = TypedDict(
    "VolumeAttachmentTypeDef",
    {
        "AttachTime": datetime,
        "Device": str,
        "InstanceId": str,
        "State": Literal["attaching", "attached", "detaching", "detached", "busy"],
        "VolumeId": str,
        "DeleteOnTermination": bool,
    },
    total=False,
)

VolumeDetailTypeDef = TypedDict("VolumeDetailTypeDef", {"Size": int})

VolumeModificationTypeDef = TypedDict(
    "VolumeModificationTypeDef",
    {
        "VolumeId": str,
        "ModificationState": Literal["modifying", "optimizing", "completed", "failed"],
        "StatusMessage": str,
        "TargetSize": int,
        "TargetIops": int,
        "TargetVolumeType": Literal["standard", "io1", "gp2", "sc1", "st1"],
        "OriginalSize": int,
        "OriginalIops": int,
        "OriginalVolumeType": Literal["standard", "io1", "gp2", "sc1", "st1"],
        "Progress": int,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

VolumeStatusActionTypeDef = TypedDict(
    "VolumeStatusActionTypeDef",
    {"Code": str, "Description": str, "EventId": str, "EventType": str},
    total=False,
)

VolumeStatusAttachmentStatusTypeDef = TypedDict(
    "VolumeStatusAttachmentStatusTypeDef", {"IoPerformance": str, "InstanceId": str}, total=False
)

VolumeStatusDetailsTypeDef = TypedDict(
    "VolumeStatusDetailsTypeDef",
    {"Name": Literal["io-enabled", "io-performance"], "Status": str},
    total=False,
)

VolumeStatusEventTypeDef = TypedDict(
    "VolumeStatusEventTypeDef",
    {
        "Description": str,
        "EventId": str,
        "EventType": str,
        "NotAfter": datetime,
        "NotBefore": datetime,
        "InstanceId": str,
    },
    total=False,
)

VolumeStatusInfoTypeDef = TypedDict(
    "VolumeStatusInfoTypeDef",
    {
        "Details": List["VolumeStatusDetailsTypeDef"],
        "Status": Literal["ok", "impaired", "insufficient-data"],
    },
    total=False,
)

VolumeStatusItemTypeDef = TypedDict(
    "VolumeStatusItemTypeDef",
    {
        "Actions": List["VolumeStatusActionTypeDef"],
        "AvailabilityZone": str,
        "OutpostArn": str,
        "Events": List["VolumeStatusEventTypeDef"],
        "VolumeId": str,
        "VolumeStatus": "VolumeStatusInfoTypeDef",
        "AttachmentStatuses": List["VolumeStatusAttachmentStatusTypeDef"],
    },
    total=False,
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "Attachments": List["VolumeAttachmentTypeDef"],
        "AvailabilityZone": str,
        "CreateTime": datetime,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OutpostArn": str,
        "Size": int,
        "SnapshotId": str,
        "State": Literal["creating", "available", "in-use", "deleting", "deleted", "error"],
        "VolumeId": str,
        "Iops": int,
        "Tags": List["TagTypeDef"],
        "VolumeType": Literal["standard", "io1", "gp2", "sc1", "st1"],
        "FastRestored": bool,
        "MultiAttachEnabled": bool,
    },
    total=False,
)

VpcAttachmentTypeDef = TypedDict(
    "VpcAttachmentTypeDef",
    {"State": Literal["attaching", "attached", "detaching", "detached"], "VpcId": str},
    total=False,
)

VpcCidrBlockAssociationTypeDef = TypedDict(
    "VpcCidrBlockAssociationTypeDef",
    {"AssociationId": str, "CidrBlock": str, "CidrBlockState": "VpcCidrBlockStateTypeDef"},
    total=False,
)

VpcCidrBlockStateTypeDef = TypedDict(
    "VpcCidrBlockStateTypeDef",
    {
        "State": Literal[
            "associating", "associated", "disassociating", "disassociated", "failing", "failed"
        ],
        "StatusMessage": str,
    },
    total=False,
)

VpcClassicLinkTypeDef = TypedDict(
    "VpcClassicLinkTypeDef",
    {"ClassicLinkEnabled": bool, "Tags": List["TagTypeDef"], "VpcId": str},
    total=False,
)

VpcEndpointConnectionTypeDef = TypedDict(
    "VpcEndpointConnectionTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointId": str,
        "VpcEndpointOwner": str,
        "VpcEndpointState": Literal[
            "PendingAcceptance",
            "Pending",
            "Available",
            "Deleting",
            "Deleted",
            "Rejected",
            "Failed",
            "Expired",
        ],
        "CreationTimestamp": datetime,
        "DnsEntries": List["DnsEntryTypeDef"],
        "NetworkLoadBalancerArns": List[str],
    },
    total=False,
)

VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": str,
        "VpcEndpointType": Literal["Interface", "Gateway"],
        "VpcId": str,
        "ServiceName": str,
        "State": Literal[
            "PendingAcceptance",
            "Pending",
            "Available",
            "Deleting",
            "Deleted",
            "Rejected",
            "Failed",
            "Expired",
        ],
        "PolicyDocument": str,
        "RouteTableIds": List[str],
        "SubnetIds": List[str],
        "Groups": List["SecurityGroupIdentifierTypeDef"],
        "PrivateDnsEnabled": bool,
        "RequesterManaged": bool,
        "NetworkInterfaceIds": List[str],
        "DnsEntries": List["DnsEntryTypeDef"],
        "CreationTimestamp": datetime,
        "Tags": List["TagTypeDef"],
        "OwnerId": str,
        "LastError": "LastErrorTypeDef",
    },
    total=False,
)

VpcIpv6CidrBlockAssociationTypeDef = TypedDict(
    "VpcIpv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "Ipv6CidrBlock": str,
        "Ipv6CidrBlockState": "VpcCidrBlockStateTypeDef",
        "NetworkBorderGroup": str,
        "Ipv6Pool": str,
    },
    total=False,
)

VpcPeeringConnectionOptionsDescriptionTypeDef = TypedDict(
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
    total=False,
)

VpcPeeringConnectionStateReasonTypeDef = TypedDict(
    "VpcPeeringConnectionStateReasonTypeDef",
    {
        "Code": Literal[
            "initiating-request",
            "pending-acceptance",
            "active",
            "deleted",
            "rejected",
            "failed",
            "expired",
            "provisioning",
            "deleting",
        ],
        "Message": str,
    },
    total=False,
)

VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "AccepterVpcInfo": "VpcPeeringConnectionVpcInfoTypeDef",
        "ExpirationTime": datetime,
        "RequesterVpcInfo": "VpcPeeringConnectionVpcInfoTypeDef",
        "Status": "VpcPeeringConnectionStateReasonTypeDef",
        "Tags": List["TagTypeDef"],
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

VpcPeeringConnectionVpcInfoTypeDef = TypedDict(
    "VpcPeeringConnectionVpcInfoTypeDef",
    {
        "CidrBlock": str,
        "Ipv6CidrBlockSet": List["Ipv6CidrBlockTypeDef"],
        "CidrBlockSet": List["CidrBlockTypeDef"],
        "OwnerId": str,
        "PeeringOptions": "VpcPeeringConnectionOptionsDescriptionTypeDef",
        "VpcId": str,
        "Region": str,
    },
    total=False,
)

VpcTypeDef = TypedDict(
    "VpcTypeDef",
    {
        "CidrBlock": str,
        "DhcpOptionsId": str,
        "State": Literal["pending", "available"],
        "VpcId": str,
        "OwnerId": str,
        "InstanceTenancy": Literal["default", "dedicated", "host"],
        "Ipv6CidrBlockAssociationSet": List["VpcIpv6CidrBlockAssociationTypeDef"],
        "CidrBlockAssociationSet": List["VpcCidrBlockAssociationTypeDef"],
        "IsDefault": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

VpnConnectionOptionsTypeDef = TypedDict(
    "VpnConnectionOptionsTypeDef",
    {
        "EnableAcceleration": bool,
        "StaticRoutesOnly": bool,
        "TunnelInsideIpVersion": Literal["ipv4", "ipv6"],
        "TunnelOptions": List["TunnelOptionTypeDef"],
    },
    total=False,
)

VpnConnectionTypeDef = TypedDict(
    "VpnConnectionTypeDef",
    {
        "CustomerGatewayConfiguration": str,
        "CustomerGatewayId": str,
        "Category": str,
        "State": Literal["pending", "available", "deleting", "deleted"],
        "Type": Literal["ipsec.1"],
        "VpnConnectionId": str,
        "VpnGatewayId": str,
        "TransitGatewayId": str,
        "Options": "VpnConnectionOptionsTypeDef",
        "Routes": List["VpnStaticRouteTypeDef"],
        "Tags": List["TagTypeDef"],
        "VgwTelemetry": List["VgwTelemetryTypeDef"],
    },
    total=False,
)

VpnGatewayTypeDef = TypedDict(
    "VpnGatewayTypeDef",
    {
        "AvailabilityZone": str,
        "State": Literal["pending", "available", "deleting", "deleted"],
        "Type": Literal["ipsec.1"],
        "VpcAttachments": List["VpcAttachmentTypeDef"],
        "VpnGatewayId": str,
        "AmazonSideAsn": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

VpnStaticRouteTypeDef = TypedDict(
    "VpnStaticRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "Source": Literal["Static"],
        "State": Literal["pending", "available", "deleting", "deleted"],
    },
    total=False,
)

VpnTunnelOptionsSpecificationTypeDef = TypedDict(
    "VpnTunnelOptionsSpecificationTypeDef",
    {
        "TunnelInsideCidr": str,
        "TunnelInsideIpv6Cidr": str,
        "PreSharedKey": str,
        "Phase1LifetimeSeconds": int,
        "Phase2LifetimeSeconds": int,
        "RekeyMarginTimeSeconds": int,
        "RekeyFuzzPercentage": int,
        "ReplayWindowSize": int,
        "DPDTimeoutSeconds": int,
        "Phase1EncryptionAlgorithms": List["Phase1EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase2EncryptionAlgorithms": List["Phase2EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase1IntegrityAlgorithms": List["Phase1IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase2IntegrityAlgorithms": List["Phase2IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase1DHGroupNumbers": List["Phase1DHGroupNumbersRequestListValueTypeDef"],
        "Phase2DHGroupNumbers": List["Phase2DHGroupNumbersRequestListValueTypeDef"],
        "IKEVersions": List["IKEVersionsRequestListValueTypeDef"],
    },
    total=False,
)

AcceptReservedInstancesExchangeQuoteResultTypeDef = TypedDict(
    "AcceptReservedInstancesExchangeQuoteResultTypeDef", {"ExchangeId": str}, total=False
)

AcceptTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "AcceptTransitGatewayPeeringAttachmentResultTypeDef",
    {"TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef"},
    total=False,
)

AcceptTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "AcceptTransitGatewayVpcAttachmentResultTypeDef",
    {"TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef"},
    total=False,
)

AcceptVpcEndpointConnectionsResultTypeDef = TypedDict(
    "AcceptVpcEndpointConnectionsResultTypeDef",
    {"Unsuccessful": List["UnsuccessfulItemTypeDef"]},
    total=False,
)

AcceptVpcPeeringConnectionResultTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionResultTypeDef",
    {"VpcPeeringConnection": "VpcPeeringConnectionTypeDef"},
    total=False,
)

_RequiredAddPrefixListEntryTypeDef = TypedDict("_RequiredAddPrefixListEntryTypeDef", {"Cidr": str})
_OptionalAddPrefixListEntryTypeDef = TypedDict(
    "_OptionalAddPrefixListEntryTypeDef", {"Description": str}, total=False
)


class AddPrefixListEntryTypeDef(
    _RequiredAddPrefixListEntryTypeDef, _OptionalAddPrefixListEntryTypeDef
):
    pass


AdvertiseByoipCidrResultTypeDef = TypedDict(
    "AdvertiseByoipCidrResultTypeDef", {"ByoipCidr": "ByoipCidrTypeDef"}, total=False
)

AllocateAddressResultTypeDef = TypedDict(
    "AllocateAddressResultTypeDef",
    {
        "PublicIp": str,
        "AllocationId": str,
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "Domain": Literal["vpc", "standard"],
        "CustomerOwnedIp": str,
        "CustomerOwnedIpv4Pool": str,
        "CarrierIp": str,
    },
    total=False,
)

AllocateHostsResultTypeDef = TypedDict(
    "AllocateHostsResultTypeDef", {"HostIds": List[str]}, total=False
)

ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef = TypedDict(
    "ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef",
    {"SecurityGroupIds": List[str]},
    total=False,
)

AssignIpv6AddressesResultTypeDef = TypedDict(
    "AssignIpv6AddressesResultTypeDef",
    {"AssignedIpv6Addresses": List[str], "NetworkInterfaceId": str},
    total=False,
)

AssignPrivateIpAddressesResultTypeDef = TypedDict(
    "AssignPrivateIpAddressesResultTypeDef",
    {
        "NetworkInterfaceId": str,
        "AssignedPrivateIpAddresses": List["AssignedPrivateIpAddressTypeDef"],
    },
    total=False,
)

AssociateAddressResultTypeDef = TypedDict(
    "AssociateAddressResultTypeDef", {"AssociationId": str}, total=False
)

AssociateClientVpnTargetNetworkResultTypeDef = TypedDict(
    "AssociateClientVpnTargetNetworkResultTypeDef",
    {"AssociationId": str, "Status": "AssociationStatusTypeDef"},
    total=False,
)

AssociateIamInstanceProfileResultTypeDef = TypedDict(
    "AssociateIamInstanceProfileResultTypeDef",
    {"IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef"},
    total=False,
)

AssociateRouteTableResultTypeDef = TypedDict(
    "AssociateRouteTableResultTypeDef",
    {"AssociationId": str, "AssociationState": "RouteTableAssociationStateTypeDef"},
    total=False,
)

AssociateSubnetCidrBlockResultTypeDef = TypedDict(
    "AssociateSubnetCidrBlockResultTypeDef",
    {"Ipv6CidrBlockAssociation": "SubnetIpv6CidrBlockAssociationTypeDef", "SubnetId": str},
    total=False,
)

AssociateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "AssociateTransitGatewayMulticastDomainResultTypeDef",
    {"Associations": "TransitGatewayMulticastDomainAssociationsTypeDef"},
    total=False,
)

AssociateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "AssociateTransitGatewayRouteTableResultTypeDef",
    {"Association": "TransitGatewayAssociationTypeDef"},
    total=False,
)

AssociateVpcCidrBlockResultTypeDef = TypedDict(
    "AssociateVpcCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": "VpcIpv6CidrBlockAssociationTypeDef",
        "CidrBlockAssociation": "VpcCidrBlockAssociationTypeDef",
        "VpcId": str,
    },
    total=False,
)

AttachClassicLinkVpcResultTypeDef = TypedDict(
    "AttachClassicLinkVpcResultTypeDef", {"Return": bool}, total=False
)

AttachNetworkInterfaceResultTypeDef = TypedDict(
    "AttachNetworkInterfaceResultTypeDef", {"AttachmentId": str}, total=False
)

AttachVpnGatewayResultTypeDef = TypedDict(
    "AttachVpnGatewayResultTypeDef", {"VpcAttachment": "VpcAttachmentTypeDef"}, total=False
)

AuthorizeClientVpnIngressResultTypeDef = TypedDict(
    "AuthorizeClientVpnIngressResultTypeDef",
    {"Status": "ClientVpnAuthorizationRuleStatusTypeDef"},
    total=False,
)

BlobAttributeValueTypeDef = TypedDict("BlobAttributeValueTypeDef", {"Value": bytes}, total=False)

BundleInstanceResultTypeDef = TypedDict(
    "BundleInstanceResultTypeDef", {"BundleTask": "BundleTaskTypeDef"}, total=False
)

CancelBundleTaskResultTypeDef = TypedDict(
    "CancelBundleTaskResultTypeDef", {"BundleTask": "BundleTaskTypeDef"}, total=False
)

CancelCapacityReservationResultTypeDef = TypedDict(
    "CancelCapacityReservationResultTypeDef", {"Return": bool}, total=False
)

CancelImportTaskResultTypeDef = TypedDict(
    "CancelImportTaskResultTypeDef",
    {"ImportTaskId": str, "PreviousState": str, "State": str},
    total=False,
)

CancelReservedInstancesListingResultTypeDef = TypedDict(
    "CancelReservedInstancesListingResultTypeDef",
    {"ReservedInstancesListings": List["ReservedInstancesListingTypeDef"]},
    total=False,
)

CancelSpotFleetRequestsResponseTypeDef = TypedDict(
    "CancelSpotFleetRequestsResponseTypeDef",
    {
        "SuccessfulFleetRequests": List["CancelSpotFleetRequestsSuccessItemTypeDef"],
        "UnsuccessfulFleetRequests": List["CancelSpotFleetRequestsErrorItemTypeDef"],
    },
    total=False,
)

CancelSpotInstanceRequestsResultTypeDef = TypedDict(
    "CancelSpotInstanceRequestsResultTypeDef",
    {"CancelledSpotInstanceRequests": List["CancelledSpotInstanceRequestTypeDef"]},
    total=False,
)

CapacityReservationSpecificationTypeDef = TypedDict(
    "CapacityReservationSpecificationTypeDef",
    {
        "CapacityReservationPreference": Literal["open", "none"],
        "CapacityReservationTarget": "CapacityReservationTargetTypeDef",
    },
    total=False,
)

CidrAuthorizationContextTypeDef = TypedDict(
    "CidrAuthorizationContextTypeDef", {"Message": str, "Signature": str}
)

ClientDataTypeDef = TypedDict(
    "ClientDataTypeDef",
    {"Comment": str, "UploadEnd": datetime, "UploadSize": float, "UploadStart": datetime},
    total=False,
)

ClientVpnAuthenticationRequestTypeDef = TypedDict(
    "ClientVpnAuthenticationRequestTypeDef",
    {
        "Type": Literal[
            "certificate-authentication",
            "directory-service-authentication",
            "federated-authentication",
        ],
        "ActiveDirectory": "DirectoryServiceAuthenticationRequestTypeDef",
        "MutualAuthentication": "CertificateAuthenticationRequestTypeDef",
        "FederatedAuthentication": "FederatedAuthenticationRequestTypeDef",
    },
    total=False,
)

ConfirmProductInstanceResultTypeDef = TypedDict(
    "ConfirmProductInstanceResultTypeDef", {"OwnerId": str, "Return": bool}, total=False
)

ConnectionLogOptionsTypeDef = TypedDict(
    "ConnectionLogOptionsTypeDef",
    {"Enabled": bool, "CloudwatchLogGroup": str, "CloudwatchLogStream": str},
    total=False,
)

CopyFpgaImageResultTypeDef = TypedDict(
    "CopyFpgaImageResultTypeDef", {"FpgaImageId": str}, total=False
)

CopyImageResultTypeDef = TypedDict("CopyImageResultTypeDef", {"ImageId": str}, total=False)

CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef", {"SnapshotId": str, "Tags": List["TagTypeDef"]}, total=False
)

CpuOptionsRequestTypeDef = TypedDict(
    "CpuOptionsRequestTypeDef", {"CoreCount": int, "ThreadsPerCore": int}, total=False
)

CreateCapacityReservationResultTypeDef = TypedDict(
    "CreateCapacityReservationResultTypeDef",
    {"CapacityReservation": "CapacityReservationTypeDef"},
    total=False,
)

CreateCarrierGatewayResultTypeDef = TypedDict(
    "CreateCarrierGatewayResultTypeDef", {"CarrierGateway": "CarrierGatewayTypeDef"}, total=False
)

CreateClientVpnEndpointResultTypeDef = TypedDict(
    "CreateClientVpnEndpointResultTypeDef",
    {"ClientVpnEndpointId": str, "Status": "ClientVpnEndpointStatusTypeDef", "DnsName": str},
    total=False,
)

CreateClientVpnRouteResultTypeDef = TypedDict(
    "CreateClientVpnRouteResultTypeDef", {"Status": "ClientVpnRouteStatusTypeDef"}, total=False
)

CreateCustomerGatewayResultTypeDef = TypedDict(
    "CreateCustomerGatewayResultTypeDef", {"CustomerGateway": "CustomerGatewayTypeDef"}, total=False
)

CreateDefaultSubnetResultTypeDef = TypedDict(
    "CreateDefaultSubnetResultTypeDef", {"Subnet": "SubnetTypeDef"}, total=False
)

CreateDefaultVpcResultTypeDef = TypedDict(
    "CreateDefaultVpcResultTypeDef", {"Vpc": "VpcTypeDef"}, total=False
)

CreateDhcpOptionsResultTypeDef = TypedDict(
    "CreateDhcpOptionsResultTypeDef", {"DhcpOptions": "DhcpOptionsTypeDef"}, total=False
)

CreateEgressOnlyInternetGatewayResultTypeDef = TypedDict(
    "CreateEgressOnlyInternetGatewayResultTypeDef",
    {"ClientToken": str, "EgressOnlyInternetGateway": "EgressOnlyInternetGatewayTypeDef"},
    total=False,
)

CreateFleetResultTypeDef = TypedDict(
    "CreateFleetResultTypeDef",
    {
        "FleetId": str,
        "Errors": List["CreateFleetErrorTypeDef"],
        "Instances": List["CreateFleetInstanceTypeDef"],
    },
    total=False,
)

CreateFlowLogsResultTypeDef = TypedDict(
    "CreateFlowLogsResultTypeDef",
    {"ClientToken": str, "FlowLogIds": List[str], "Unsuccessful": List["UnsuccessfulItemTypeDef"]},
    total=False,
)

CreateFpgaImageResultTypeDef = TypedDict(
    "CreateFpgaImageResultTypeDef", {"FpgaImageId": str, "FpgaImageGlobalId": str}, total=False
)

CreateImageResultTypeDef = TypedDict("CreateImageResultTypeDef", {"ImageId": str}, total=False)

CreateInstanceExportTaskResultTypeDef = TypedDict(
    "CreateInstanceExportTaskResultTypeDef", {"ExportTask": "ExportTaskTypeDef"}, total=False
)

CreateInternetGatewayResultTypeDef = TypedDict(
    "CreateInternetGatewayResultTypeDef", {"InternetGateway": "InternetGatewayTypeDef"}, total=False
)

CreateLaunchTemplateResultTypeDef = TypedDict(
    "CreateLaunchTemplateResultTypeDef",
    {"LaunchTemplate": "LaunchTemplateTypeDef", "Warning": "ValidationWarningTypeDef"},
    total=False,
)

CreateLaunchTemplateVersionResultTypeDef = TypedDict(
    "CreateLaunchTemplateVersionResultTypeDef",
    {
        "LaunchTemplateVersion": "LaunchTemplateVersionTypeDef",
        "Warning": "ValidationWarningTypeDef",
    },
    total=False,
)

CreateLocalGatewayRouteResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteResultTypeDef", {"Route": "LocalGatewayRouteTypeDef"}, total=False
)

CreateLocalGatewayRouteTableVpcAssociationResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableVpcAssociationResultTypeDef",
    {"LocalGatewayRouteTableVpcAssociation": "LocalGatewayRouteTableVpcAssociationTypeDef"},
    total=False,
)

CreateManagedPrefixListResultTypeDef = TypedDict(
    "CreateManagedPrefixListResultTypeDef", {"PrefixList": "ManagedPrefixListTypeDef"}, total=False
)

CreateNatGatewayResultTypeDef = TypedDict(
    "CreateNatGatewayResultTypeDef",
    {"ClientToken": str, "NatGateway": "NatGatewayTypeDef"},
    total=False,
)

CreateNetworkAclResultTypeDef = TypedDict(
    "CreateNetworkAclResultTypeDef", {"NetworkAcl": "NetworkAclTypeDef"}, total=False
)

CreateNetworkInterfacePermissionResultTypeDef = TypedDict(
    "CreateNetworkInterfacePermissionResultTypeDef",
    {"InterfacePermission": "NetworkInterfacePermissionTypeDef"},
    total=False,
)

CreateNetworkInterfaceResultTypeDef = TypedDict(
    "CreateNetworkInterfaceResultTypeDef",
    {"NetworkInterface": "NetworkInterfaceTypeDef"},
    total=False,
)

CreatePlacementGroupResultTypeDef = TypedDict(
    "CreatePlacementGroupResultTypeDef", {"PlacementGroup": "PlacementGroupTypeDef"}, total=False
)

CreateReservedInstancesListingResultTypeDef = TypedDict(
    "CreateReservedInstancesListingResultTypeDef",
    {"ReservedInstancesListings": List["ReservedInstancesListingTypeDef"]},
    total=False,
)

CreateRouteResultTypeDef = TypedDict("CreateRouteResultTypeDef", {"Return": bool}, total=False)

CreateRouteTableResultTypeDef = TypedDict(
    "CreateRouteTableResultTypeDef", {"RouteTable": "RouteTableTypeDef"}, total=False
)

CreateSecurityGroupResultTypeDef = TypedDict(
    "CreateSecurityGroupResultTypeDef", {"GroupId": str, "Tags": List["TagTypeDef"]}, total=False
)

CreateSnapshotsResultTypeDef = TypedDict(
    "CreateSnapshotsResultTypeDef", {"Snapshots": List["SnapshotInfoTypeDef"]}, total=False
)

CreateSpotDatafeedSubscriptionResultTypeDef = TypedDict(
    "CreateSpotDatafeedSubscriptionResultTypeDef",
    {"SpotDatafeedSubscription": "SpotDatafeedSubscriptionTypeDef"},
    total=False,
)

CreateSubnetResultTypeDef = TypedDict(
    "CreateSubnetResultTypeDef", {"Subnet": "SubnetTypeDef"}, total=False
)

CreateTrafficMirrorFilterResultTypeDef = TypedDict(
    "CreateTrafficMirrorFilterResultTypeDef",
    {"TrafficMirrorFilter": "TrafficMirrorFilterTypeDef", "ClientToken": str},
    total=False,
)

CreateTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRuleResultTypeDef",
    {"TrafficMirrorFilterRule": "TrafficMirrorFilterRuleTypeDef", "ClientToken": str},
    total=False,
)

CreateTrafficMirrorSessionResultTypeDef = TypedDict(
    "CreateTrafficMirrorSessionResultTypeDef",
    {"TrafficMirrorSession": "TrafficMirrorSessionTypeDef", "ClientToken": str},
    total=False,
)

CreateTrafficMirrorTargetResultTypeDef = TypedDict(
    "CreateTrafficMirrorTargetResultTypeDef",
    {"TrafficMirrorTarget": "TrafficMirrorTargetTypeDef", "ClientToken": str},
    total=False,
)

CreateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainResultTypeDef",
    {"TransitGatewayMulticastDomain": "TransitGatewayMulticastDomainTypeDef"},
    total=False,
)

CreateTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "CreateTransitGatewayPeeringAttachmentResultTypeDef",
    {"TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef"},
    total=False,
)

CreateTransitGatewayResultTypeDef = TypedDict(
    "CreateTransitGatewayResultTypeDef", {"TransitGateway": "TransitGatewayTypeDef"}, total=False
)

CreateTransitGatewayRouteResultTypeDef = TypedDict(
    "CreateTransitGatewayRouteResultTypeDef", {"Route": "TransitGatewayRouteTypeDef"}, total=False
)

CreateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableResultTypeDef",
    {"TransitGatewayRouteTable": "TransitGatewayRouteTableTypeDef"},
    total=False,
)

CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    {"DnsSupport": Literal["enable", "disable"], "Ipv6Support": Literal["enable", "disable"]},
    total=False,
)

CreateTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentResultTypeDef",
    {"TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef"},
    total=False,
)

CreateVolumePermissionModificationsTypeDef = TypedDict(
    "CreateVolumePermissionModificationsTypeDef",
    {"Add": List["CreateVolumePermissionTypeDef"], "Remove": List["CreateVolumePermissionTypeDef"]},
    total=False,
)

CreateVpcEndpointConnectionNotificationResultTypeDef = TypedDict(
    "CreateVpcEndpointConnectionNotificationResultTypeDef",
    {"ConnectionNotification": "ConnectionNotificationTypeDef", "ClientToken": str},
    total=False,
)

CreateVpcEndpointResultTypeDef = TypedDict(
    "CreateVpcEndpointResultTypeDef",
    {"VpcEndpoint": "VpcEndpointTypeDef", "ClientToken": str},
    total=False,
)

CreateVpcEndpointServiceConfigurationResultTypeDef = TypedDict(
    "CreateVpcEndpointServiceConfigurationResultTypeDef",
    {"ServiceConfiguration": "ServiceConfigurationTypeDef", "ClientToken": str},
    total=False,
)

CreateVpcPeeringConnectionResultTypeDef = TypedDict(
    "CreateVpcPeeringConnectionResultTypeDef",
    {"VpcPeeringConnection": "VpcPeeringConnectionTypeDef"},
    total=False,
)

CreateVpcResultTypeDef = TypedDict("CreateVpcResultTypeDef", {"Vpc": "VpcTypeDef"}, total=False)

CreateVpnConnectionResultTypeDef = TypedDict(
    "CreateVpnConnectionResultTypeDef", {"VpnConnection": "VpnConnectionTypeDef"}, total=False
)

CreateVpnGatewayResultTypeDef = TypedDict(
    "CreateVpnGatewayResultTypeDef", {"VpnGateway": "VpnGatewayTypeDef"}, total=False
)

DeleteCarrierGatewayResultTypeDef = TypedDict(
    "DeleteCarrierGatewayResultTypeDef", {"CarrierGateway": "CarrierGatewayTypeDef"}, total=False
)

DeleteClientVpnEndpointResultTypeDef = TypedDict(
    "DeleteClientVpnEndpointResultTypeDef",
    {"Status": "ClientVpnEndpointStatusTypeDef"},
    total=False,
)

DeleteClientVpnRouteResultTypeDef = TypedDict(
    "DeleteClientVpnRouteResultTypeDef", {"Status": "ClientVpnRouteStatusTypeDef"}, total=False
)

DeleteEgressOnlyInternetGatewayResultTypeDef = TypedDict(
    "DeleteEgressOnlyInternetGatewayResultTypeDef", {"ReturnCode": bool}, total=False
)

DeleteFleetsResultTypeDef = TypedDict(
    "DeleteFleetsResultTypeDef",
    {
        "SuccessfulFleetDeletions": List["DeleteFleetSuccessItemTypeDef"],
        "UnsuccessfulFleetDeletions": List["DeleteFleetErrorItemTypeDef"],
    },
    total=False,
)

DeleteFlowLogsResultTypeDef = TypedDict(
    "DeleteFlowLogsResultTypeDef", {"Unsuccessful": List["UnsuccessfulItemTypeDef"]}, total=False
)

DeleteFpgaImageResultTypeDef = TypedDict(
    "DeleteFpgaImageResultTypeDef", {"Return": bool}, total=False
)

DeleteLaunchTemplateResultTypeDef = TypedDict(
    "DeleteLaunchTemplateResultTypeDef", {"LaunchTemplate": "LaunchTemplateTypeDef"}, total=False
)

DeleteLaunchTemplateVersionsResultTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResultTypeDef",
    {
        "SuccessfullyDeletedLaunchTemplateVersions": List[
            "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef"
        ],
        "UnsuccessfullyDeletedLaunchTemplateVersions": List[
            "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef"
        ],
    },
    total=False,
)

DeleteLocalGatewayRouteResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteResultTypeDef", {"Route": "LocalGatewayRouteTypeDef"}, total=False
)

DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef",
    {"LocalGatewayRouteTableVpcAssociation": "LocalGatewayRouteTableVpcAssociationTypeDef"},
    total=False,
)

DeleteManagedPrefixListResultTypeDef = TypedDict(
    "DeleteManagedPrefixListResultTypeDef", {"PrefixList": "ManagedPrefixListTypeDef"}, total=False
)

DeleteNatGatewayResultTypeDef = TypedDict(
    "DeleteNatGatewayResultTypeDef", {"NatGatewayId": str}, total=False
)

DeleteNetworkInterfacePermissionResultTypeDef = TypedDict(
    "DeleteNetworkInterfacePermissionResultTypeDef", {"Return": bool}, total=False
)

DeleteQueuedReservedInstancesResultTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesResultTypeDef",
    {
        "SuccessfulQueuedPurchaseDeletions": List["SuccessfulQueuedPurchaseDeletionTypeDef"],
        "FailedQueuedPurchaseDeletions": List["FailedQueuedPurchaseDeletionTypeDef"],
    },
    total=False,
)

DeleteTrafficMirrorFilterResultTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterResultTypeDef", {"TrafficMirrorFilterId": str}, total=False
)

DeleteTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterRuleResultTypeDef", {"TrafficMirrorFilterRuleId": str}, total=False
)

DeleteTrafficMirrorSessionResultTypeDef = TypedDict(
    "DeleteTrafficMirrorSessionResultTypeDef", {"TrafficMirrorSessionId": str}, total=False
)

DeleteTrafficMirrorTargetResultTypeDef = TypedDict(
    "DeleteTrafficMirrorTargetResultTypeDef", {"TrafficMirrorTargetId": str}, total=False
)

DeleteTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "DeleteTransitGatewayMulticastDomainResultTypeDef",
    {"TransitGatewayMulticastDomain": "TransitGatewayMulticastDomainTypeDef"},
    total=False,
)

DeleteTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "DeleteTransitGatewayPeeringAttachmentResultTypeDef",
    {"TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef"},
    total=False,
)

DeleteTransitGatewayResultTypeDef = TypedDict(
    "DeleteTransitGatewayResultTypeDef", {"TransitGateway": "TransitGatewayTypeDef"}, total=False
)

DeleteTransitGatewayRouteResultTypeDef = TypedDict(
    "DeleteTransitGatewayRouteResultTypeDef", {"Route": "TransitGatewayRouteTypeDef"}, total=False
)

DeleteTransitGatewayRouteTableResultTypeDef = TypedDict(
    "DeleteTransitGatewayRouteTableResultTypeDef",
    {"TransitGatewayRouteTable": "TransitGatewayRouteTableTypeDef"},
    total=False,
)

DeleteTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "DeleteTransitGatewayVpcAttachmentResultTypeDef",
    {"TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef"},
    total=False,
)

DeleteVpcEndpointConnectionNotificationsResultTypeDef = TypedDict(
    "DeleteVpcEndpointConnectionNotificationsResultTypeDef",
    {"Unsuccessful": List["UnsuccessfulItemTypeDef"]},
    total=False,
)

DeleteVpcEndpointServiceConfigurationsResultTypeDef = TypedDict(
    "DeleteVpcEndpointServiceConfigurationsResultTypeDef",
    {"Unsuccessful": List["UnsuccessfulItemTypeDef"]},
    total=False,
)

DeleteVpcEndpointsResultTypeDef = TypedDict(
    "DeleteVpcEndpointsResultTypeDef",
    {"Unsuccessful": List["UnsuccessfulItemTypeDef"]},
    total=False,
)

DeleteVpcPeeringConnectionResultTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionResultTypeDef", {"Return": bool}, total=False
)

DeprovisionByoipCidrResultTypeDef = TypedDict(
    "DeprovisionByoipCidrResultTypeDef", {"ByoipCidr": "ByoipCidrTypeDef"}, total=False
)

DeregisterInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "DeregisterInstanceEventNotificationAttributesResultTypeDef",
    {"InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef"},
    total=False,
)

DeregisterInstanceTagAttributeRequestTypeDef = TypedDict(
    "DeregisterInstanceTagAttributeRequestTypeDef",
    {"IncludeAllTagsOfInstance": bool, "InstanceTagKeys": List[str]},
    total=False,
)

DeregisterTransitGatewayMulticastGroupMembersResultTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupMembersResultTypeDef",
    {"DeregisteredMulticastGroupMembers": "TransitGatewayMulticastDeregisteredGroupMembersTypeDef"},
    total=False,
)

DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    {"DeregisteredMulticastGroupSources": "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef"},
    total=False,
)

DescribeAccountAttributesResultTypeDef = TypedDict(
    "DescribeAccountAttributesResultTypeDef",
    {"AccountAttributes": List["AccountAttributeTypeDef"]},
    total=False,
)

DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef", {"Addresses": List["AddressTypeDef"]}, total=False
)

DescribeAggregateIdFormatResultTypeDef = TypedDict(
    "DescribeAggregateIdFormatResultTypeDef",
    {"UseLongIdsAggregated": bool, "Statuses": List["IdFormatTypeDef"]},
    total=False,
)

DescribeAvailabilityZonesResultTypeDef = TypedDict(
    "DescribeAvailabilityZonesResultTypeDef",
    {"AvailabilityZones": List["AvailabilityZoneTypeDef"]},
    total=False,
)

DescribeBundleTasksResultTypeDef = TypedDict(
    "DescribeBundleTasksResultTypeDef", {"BundleTasks": List["BundleTaskTypeDef"]}, total=False
)

DescribeByoipCidrsResultTypeDef = TypedDict(
    "DescribeByoipCidrsResultTypeDef",
    {"ByoipCidrs": List["ByoipCidrTypeDef"], "NextToken": str},
    total=False,
)

DescribeCapacityReservationsResultTypeDef = TypedDict(
    "DescribeCapacityReservationsResultTypeDef",
    {"NextToken": str, "CapacityReservations": List["CapacityReservationTypeDef"]},
    total=False,
)

DescribeCarrierGatewaysResultTypeDef = TypedDict(
    "DescribeCarrierGatewaysResultTypeDef",
    {"CarrierGateways": List["CarrierGatewayTypeDef"], "NextToken": str},
    total=False,
)

DescribeClassicLinkInstancesResultTypeDef = TypedDict(
    "DescribeClassicLinkInstancesResultTypeDef",
    {"Instances": List["ClassicLinkInstanceTypeDef"], "NextToken": str},
    total=False,
)

DescribeClientVpnAuthorizationRulesResultTypeDef = TypedDict(
    "DescribeClientVpnAuthorizationRulesResultTypeDef",
    {"AuthorizationRules": List["AuthorizationRuleTypeDef"], "NextToken": str},
    total=False,
)

DescribeClientVpnConnectionsResultTypeDef = TypedDict(
    "DescribeClientVpnConnectionsResultTypeDef",
    {"Connections": List["ClientVpnConnectionTypeDef"], "NextToken": str},
    total=False,
)

DescribeClientVpnEndpointsResultTypeDef = TypedDict(
    "DescribeClientVpnEndpointsResultTypeDef",
    {"ClientVpnEndpoints": List["ClientVpnEndpointTypeDef"], "NextToken": str},
    total=False,
)

DescribeClientVpnRoutesResultTypeDef = TypedDict(
    "DescribeClientVpnRoutesResultTypeDef",
    {"Routes": List["ClientVpnRouteTypeDef"], "NextToken": str},
    total=False,
)

DescribeClientVpnTargetNetworksResultTypeDef = TypedDict(
    "DescribeClientVpnTargetNetworksResultTypeDef",
    {"ClientVpnTargetNetworks": List["TargetNetworkTypeDef"], "NextToken": str},
    total=False,
)

DescribeCoipPoolsResultTypeDef = TypedDict(
    "DescribeCoipPoolsResultTypeDef",
    {"CoipPools": List["CoipPoolTypeDef"], "NextToken": str},
    total=False,
)

DescribeConversionTasksResultTypeDef = TypedDict(
    "DescribeConversionTasksResultTypeDef",
    {"ConversionTasks": List["ConversionTaskTypeDef"]},
    total=False,
)

DescribeCustomerGatewaysResultTypeDef = TypedDict(
    "DescribeCustomerGatewaysResultTypeDef",
    {"CustomerGateways": List["CustomerGatewayTypeDef"]},
    total=False,
)

DescribeDhcpOptionsResultTypeDef = TypedDict(
    "DescribeDhcpOptionsResultTypeDef",
    {"DhcpOptions": List["DhcpOptionsTypeDef"], "NextToken": str},
    total=False,
)

DescribeEgressOnlyInternetGatewaysResultTypeDef = TypedDict(
    "DescribeEgressOnlyInternetGatewaysResultTypeDef",
    {"EgressOnlyInternetGateways": List["EgressOnlyInternetGatewayTypeDef"], "NextToken": str},
    total=False,
)

DescribeElasticGpusResultTypeDef = TypedDict(
    "DescribeElasticGpusResultTypeDef",
    {"ElasticGpuSet": List["ElasticGpusTypeDef"], "MaxResults": int, "NextToken": str},
    total=False,
)

DescribeExportImageTasksResultTypeDef = TypedDict(
    "DescribeExportImageTasksResultTypeDef",
    {"ExportImageTasks": List["ExportImageTaskTypeDef"], "NextToken": str},
    total=False,
)

DescribeExportTasksResultTypeDef = TypedDict(
    "DescribeExportTasksResultTypeDef", {"ExportTasks": List["ExportTaskTypeDef"]}, total=False
)

DescribeFastSnapshotRestoresResultTypeDef = TypedDict(
    "DescribeFastSnapshotRestoresResultTypeDef",
    {
        "FastSnapshotRestores": List["DescribeFastSnapshotRestoreSuccessItemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeFleetHistoryResultTypeDef = TypedDict(
    "DescribeFleetHistoryResultTypeDef",
    {
        "HistoryRecords": List["HistoryRecordEntryTypeDef"],
        "LastEvaluatedTime": datetime,
        "NextToken": str,
        "FleetId": str,
        "StartTime": datetime,
    },
    total=False,
)

DescribeFleetInstancesResultTypeDef = TypedDict(
    "DescribeFleetInstancesResultTypeDef",
    {"ActiveInstances": List["ActiveInstanceTypeDef"], "NextToken": str, "FleetId": str},
    total=False,
)

DescribeFleetsResultTypeDef = TypedDict(
    "DescribeFleetsResultTypeDef",
    {"NextToken": str, "Fleets": List["FleetDataTypeDef"]},
    total=False,
)

DescribeFlowLogsResultTypeDef = TypedDict(
    "DescribeFlowLogsResultTypeDef",
    {"FlowLogs": List["FlowLogTypeDef"], "NextToken": str},
    total=False,
)

DescribeFpgaImageAttributeResultTypeDef = TypedDict(
    "DescribeFpgaImageAttributeResultTypeDef",
    {"FpgaImageAttribute": "FpgaImageAttributeTypeDef"},
    total=False,
)

DescribeFpgaImagesResultTypeDef = TypedDict(
    "DescribeFpgaImagesResultTypeDef",
    {"FpgaImages": List["FpgaImageTypeDef"], "NextToken": str},
    total=False,
)

DescribeHostReservationOfferingsResultTypeDef = TypedDict(
    "DescribeHostReservationOfferingsResultTypeDef",
    {"NextToken": str, "OfferingSet": List["HostOfferingTypeDef"]},
    total=False,
)

DescribeHostReservationsResultTypeDef = TypedDict(
    "DescribeHostReservationsResultTypeDef",
    {"HostReservationSet": List["HostReservationTypeDef"], "NextToken": str},
    total=False,
)

DescribeHostsResultTypeDef = TypedDict(
    "DescribeHostsResultTypeDef", {"Hosts": List["HostTypeDef"], "NextToken": str}, total=False
)

DescribeIamInstanceProfileAssociationsResultTypeDef = TypedDict(
    "DescribeIamInstanceProfileAssociationsResultTypeDef",
    {
        "IamInstanceProfileAssociations": List["IamInstanceProfileAssociationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeIdFormatResultTypeDef = TypedDict(
    "DescribeIdFormatResultTypeDef", {"Statuses": List["IdFormatTypeDef"]}, total=False
)

DescribeIdentityIdFormatResultTypeDef = TypedDict(
    "DescribeIdentityIdFormatResultTypeDef", {"Statuses": List["IdFormatTypeDef"]}, total=False
)

DescribeImagesResultTypeDef = TypedDict(
    "DescribeImagesResultTypeDef", {"Images": List["ImageTypeDef"]}, total=False
)

DescribeImportImageTasksResultTypeDef = TypedDict(
    "DescribeImportImageTasksResultTypeDef",
    {"ImportImageTasks": List["ImportImageTaskTypeDef"], "NextToken": str},
    total=False,
)

DescribeImportSnapshotTasksResultTypeDef = TypedDict(
    "DescribeImportSnapshotTasksResultTypeDef",
    {"ImportSnapshotTasks": List["ImportSnapshotTaskTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstanceCreditSpecificationsResultTypeDef = TypedDict(
    "DescribeInstanceCreditSpecificationsResultTypeDef",
    {"InstanceCreditSpecifications": List["InstanceCreditSpecificationTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "DescribeInstanceEventNotificationAttributesResultTypeDef",
    {"InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef"},
    total=False,
)

DescribeInstanceStatusResultTypeDef = TypedDict(
    "DescribeInstanceStatusResultTypeDef",
    {"InstanceStatuses": List["InstanceStatusTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstanceTypeOfferingsResultTypeDef = TypedDict(
    "DescribeInstanceTypeOfferingsResultTypeDef",
    {"InstanceTypeOfferings": List["InstanceTypeOfferingTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstanceTypesResultTypeDef = TypedDict(
    "DescribeInstanceTypesResultTypeDef",
    {"InstanceTypes": List["InstanceTypeInfoTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstancesResultTypeDef = TypedDict(
    "DescribeInstancesResultTypeDef",
    {"Reservations": List["ReservationTypeDef"], "NextToken": str},
    total=False,
)

DescribeInternetGatewaysResultTypeDef = TypedDict(
    "DescribeInternetGatewaysResultTypeDef",
    {"InternetGateways": List["InternetGatewayTypeDef"], "NextToken": str},
    total=False,
)

DescribeIpv6PoolsResultTypeDef = TypedDict(
    "DescribeIpv6PoolsResultTypeDef",
    {"Ipv6Pools": List["Ipv6PoolTypeDef"], "NextToken": str},
    total=False,
)

DescribeKeyPairsResultTypeDef = TypedDict(
    "DescribeKeyPairsResultTypeDef", {"KeyPairs": List["KeyPairInfoTypeDef"]}, total=False
)

DescribeLaunchTemplateVersionsResultTypeDef = TypedDict(
    "DescribeLaunchTemplateVersionsResultTypeDef",
    {"LaunchTemplateVersions": List["LaunchTemplateVersionTypeDef"], "NextToken": str},
    total=False,
)

DescribeLaunchTemplatesResultTypeDef = TypedDict(
    "DescribeLaunchTemplatesResultTypeDef",
    {"LaunchTemplates": List["LaunchTemplateTypeDef"], "NextToken": str},
    total=False,
)

DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociations": List[
            "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociations": List[
            "LocalGatewayRouteTableVpcAssociationTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeLocalGatewayRouteTablesResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTablesResultTypeDef",
    {"LocalGatewayRouteTables": List["LocalGatewayRouteTableTypeDef"], "NextToken": str},
    total=False,
)

DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroups": List["LocalGatewayVirtualInterfaceGroupTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeLocalGatewayVirtualInterfacesResultTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfacesResultTypeDef",
    {
        "LocalGatewayVirtualInterfaces": List["LocalGatewayVirtualInterfaceTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeLocalGatewaysResultTypeDef = TypedDict(
    "DescribeLocalGatewaysResultTypeDef",
    {"LocalGateways": List["LocalGatewayTypeDef"], "NextToken": str},
    total=False,
)

DescribeManagedPrefixListsResultTypeDef = TypedDict(
    "DescribeManagedPrefixListsResultTypeDef",
    {"NextToken": str, "PrefixLists": List["ManagedPrefixListTypeDef"]},
    total=False,
)

DescribeMovingAddressesResultTypeDef = TypedDict(
    "DescribeMovingAddressesResultTypeDef",
    {"MovingAddressStatuses": List["MovingAddressStatusTypeDef"], "NextToken": str},
    total=False,
)

DescribeNatGatewaysResultTypeDef = TypedDict(
    "DescribeNatGatewaysResultTypeDef",
    {"NatGateways": List["NatGatewayTypeDef"], "NextToken": str},
    total=False,
)

DescribeNetworkAclsResultTypeDef = TypedDict(
    "DescribeNetworkAclsResultTypeDef",
    {"NetworkAcls": List["NetworkAclTypeDef"], "NextToken": str},
    total=False,
)

DescribeNetworkInterfaceAttributeResultTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeResultTypeDef",
    {
        "Attachment": "NetworkInterfaceAttachmentTypeDef",
        "Description": "AttributeValueTypeDef",
        "Groups": List["GroupIdentifierTypeDef"],
        "NetworkInterfaceId": str,
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
    },
    total=False,
)

DescribeNetworkInterfacePermissionsResultTypeDef = TypedDict(
    "DescribeNetworkInterfacePermissionsResultTypeDef",
    {"NetworkInterfacePermissions": List["NetworkInterfacePermissionTypeDef"], "NextToken": str},
    total=False,
)

DescribeNetworkInterfacesResultTypeDef = TypedDict(
    "DescribeNetworkInterfacesResultTypeDef",
    {"NetworkInterfaces": List["NetworkInterfaceTypeDef"], "NextToken": str},
    total=False,
)

DescribePlacementGroupsResultTypeDef = TypedDict(
    "DescribePlacementGroupsResultTypeDef",
    {"PlacementGroups": List["PlacementGroupTypeDef"]},
    total=False,
)

DescribePrefixListsResultTypeDef = TypedDict(
    "DescribePrefixListsResultTypeDef",
    {"NextToken": str, "PrefixLists": List["PrefixListTypeDef"]},
    total=False,
)

DescribePrincipalIdFormatResultTypeDef = TypedDict(
    "DescribePrincipalIdFormatResultTypeDef",
    {"Principals": List["PrincipalIdFormatTypeDef"], "NextToken": str},
    total=False,
)

DescribePublicIpv4PoolsResultTypeDef = TypedDict(
    "DescribePublicIpv4PoolsResultTypeDef",
    {"PublicIpv4Pools": List["PublicIpv4PoolTypeDef"], "NextToken": str},
    total=False,
)

DescribeRegionsResultTypeDef = TypedDict(
    "DescribeRegionsResultTypeDef", {"Regions": List["RegionTypeDef"]}, total=False
)

DescribeReservedInstancesListingsResultTypeDef = TypedDict(
    "DescribeReservedInstancesListingsResultTypeDef",
    {"ReservedInstancesListings": List["ReservedInstancesListingTypeDef"]},
    total=False,
)

DescribeReservedInstancesModificationsResultTypeDef = TypedDict(
    "DescribeReservedInstancesModificationsResultTypeDef",
    {
        "NextToken": str,
        "ReservedInstancesModifications": List["ReservedInstancesModificationTypeDef"],
    },
    total=False,
)

DescribeReservedInstancesOfferingsResultTypeDef = TypedDict(
    "DescribeReservedInstancesOfferingsResultTypeDef",
    {"ReservedInstancesOfferings": List["ReservedInstancesOfferingTypeDef"], "NextToken": str},
    total=False,
)

DescribeReservedInstancesResultTypeDef = TypedDict(
    "DescribeReservedInstancesResultTypeDef",
    {"ReservedInstances": List["ReservedInstancesTypeDef"]},
    total=False,
)

DescribeRouteTablesResultTypeDef = TypedDict(
    "DescribeRouteTablesResultTypeDef",
    {"RouteTables": List["RouteTableTypeDef"], "NextToken": str},
    total=False,
)

DescribeScheduledInstanceAvailabilityResultTypeDef = TypedDict(
    "DescribeScheduledInstanceAvailabilityResultTypeDef",
    {
        "NextToken": str,
        "ScheduledInstanceAvailabilitySet": List["ScheduledInstanceAvailabilityTypeDef"],
    },
    total=False,
)

DescribeScheduledInstancesResultTypeDef = TypedDict(
    "DescribeScheduledInstancesResultTypeDef",
    {"NextToken": str, "ScheduledInstanceSet": List["ScheduledInstanceTypeDef"]},
    total=False,
)

DescribeSecurityGroupReferencesResultTypeDef = TypedDict(
    "DescribeSecurityGroupReferencesResultTypeDef",
    {"SecurityGroupReferenceSet": List["SecurityGroupReferenceTypeDef"]},
    total=False,
)

DescribeSecurityGroupsResultTypeDef = TypedDict(
    "DescribeSecurityGroupsResultTypeDef",
    {"SecurityGroups": List["SecurityGroupTypeDef"], "NextToken": str},
    total=False,
)

DescribeSnapshotAttributeResultTypeDef = TypedDict(
    "DescribeSnapshotAttributeResultTypeDef",
    {
        "CreateVolumePermissions": List["CreateVolumePermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
        "SnapshotId": str,
    },
    total=False,
)

DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {"Snapshots": List["SnapshotTypeDef"], "NextToken": str},
    total=False,
)

DescribeSpotDatafeedSubscriptionResultTypeDef = TypedDict(
    "DescribeSpotDatafeedSubscriptionResultTypeDef",
    {"SpotDatafeedSubscription": "SpotDatafeedSubscriptionTypeDef"},
    total=False,
)

DescribeSpotFleetInstancesResponseTypeDef = TypedDict(
    "DescribeSpotFleetInstancesResponseTypeDef",
    {"ActiveInstances": List["ActiveInstanceTypeDef"], "NextToken": str, "SpotFleetRequestId": str},
    total=False,
)

DescribeSpotFleetRequestHistoryResponseTypeDef = TypedDict(
    "DescribeSpotFleetRequestHistoryResponseTypeDef",
    {
        "HistoryRecords": List["HistoryRecordTypeDef"],
        "LastEvaluatedTime": datetime,
        "NextToken": str,
        "SpotFleetRequestId": str,
        "StartTime": datetime,
    },
    total=False,
)

DescribeSpotFleetRequestsResponseTypeDef = TypedDict(
    "DescribeSpotFleetRequestsResponseTypeDef",
    {"NextToken": str, "SpotFleetRequestConfigs": List["SpotFleetRequestConfigTypeDef"]},
    total=False,
)

DescribeSpotInstanceRequestsResultTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsResultTypeDef",
    {"SpotInstanceRequests": List["SpotInstanceRequestTypeDef"], "NextToken": str},
    total=False,
)

DescribeSpotPriceHistoryResultTypeDef = TypedDict(
    "DescribeSpotPriceHistoryResultTypeDef",
    {"NextToken": str, "SpotPriceHistory": List["SpotPriceTypeDef"]},
    total=False,
)

DescribeStaleSecurityGroupsResultTypeDef = TypedDict(
    "DescribeStaleSecurityGroupsResultTypeDef",
    {"NextToken": str, "StaleSecurityGroupSet": List["StaleSecurityGroupTypeDef"]},
    total=False,
)

DescribeSubnetsResultTypeDef = TypedDict(
    "DescribeSubnetsResultTypeDef",
    {"Subnets": List["SubnetTypeDef"], "NextToken": str},
    total=False,
)

DescribeTagsResultTypeDef = TypedDict(
    "DescribeTagsResultTypeDef",
    {"NextToken": str, "Tags": List["TagDescriptionTypeDef"]},
    total=False,
)

DescribeTrafficMirrorFiltersResultTypeDef = TypedDict(
    "DescribeTrafficMirrorFiltersResultTypeDef",
    {"TrafficMirrorFilters": List["TrafficMirrorFilterTypeDef"], "NextToken": str},
    total=False,
)

DescribeTrafficMirrorSessionsResultTypeDef = TypedDict(
    "DescribeTrafficMirrorSessionsResultTypeDef",
    {"TrafficMirrorSessions": List["TrafficMirrorSessionTypeDef"], "NextToken": str},
    total=False,
)

DescribeTrafficMirrorTargetsResultTypeDef = TypedDict(
    "DescribeTrafficMirrorTargetsResultTypeDef",
    {"TrafficMirrorTargets": List["TrafficMirrorTargetTypeDef"], "NextToken": str},
    total=False,
)

DescribeTransitGatewayAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayAttachmentsResultTypeDef",
    {"TransitGatewayAttachments": List["TransitGatewayAttachmentTypeDef"], "NextToken": str},
    total=False,
)

DescribeTransitGatewayMulticastDomainsResultTypeDef = TypedDict(
    "DescribeTransitGatewayMulticastDomainsResultTypeDef",
    {
        "TransitGatewayMulticastDomains": List["TransitGatewayMulticastDomainTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeTransitGatewayPeeringAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayPeeringAttachmentsResultTypeDef",
    {
        "TransitGatewayPeeringAttachments": List["TransitGatewayPeeringAttachmentTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeTransitGatewayRouteTablesResultTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTablesResultTypeDef",
    {"TransitGatewayRouteTables": List["TransitGatewayRouteTableTypeDef"], "NextToken": str},
    total=False,
)

DescribeTransitGatewayVpcAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayVpcAttachmentsResultTypeDef",
    {"TransitGatewayVpcAttachments": List["TransitGatewayVpcAttachmentTypeDef"], "NextToken": str},
    total=False,
)

DescribeTransitGatewaysResultTypeDef = TypedDict(
    "DescribeTransitGatewaysResultTypeDef",
    {"TransitGateways": List["TransitGatewayTypeDef"], "NextToken": str},
    total=False,
)

DescribeVolumeAttributeResultTypeDef = TypedDict(
    "DescribeVolumeAttributeResultTypeDef",
    {
        "AutoEnableIO": "AttributeBooleanValueTypeDef",
        "ProductCodes": List["ProductCodeTypeDef"],
        "VolumeId": str,
    },
    total=False,
)

DescribeVolumeStatusResultTypeDef = TypedDict(
    "DescribeVolumeStatusResultTypeDef",
    {"NextToken": str, "VolumeStatuses": List["VolumeStatusItemTypeDef"]},
    total=False,
)

DescribeVolumesModificationsResultTypeDef = TypedDict(
    "DescribeVolumesModificationsResultTypeDef",
    {"VolumesModifications": List["VolumeModificationTypeDef"], "NextToken": str},
    total=False,
)

DescribeVolumesResultTypeDef = TypedDict(
    "DescribeVolumesResultTypeDef",
    {"Volumes": List["VolumeTypeDef"], "NextToken": str},
    total=False,
)

DescribeVpcAttributeResultTypeDef = TypedDict(
    "DescribeVpcAttributeResultTypeDef",
    {
        "VpcId": str,
        "EnableDnsHostnames": "AttributeBooleanValueTypeDef",
        "EnableDnsSupport": "AttributeBooleanValueTypeDef",
    },
    total=False,
)

DescribeVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "DescribeVpcClassicLinkDnsSupportResultTypeDef",
    {"NextToken": str, "Vpcs": List["ClassicLinkDnsSupportTypeDef"]},
    total=False,
)

DescribeVpcClassicLinkResultTypeDef = TypedDict(
    "DescribeVpcClassicLinkResultTypeDef", {"Vpcs": List["VpcClassicLinkTypeDef"]}, total=False
)

DescribeVpcEndpointConnectionNotificationsResultTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionNotificationsResultTypeDef",
    {"ConnectionNotificationSet": List["ConnectionNotificationTypeDef"], "NextToken": str},
    total=False,
)

DescribeVpcEndpointConnectionsResultTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionsResultTypeDef",
    {"VpcEndpointConnections": List["VpcEndpointConnectionTypeDef"], "NextToken": str},
    total=False,
)

DescribeVpcEndpointServiceConfigurationsResultTypeDef = TypedDict(
    "DescribeVpcEndpointServiceConfigurationsResultTypeDef",
    {"ServiceConfigurations": List["ServiceConfigurationTypeDef"], "NextToken": str},
    total=False,
)

DescribeVpcEndpointServicePermissionsResultTypeDef = TypedDict(
    "DescribeVpcEndpointServicePermissionsResultTypeDef",
    {"AllowedPrincipals": List["AllowedPrincipalTypeDef"], "NextToken": str},
    total=False,
)

DescribeVpcEndpointServicesResultTypeDef = TypedDict(
    "DescribeVpcEndpointServicesResultTypeDef",
    {"ServiceNames": List[str], "ServiceDetails": List["ServiceDetailTypeDef"], "NextToken": str},
    total=False,
)

DescribeVpcEndpointsResultTypeDef = TypedDict(
    "DescribeVpcEndpointsResultTypeDef",
    {"VpcEndpoints": List["VpcEndpointTypeDef"], "NextToken": str},
    total=False,
)

DescribeVpcPeeringConnectionsResultTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsResultTypeDef",
    {"VpcPeeringConnections": List["VpcPeeringConnectionTypeDef"], "NextToken": str},
    total=False,
)

DescribeVpcsResultTypeDef = TypedDict(
    "DescribeVpcsResultTypeDef", {"Vpcs": List["VpcTypeDef"], "NextToken": str}, total=False
)

DescribeVpnConnectionsResultTypeDef = TypedDict(
    "DescribeVpnConnectionsResultTypeDef",
    {"VpnConnections": List["VpnConnectionTypeDef"]},
    total=False,
)

DescribeVpnGatewaysResultTypeDef = TypedDict(
    "DescribeVpnGatewaysResultTypeDef", {"VpnGateways": List["VpnGatewayTypeDef"]}, total=False
)

DetachClassicLinkVpcResultTypeDef = TypedDict(
    "DetachClassicLinkVpcResultTypeDef", {"Return": bool}, total=False
)

DisableEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "DisableEbsEncryptionByDefaultResultTypeDef", {"EbsEncryptionByDefault": bool}, total=False
)

DisableFastSnapshotRestoresResultTypeDef = TypedDict(
    "DisableFastSnapshotRestoresResultTypeDef",
    {
        "Successful": List["DisableFastSnapshotRestoreSuccessItemTypeDef"],
        "Unsuccessful": List["DisableFastSnapshotRestoreErrorItemTypeDef"],
    },
    total=False,
)

DisableTransitGatewayRouteTablePropagationResultTypeDef = TypedDict(
    "DisableTransitGatewayRouteTablePropagationResultTypeDef",
    {"Propagation": "TransitGatewayPropagationTypeDef"},
    total=False,
)

DisableVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "DisableVpcClassicLinkDnsSupportResultTypeDef", {"Return": bool}, total=False
)

DisableVpcClassicLinkResultTypeDef = TypedDict(
    "DisableVpcClassicLinkResultTypeDef", {"Return": bool}, total=False
)

DisassociateClientVpnTargetNetworkResultTypeDef = TypedDict(
    "DisassociateClientVpnTargetNetworkResultTypeDef",
    {"AssociationId": str, "Status": "AssociationStatusTypeDef"},
    total=False,
)

DisassociateIamInstanceProfileResultTypeDef = TypedDict(
    "DisassociateIamInstanceProfileResultTypeDef",
    {"IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef"},
    total=False,
)

DisassociateSubnetCidrBlockResultTypeDef = TypedDict(
    "DisassociateSubnetCidrBlockResultTypeDef",
    {"Ipv6CidrBlockAssociation": "SubnetIpv6CidrBlockAssociationTypeDef", "SubnetId": str},
    total=False,
)

DisassociateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "DisassociateTransitGatewayMulticastDomainResultTypeDef",
    {"Associations": "TransitGatewayMulticastDomainAssociationsTypeDef"},
    total=False,
)

DisassociateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "DisassociateTransitGatewayRouteTableResultTypeDef",
    {"Association": "TransitGatewayAssociationTypeDef"},
    total=False,
)

DisassociateVpcCidrBlockResultTypeDef = TypedDict(
    "DisassociateVpcCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": "VpcIpv6CidrBlockAssociationTypeDef",
        "CidrBlockAssociation": "VpcCidrBlockAssociationTypeDef",
        "VpcId": str,
    },
    total=False,
)

DiskImageTypeDef = TypedDict(
    "DiskImageTypeDef",
    {"Description": str, "Image": "DiskImageDetailTypeDef", "Volume": "VolumeDetailTypeDef"},
    total=False,
)

DnsServersOptionsModifyStructureTypeDef = TypedDict(
    "DnsServersOptionsModifyStructureTypeDef",
    {"CustomDnsServers": List[str], "Enabled": bool},
    total=False,
)

_RequiredElasticInferenceAcceleratorTypeDef = TypedDict(
    "_RequiredElasticInferenceAcceleratorTypeDef", {"Type": str}
)
_OptionalElasticInferenceAcceleratorTypeDef = TypedDict(
    "_OptionalElasticInferenceAcceleratorTypeDef", {"Count": int}, total=False
)


class ElasticInferenceAcceleratorTypeDef(
    _RequiredElasticInferenceAcceleratorTypeDef, _OptionalElasticInferenceAcceleratorTypeDef
):
    pass


EnableEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "EnableEbsEncryptionByDefaultResultTypeDef", {"EbsEncryptionByDefault": bool}, total=False
)

EnableFastSnapshotRestoresResultTypeDef = TypedDict(
    "EnableFastSnapshotRestoresResultTypeDef",
    {
        "Successful": List["EnableFastSnapshotRestoreSuccessItemTypeDef"],
        "Unsuccessful": List["EnableFastSnapshotRestoreErrorItemTypeDef"],
    },
    total=False,
)

EnableTransitGatewayRouteTablePropagationResultTypeDef = TypedDict(
    "EnableTransitGatewayRouteTablePropagationResultTypeDef",
    {"Propagation": "TransitGatewayPropagationTypeDef"},
    total=False,
)

EnableVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "EnableVpcClassicLinkDnsSupportResultTypeDef", {"Return": bool}, total=False
)

EnableVpcClassicLinkResultTypeDef = TypedDict(
    "EnableVpcClassicLinkResultTypeDef", {"Return": bool}, total=False
)

ExportClientVpnClientCertificateRevocationListResultTypeDef = TypedDict(
    "ExportClientVpnClientCertificateRevocationListResultTypeDef",
    {"CertificateRevocationList": str, "Status": "ClientCertificateRevocationListStatusTypeDef"},
    total=False,
)

ExportClientVpnClientConfigurationResultTypeDef = TypedDict(
    "ExportClientVpnClientConfigurationResultTypeDef", {"ClientConfiguration": str}, total=False
)

ExportImageResultTypeDef = TypedDict(
    "ExportImageResultTypeDef",
    {
        "Description": str,
        "DiskImageFormat": Literal["VMDK", "RAW", "VHD"],
        "ExportImageTaskId": str,
        "ImageId": str,
        "RoleName": str,
        "Progress": str,
        "S3ExportLocation": "ExportTaskS3LocationTypeDef",
        "Status": str,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredExportTaskS3LocationRequestTypeDef = TypedDict(
    "_RequiredExportTaskS3LocationRequestTypeDef", {"S3Bucket": str}
)
_OptionalExportTaskS3LocationRequestTypeDef = TypedDict(
    "_OptionalExportTaskS3LocationRequestTypeDef", {"S3Prefix": str}, total=False
)


class ExportTaskS3LocationRequestTypeDef(
    _RequiredExportTaskS3LocationRequestTypeDef, _OptionalExportTaskS3LocationRequestTypeDef
):
    pass


ExportToS3TaskSpecificationTypeDef = TypedDict(
    "ExportToS3TaskSpecificationTypeDef",
    {
        "ContainerFormat": Literal["ova"],
        "DiskImageFormat": Literal["VMDK", "RAW", "VHD"],
        "S3Bucket": str,
        "S3Prefix": str,
    },
    total=False,
)

ExportTransitGatewayRoutesResultTypeDef = TypedDict(
    "ExportTransitGatewayRoutesResultTypeDef", {"S3Location": str}, total=False
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]}, total=False)

FleetLaunchTemplateConfigRequestTypeDef = TypedDict(
    "FleetLaunchTemplateConfigRequestTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationRequestTypeDef",
        "Overrides": List["FleetLaunchTemplateOverridesRequestTypeDef"],
    },
    total=False,
)

GetAssociatedIpv6PoolCidrsResultTypeDef = TypedDict(
    "GetAssociatedIpv6PoolCidrsResultTypeDef",
    {"Ipv6CidrAssociations": List["Ipv6CidrAssociationTypeDef"], "NextToken": str},
    total=False,
)

GetCapacityReservationUsageResultTypeDef = TypedDict(
    "GetCapacityReservationUsageResultTypeDef",
    {
        "NextToken": str,
        "CapacityReservationId": str,
        "InstanceType": str,
        "TotalInstanceCount": int,
        "AvailableInstanceCount": int,
        "State": Literal["active", "expired", "cancelled", "pending", "failed"],
        "InstanceUsages": List["InstanceUsageTypeDef"],
    },
    total=False,
)

GetCoipPoolUsageResultTypeDef = TypedDict(
    "GetCoipPoolUsageResultTypeDef",
    {
        "CoipPoolId": str,
        "CoipAddressUsages": List["CoipAddressUsageTypeDef"],
        "LocalGatewayRouteTableId": str,
    },
    total=False,
)

GetConsoleOutputResultTypeDef = TypedDict(
    "GetConsoleOutputResultTypeDef",
    {"InstanceId": str, "Output": str, "Timestamp": datetime},
    total=False,
)

GetConsoleScreenshotResultTypeDef = TypedDict(
    "GetConsoleScreenshotResultTypeDef", {"ImageData": str, "InstanceId": str}, total=False
)

GetDefaultCreditSpecificationResultTypeDef = TypedDict(
    "GetDefaultCreditSpecificationResultTypeDef",
    {"InstanceFamilyCreditSpecification": "InstanceFamilyCreditSpecificationTypeDef"},
    total=False,
)

GetEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "GetEbsDefaultKmsKeyIdResultTypeDef", {"KmsKeyId": str}, total=False
)

GetEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "GetEbsEncryptionByDefaultResultTypeDef", {"EbsEncryptionByDefault": bool}, total=False
)

GetGroupsForCapacityReservationResultTypeDef = TypedDict(
    "GetGroupsForCapacityReservationResultTypeDef",
    {"NextToken": str, "CapacityReservationGroups": List["CapacityReservationGroupTypeDef"]},
    total=False,
)

GetHostReservationPurchasePreviewResultTypeDef = TypedDict(
    "GetHostReservationPurchasePreviewResultTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Purchase": List["PurchaseTypeDef"],
        "TotalHourlyPrice": str,
        "TotalUpfrontPrice": str,
    },
    total=False,
)

GetLaunchTemplateDataResultTypeDef = TypedDict(
    "GetLaunchTemplateDataResultTypeDef",
    {"LaunchTemplateData": "ResponseLaunchTemplateDataTypeDef"},
    total=False,
)

GetManagedPrefixListAssociationsResultTypeDef = TypedDict(
    "GetManagedPrefixListAssociationsResultTypeDef",
    {"PrefixListAssociations": List["PrefixListAssociationTypeDef"], "NextToken": str},
    total=False,
)

GetManagedPrefixListEntriesResultTypeDef = TypedDict(
    "GetManagedPrefixListEntriesResultTypeDef",
    {"Entries": List["PrefixListEntryTypeDef"], "NextToken": str},
    total=False,
)

GetPasswordDataResultTypeDef = TypedDict(
    "GetPasswordDataResultTypeDef",
    {"InstanceId": str, "PasswordData": str, "Timestamp": datetime},
    total=False,
)

GetReservedInstancesExchangeQuoteResultTypeDef = TypedDict(
    "GetReservedInstancesExchangeQuoteResultTypeDef",
    {
        "CurrencyCode": str,
        "IsValidExchange": bool,
        "OutputReservedInstancesWillExpireAt": datetime,
        "PaymentDue": str,
        "ReservedInstanceValueRollup": "ReservationValueTypeDef",
        "ReservedInstanceValueSet": List["ReservedInstanceReservationValueTypeDef"],
        "TargetConfigurationValueRollup": "ReservationValueTypeDef",
        "TargetConfigurationValueSet": List["TargetReservationValueTypeDef"],
        "ValidationFailureReason": str,
    },
    total=False,
)

GetTransitGatewayAttachmentPropagationsResultTypeDef = TypedDict(
    "GetTransitGatewayAttachmentPropagationsResultTypeDef",
    {
        "TransitGatewayAttachmentPropagations": List["TransitGatewayAttachmentPropagationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetTransitGatewayMulticastDomainAssociationsResultTypeDef = TypedDict(
    "GetTransitGatewayMulticastDomainAssociationsResultTypeDef",
    {
        "MulticastDomainAssociations": List["TransitGatewayMulticastDomainAssociationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetTransitGatewayRouteTableAssociationsResultTypeDef = TypedDict(
    "GetTransitGatewayRouteTableAssociationsResultTypeDef",
    {"Associations": List["TransitGatewayRouteTableAssociationTypeDef"], "NextToken": str},
    total=False,
)

GetTransitGatewayRouteTablePropagationsResultTypeDef = TypedDict(
    "GetTransitGatewayRouteTablePropagationsResultTypeDef",
    {
        "TransitGatewayRouteTablePropagations": List["TransitGatewayRouteTablePropagationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

HibernationOptionsRequestTypeDef = TypedDict(
    "HibernationOptionsRequestTypeDef", {"Configured": bool}, total=False
)

ImageAttributeTypeDef = TypedDict(
    "ImageAttributeTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "ImageId": str,
        "LaunchPermissions": List["LaunchPermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
        "Description": "AttributeValueTypeDef",
        "KernelId": "AttributeValueTypeDef",
        "RamdiskId": "AttributeValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
    },
    total=False,
)

ImageDiskContainerTypeDef = TypedDict(
    "ImageDiskContainerTypeDef",
    {
        "Description": str,
        "DeviceName": str,
        "Format": str,
        "SnapshotId": str,
        "Url": str,
        "UserBucket": "UserBucketTypeDef",
    },
    total=False,
)

ImportClientVpnClientCertificateRevocationListResultTypeDef = TypedDict(
    "ImportClientVpnClientCertificateRevocationListResultTypeDef", {"Return": bool}, total=False
)

ImportImageLicenseConfigurationRequestTypeDef = TypedDict(
    "ImportImageLicenseConfigurationRequestTypeDef", {"LicenseConfigurationArn": str}, total=False
)

ImportImageResultTypeDef = TypedDict(
    "ImportImageResultTypeDef",
    {
        "Architecture": str,
        "Description": str,
        "Encrypted": bool,
        "Hypervisor": str,
        "ImageId": str,
        "ImportTaskId": str,
        "KmsKeyId": str,
        "LicenseType": str,
        "Platform": str,
        "Progress": str,
        "SnapshotDetails": List["SnapshotDetailTypeDef"],
        "Status": str,
        "StatusMessage": str,
        "LicenseSpecifications": List["ImportImageLicenseConfigurationResponseTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ImportInstanceLaunchSpecificationTypeDef = TypedDict(
    "ImportInstanceLaunchSpecificationTypeDef",
    {
        "AdditionalInfo": str,
        "Architecture": Literal["i386", "x86_64", "arm64"],
        "GroupIds": List[str],
        "GroupNames": List[str],
        "InstanceInitiatedShutdownBehavior": Literal["stop", "terminate"],
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "Monitoring": bool,
        "Placement": "PlacementTypeDef",
        "PrivateIpAddress": str,
        "SubnetId": str,
        "UserData": "UserDataTypeDef",
    },
    total=False,
)

ImportInstanceResultTypeDef = TypedDict(
    "ImportInstanceResultTypeDef", {"ConversionTask": "ConversionTaskTypeDef"}, total=False
)

ImportKeyPairResultTypeDef = TypedDict(
    "ImportKeyPairResultTypeDef",
    {"KeyFingerprint": str, "KeyName": str, "KeyPairId": str, "Tags": List["TagTypeDef"]},
    total=False,
)

ImportSnapshotResultTypeDef = TypedDict(
    "ImportSnapshotResultTypeDef",
    {
        "Description": str,
        "ImportTaskId": str,
        "SnapshotTaskDetail": "SnapshotTaskDetailTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ImportVolumeResultTypeDef = TypedDict(
    "ImportVolumeResultTypeDef", {"ConversionTask": "ConversionTaskTypeDef"}, total=False
)

InstanceAttributeTypeDef = TypedDict(
    "InstanceAttributeTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "DisableApiTermination": "AttributeBooleanValueTypeDef",
        "EnaSupport": "AttributeBooleanValueTypeDef",
        "EbsOptimized": "AttributeBooleanValueTypeDef",
        "InstanceId": str,
        "InstanceInitiatedShutdownBehavior": "AttributeValueTypeDef",
        "InstanceType": "AttributeValueTypeDef",
        "KernelId": "AttributeValueTypeDef",
        "ProductCodes": List["ProductCodeTypeDef"],
        "RamdiskId": "AttributeValueTypeDef",
        "RootDeviceName": "AttributeValueTypeDef",
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "UserData": "AttributeValueTypeDef",
    },
    total=False,
)

InstanceBlockDeviceMappingSpecificationTypeDef = TypedDict(
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    {
        "DeviceName": str,
        "Ebs": "EbsInstanceBlockDeviceSpecificationTypeDef",
        "NoDevice": str,
        "VirtualName": str,
    },
    total=False,
)

InstanceCreditSpecificationRequestTypeDef = TypedDict(
    "InstanceCreditSpecificationRequestTypeDef", {"InstanceId": str, "CpuCredits": str}, total=False
)

InstanceMarketOptionsRequestTypeDef = TypedDict(
    "InstanceMarketOptionsRequestTypeDef",
    {"MarketType": Literal["spot"], "SpotOptions": "SpotMarketOptionsTypeDef"},
    total=False,
)

InstanceMetadataOptionsRequestTypeDef = TypedDict(
    "InstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": Literal["optional", "required"],
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": Literal["disabled", "enabled"],
    },
    total=False,
)

InstanceSpecificationTypeDef = TypedDict(
    "InstanceSpecificationTypeDef", {"InstanceId": str, "ExcludeBootVolume": bool}, total=False
)

KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "KeyFingerprint": str,
        "KeyMaterial": str,
        "KeyName": str,
        "KeyPairId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LaunchPermissionModificationsTypeDef = TypedDict(
    "LaunchPermissionModificationsTypeDef",
    {"Add": List["LaunchPermissionTypeDef"], "Remove": List["LaunchPermissionTypeDef"]},
    total=False,
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

LicenseConfigurationRequestTypeDef = TypedDict(
    "LicenseConfigurationRequestTypeDef", {"LicenseConfigurationArn": str}, total=False
)

LoadPermissionModificationsTypeDef = TypedDict(
    "LoadPermissionModificationsTypeDef",
    {"Add": List["LoadPermissionRequestTypeDef"], "Remove": List["LoadPermissionRequestTypeDef"]},
    total=False,
)

ModifyAvailabilityZoneGroupResultTypeDef = TypedDict(
    "ModifyAvailabilityZoneGroupResultTypeDef", {"Return": bool}, total=False
)

ModifyCapacityReservationResultTypeDef = TypedDict(
    "ModifyCapacityReservationResultTypeDef", {"Return": bool}, total=False
)

ModifyClientVpnEndpointResultTypeDef = TypedDict(
    "ModifyClientVpnEndpointResultTypeDef", {"Return": bool}, total=False
)

ModifyDefaultCreditSpecificationResultTypeDef = TypedDict(
    "ModifyDefaultCreditSpecificationResultTypeDef",
    {"InstanceFamilyCreditSpecification": "InstanceFamilyCreditSpecificationTypeDef"},
    total=False,
)

ModifyEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "ModifyEbsDefaultKmsKeyIdResultTypeDef", {"KmsKeyId": str}, total=False
)

ModifyFleetResultTypeDef = TypedDict("ModifyFleetResultTypeDef", {"Return": bool}, total=False)

ModifyFpgaImageAttributeResultTypeDef = TypedDict(
    "ModifyFpgaImageAttributeResultTypeDef",
    {"FpgaImageAttribute": "FpgaImageAttributeTypeDef"},
    total=False,
)

ModifyHostsResultTypeDef = TypedDict(
    "ModifyHostsResultTypeDef",
    {"Successful": List[str], "Unsuccessful": List["UnsuccessfulItemTypeDef"]},
    total=False,
)

ModifyInstanceCapacityReservationAttributesResultTypeDef = TypedDict(
    "ModifyInstanceCapacityReservationAttributesResultTypeDef", {"Return": bool}, total=False
)

ModifyInstanceCreditSpecificationResultTypeDef = TypedDict(
    "ModifyInstanceCreditSpecificationResultTypeDef",
    {
        "SuccessfulInstanceCreditSpecifications": List[
            "SuccessfulInstanceCreditSpecificationItemTypeDef"
        ],
        "UnsuccessfulInstanceCreditSpecifications": List[
            "UnsuccessfulInstanceCreditSpecificationItemTypeDef"
        ],
    },
    total=False,
)

ModifyInstanceEventStartTimeResultTypeDef = TypedDict(
    "ModifyInstanceEventStartTimeResultTypeDef",
    {"Event": "InstanceStatusEventTypeDef"},
    total=False,
)

ModifyInstanceMetadataOptionsResultTypeDef = TypedDict(
    "ModifyInstanceMetadataOptionsResultTypeDef",
    {"InstanceId": str, "InstanceMetadataOptions": "InstanceMetadataOptionsResponseTypeDef"},
    total=False,
)

ModifyInstancePlacementResultTypeDef = TypedDict(
    "ModifyInstancePlacementResultTypeDef", {"Return": bool}, total=False
)

ModifyLaunchTemplateResultTypeDef = TypedDict(
    "ModifyLaunchTemplateResultTypeDef", {"LaunchTemplate": "LaunchTemplateTypeDef"}, total=False
)

ModifyManagedPrefixListResultTypeDef = TypedDict(
    "ModifyManagedPrefixListResultTypeDef", {"PrefixList": "ManagedPrefixListTypeDef"}, total=False
)

ModifyReservedInstancesResultTypeDef = TypedDict(
    "ModifyReservedInstancesResultTypeDef", {"ReservedInstancesModificationId": str}, total=False
)

ModifySpotFleetRequestResponseTypeDef = TypedDict(
    "ModifySpotFleetRequestResponseTypeDef", {"Return": bool}, total=False
)

ModifyTrafficMirrorFilterNetworkServicesResultTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterNetworkServicesResultTypeDef",
    {"TrafficMirrorFilter": "TrafficMirrorFilterTypeDef"},
    total=False,
)

ModifyTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterRuleResultTypeDef",
    {"TrafficMirrorFilterRule": "TrafficMirrorFilterRuleTypeDef"},
    total=False,
)

ModifyTrafficMirrorSessionResultTypeDef = TypedDict(
    "ModifyTrafficMirrorSessionResultTypeDef",
    {"TrafficMirrorSession": "TrafficMirrorSessionTypeDef"},
    total=False,
)

ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    {"DnsSupport": Literal["enable", "disable"], "Ipv6Support": Literal["enable", "disable"]},
    total=False,
)

ModifyTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentResultTypeDef",
    {"TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef"},
    total=False,
)

ModifyVolumeResultTypeDef = TypedDict(
    "ModifyVolumeResultTypeDef", {"VolumeModification": "VolumeModificationTypeDef"}, total=False
)

ModifyVpcEndpointConnectionNotificationResultTypeDef = TypedDict(
    "ModifyVpcEndpointConnectionNotificationResultTypeDef", {"ReturnValue": bool}, total=False
)

ModifyVpcEndpointResultTypeDef = TypedDict(
    "ModifyVpcEndpointResultTypeDef", {"Return": bool}, total=False
)

ModifyVpcEndpointServiceConfigurationResultTypeDef = TypedDict(
    "ModifyVpcEndpointServiceConfigurationResultTypeDef", {"Return": bool}, total=False
)

ModifyVpcEndpointServicePermissionsResultTypeDef = TypedDict(
    "ModifyVpcEndpointServicePermissionsResultTypeDef", {"ReturnValue": bool}, total=False
)

ModifyVpcPeeringConnectionOptionsResultTypeDef = TypedDict(
    "ModifyVpcPeeringConnectionOptionsResultTypeDef",
    {
        "AccepterPeeringConnectionOptions": "PeeringConnectionOptionsTypeDef",
        "RequesterPeeringConnectionOptions": "PeeringConnectionOptionsTypeDef",
    },
    total=False,
)

ModifyVpcTenancyResultTypeDef = TypedDict(
    "ModifyVpcTenancyResultTypeDef", {"ReturnValue": bool}, total=False
)

ModifyVpnConnectionResultTypeDef = TypedDict(
    "ModifyVpnConnectionResultTypeDef", {"VpnConnection": "VpnConnectionTypeDef"}, total=False
)

ModifyVpnTunnelCertificateResultTypeDef = TypedDict(
    "ModifyVpnTunnelCertificateResultTypeDef",
    {"VpnConnection": "VpnConnectionTypeDef"},
    total=False,
)

ModifyVpnTunnelOptionsResultTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsResultTypeDef", {"VpnConnection": "VpnConnectionTypeDef"}, total=False
)

ModifyVpnTunnelOptionsSpecificationTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    {
        "TunnelInsideCidr": str,
        "TunnelInsideIpv6Cidr": str,
        "PreSharedKey": str,
        "Phase1LifetimeSeconds": int,
        "Phase2LifetimeSeconds": int,
        "RekeyMarginTimeSeconds": int,
        "RekeyFuzzPercentage": int,
        "ReplayWindowSize": int,
        "DPDTimeoutSeconds": int,
        "Phase1EncryptionAlgorithms": List["Phase1EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase2EncryptionAlgorithms": List["Phase2EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase1IntegrityAlgorithms": List["Phase1IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase2IntegrityAlgorithms": List["Phase2IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase1DHGroupNumbers": List["Phase1DHGroupNumbersRequestListValueTypeDef"],
        "Phase2DHGroupNumbers": List["Phase2DHGroupNumbersRequestListValueTypeDef"],
        "IKEVersions": List["IKEVersionsRequestListValueTypeDef"],
    },
    total=False,
)

MonitorInstancesResultTypeDef = TypedDict(
    "MonitorInstancesResultTypeDef",
    {"InstanceMonitorings": List["InstanceMonitoringTypeDef"]},
    total=False,
)

MoveAddressToVpcResultTypeDef = TypedDict(
    "MoveAddressToVpcResultTypeDef",
    {"AllocationId": str, "Status": Literal["MoveInProgress", "InVpc", "InClassic"]},
    total=False,
)

NetworkInterfaceAttachmentChangesTypeDef = TypedDict(
    "NetworkInterfaceAttachmentChangesTypeDef",
    {"AttachmentId": str, "DeleteOnTermination": bool},
    total=False,
)

NewDhcpConfigurationTypeDef = TypedDict(
    "NewDhcpConfigurationTypeDef", {"Key": str, "Values": List[str]}, total=False
)

OnDemandOptionsRequestTypeDef = TypedDict(
    "OnDemandOptionsRequestTypeDef",
    {
        "AllocationStrategy": Literal["lowest-price", "prioritized"],
        "CapacityReservationOptions": "CapacityReservationOptionsRequestTypeDef",
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PeeringConnectionOptionsRequestTypeDef = TypedDict(
    "PeeringConnectionOptionsRequestTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
    total=False,
)

PriceScheduleSpecificationTypeDef = TypedDict(
    "PriceScheduleSpecificationTypeDef",
    {"CurrencyCode": Literal["USD"], "Price": float, "Term": int},
    total=False,
)

ProvisionByoipCidrResultTypeDef = TypedDict(
    "ProvisionByoipCidrResultTypeDef", {"ByoipCidr": "ByoipCidrTypeDef"}, total=False
)

PurchaseHostReservationResultTypeDef = TypedDict(
    "PurchaseHostReservationResultTypeDef",
    {
        "ClientToken": str,
        "CurrencyCode": Literal["USD"],
        "Purchase": List["PurchaseTypeDef"],
        "TotalHourlyPrice": str,
        "TotalUpfrontPrice": str,
    },
    total=False,
)

PurchaseRequestTypeDef = TypedDict(
    "PurchaseRequestTypeDef", {"InstanceCount": int, "PurchaseToken": str}
)

PurchaseReservedInstancesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedInstancesOfferingResultTypeDef", {"ReservedInstancesId": str}, total=False
)

PurchaseScheduledInstancesResultTypeDef = TypedDict(
    "PurchaseScheduledInstancesResultTypeDef",
    {"ScheduledInstanceSet": List["ScheduledInstanceTypeDef"]},
    total=False,
)

RegisterImageResultTypeDef = TypedDict("RegisterImageResultTypeDef", {"ImageId": str}, total=False)

RegisterInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "RegisterInstanceEventNotificationAttributesResultTypeDef",
    {"InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef"},
    total=False,
)

RegisterInstanceTagAttributeRequestTypeDef = TypedDict(
    "RegisterInstanceTagAttributeRequestTypeDef",
    {"IncludeAllTagsOfInstance": bool, "InstanceTagKeys": List[str]},
    total=False,
)

RegisterTransitGatewayMulticastGroupMembersResultTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupMembersResultTypeDef",
    {"RegisteredMulticastGroupMembers": "TransitGatewayMulticastRegisteredGroupMembersTypeDef"},
    total=False,
)

RegisterTransitGatewayMulticastGroupSourcesResultTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    {"RegisteredMulticastGroupSources": "TransitGatewayMulticastRegisteredGroupSourcesTypeDef"},
    total=False,
)

RejectTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "RejectTransitGatewayPeeringAttachmentResultTypeDef",
    {"TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef"},
    total=False,
)

RejectTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "RejectTransitGatewayVpcAttachmentResultTypeDef",
    {"TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef"},
    total=False,
)

RejectVpcEndpointConnectionsResultTypeDef = TypedDict(
    "RejectVpcEndpointConnectionsResultTypeDef",
    {"Unsuccessful": List["UnsuccessfulItemTypeDef"]},
    total=False,
)

RejectVpcPeeringConnectionResultTypeDef = TypedDict(
    "RejectVpcPeeringConnectionResultTypeDef", {"Return": bool}, total=False
)

ReleaseHostsResultTypeDef = TypedDict(
    "ReleaseHostsResultTypeDef",
    {"Successful": List[str], "Unsuccessful": List["UnsuccessfulItemTypeDef"]},
    total=False,
)

RemovePrefixListEntryTypeDef = TypedDict("RemovePrefixListEntryTypeDef", {"Cidr": str})

ReplaceIamInstanceProfileAssociationResultTypeDef = TypedDict(
    "ReplaceIamInstanceProfileAssociationResultTypeDef",
    {"IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef"},
    total=False,
)

ReplaceNetworkAclAssociationResultTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationResultTypeDef", {"NewAssociationId": str}, total=False
)

ReplaceRouteTableAssociationResultTypeDef = TypedDict(
    "ReplaceRouteTableAssociationResultTypeDef",
    {"NewAssociationId": str, "AssociationState": "RouteTableAssociationStateTypeDef"},
    total=False,
)

ReplaceTransitGatewayRouteResultTypeDef = TypedDict(
    "ReplaceTransitGatewayRouteResultTypeDef", {"Route": "TransitGatewayRouteTypeDef"}, total=False
)

RequestLaunchTemplateDataTypeDef = TypedDict(
    "RequestLaunchTemplateDataTypeDef",
    {
        "KernelId": str,
        "EbsOptimized": bool,
        "IamInstanceProfile": "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
        "BlockDeviceMappings": List["LaunchTemplateBlockDeviceMappingRequestTypeDef"],
        "NetworkInterfaces": List[
            "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef"
        ],
        "ImageId": str,
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "KeyName": str,
        "Monitoring": "LaunchTemplatesMonitoringRequestTypeDef",
        "Placement": "LaunchTemplatePlacementRequestTypeDef",
        "RamDiskId": str,
        "DisableApiTermination": bool,
        "InstanceInitiatedShutdownBehavior": Literal["stop", "terminate"],
        "UserData": str,
        "TagSpecifications": List["LaunchTemplateTagSpecificationRequestTypeDef"],
        "ElasticGpuSpecifications": List["ElasticGpuSpecificationTypeDef"],
        "ElasticInferenceAccelerators": List["LaunchTemplateElasticInferenceAcceleratorTypeDef"],
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "InstanceMarketOptions": "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
        "CreditSpecification": "CreditSpecificationRequestTypeDef",
        "CpuOptions": "LaunchTemplateCpuOptionsRequestTypeDef",
        "CapacityReservationSpecification": "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
        "LicenseSpecifications": List["LaunchTemplateLicenseConfigurationRequestTypeDef"],
        "HibernationOptions": "LaunchTemplateHibernationOptionsRequestTypeDef",
        "MetadataOptions": "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    },
    total=False,
)

RequestSpotFleetResponseTypeDef = TypedDict(
    "RequestSpotFleetResponseTypeDef", {"SpotFleetRequestId": str}, total=False
)

RequestSpotInstancesResultTypeDef = TypedDict(
    "RequestSpotInstancesResultTypeDef",
    {"SpotInstanceRequests": List["SpotInstanceRequestTypeDef"]},
    total=False,
)

RequestSpotLaunchSpecificationTypeDef = TypedDict(
    "RequestSpotLaunchSpecificationTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "AddressingType": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "ImageId": str,
        "InstanceType": Literal[
            "t1.micro",
            "t2.nano",
            "t2.micro",
            "t2.small",
            "t2.medium",
            "t2.large",
            "t2.xlarge",
            "t2.2xlarge",
            "t3.nano",
            "t3.micro",
            "t3.small",
            "t3.medium",
            "t3.large",
            "t3.xlarge",
            "t3.2xlarge",
            "t3a.nano",
            "t3a.micro",
            "t3a.small",
            "t3a.medium",
            "t3a.large",
            "t3a.xlarge",
            "t3a.2xlarge",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m3.medium",
            "m3.large",
            "m3.xlarge",
            "m3.2xlarge",
            "m4.large",
            "m4.xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.10xlarge",
            "m4.16xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "cr1.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.16xlarge",
            "r5.large",
            "r5.xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.metal",
            "r5a.large",
            "r5a.xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5d.large",
            "r5d.xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.metal",
            "r5ad.large",
            "r5ad.xlarge",
            "r5ad.2xlarge",
            "r5ad.4xlarge",
            "r5ad.8xlarge",
            "r5ad.12xlarge",
            "r5ad.16xlarge",
            "r5ad.24xlarge",
            "r6g.metal",
            "r6g.medium",
            "r6g.large",
            "r6g.xlarge",
            "r6g.2xlarge",
            "r6g.4xlarge",
            "r6g.8xlarge",
            "r6g.12xlarge",
            "r6g.16xlarge",
            "r6gd.metal",
            "r6gd.medium",
            "r6gd.large",
            "r6gd.xlarge",
            "r6gd.2xlarge",
            "r6gd.4xlarge",
            "r6gd.8xlarge",
            "r6gd.12xlarge",
            "r6gd.16xlarge",
            "x1.16xlarge",
            "x1.32xlarge",
            "x1e.xlarge",
            "x1e.2xlarge",
            "x1e.4xlarge",
            "x1e.8xlarge",
            "x1e.16xlarge",
            "x1e.32xlarge",
            "i2.xlarge",
            "i2.2xlarge",
            "i2.4xlarge",
            "i2.8xlarge",
            "i3.large",
            "i3.xlarge",
            "i3.2xlarge",
            "i3.4xlarge",
            "i3.8xlarge",
            "i3.16xlarge",
            "i3.metal",
            "i3en.large",
            "i3en.xlarge",
            "i3en.2xlarge",
            "i3en.3xlarge",
            "i3en.6xlarge",
            "i3en.12xlarge",
            "i3en.24xlarge",
            "i3en.metal",
            "hi1.4xlarge",
            "hs1.8xlarge",
            "c1.medium",
            "c1.xlarge",
            "c3.large",
            "c3.xlarge",
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c5.large",
            "c5.xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.metal",
            "c5a.large",
            "c5a.xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5ad.large",
            "c5ad.xlarge",
            "c5ad.2xlarge",
            "c5ad.4xlarge",
            "c5ad.8xlarge",
            "c5ad.12xlarge",
            "c5ad.16xlarge",
            "c5ad.24xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.metal",
            "c5n.large",
            "c5n.xlarge",
            "c5n.2xlarge",
            "c5n.4xlarge",
            "c5n.9xlarge",
            "c5n.18xlarge",
            "c6g.metal",
            "c6g.medium",
            "c6g.large",
            "c6g.xlarge",
            "c6g.2xlarge",
            "c6g.4xlarge",
            "c6g.8xlarge",
            "c6g.12xlarge",
            "c6g.16xlarge",
            "c6gd.metal",
            "c6gd.medium",
            "c6gd.large",
            "c6gd.xlarge",
            "c6gd.2xlarge",
            "c6gd.4xlarge",
            "c6gd.8xlarge",
            "c6gd.12xlarge",
            "c6gd.16xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "g2.2xlarge",
            "g2.8xlarge",
            "g3.4xlarge",
            "g3.8xlarge",
            "g3.16xlarge",
            "g3s.xlarge",
            "g4dn.xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.metal",
            "cg1.4xlarge",
            "p2.xlarge",
            "p2.8xlarge",
            "p2.16xlarge",
            "p3.2xlarge",
            "p3.8xlarge",
            "p3.16xlarge",
            "p3dn.24xlarge",
            "d2.xlarge",
            "d2.2xlarge",
            "d2.4xlarge",
            "d2.8xlarge",
            "f1.2xlarge",
            "f1.4xlarge",
            "f1.16xlarge",
            "m5.large",
            "m5.xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.metal",
            "m5a.large",
            "m5a.xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5d.large",
            "m5d.xlarge",
            "m5d.2xlarge",
            "m5d.4xlarge",
            "m5d.8xlarge",
            "m5d.12xlarge",
            "m5d.16xlarge",
            "m5d.24xlarge",
            "m5d.metal",
            "m5ad.large",
            "m5ad.xlarge",
            "m5ad.2xlarge",
            "m5ad.4xlarge",
            "m5ad.8xlarge",
            "m5ad.12xlarge",
            "m5ad.16xlarge",
            "m5ad.24xlarge",
            "h1.2xlarge",
            "h1.4xlarge",
            "h1.8xlarge",
            "h1.16xlarge",
            "z1d.large",
            "z1d.xlarge",
            "z1d.2xlarge",
            "z1d.3xlarge",
            "z1d.6xlarge",
            "z1d.12xlarge",
            "z1d.metal",
            "u-6tb1.metal",
            "u-9tb1.metal",
            "u-12tb1.metal",
            "u-18tb1.metal",
            "u-24tb1.metal",
            "a1.medium",
            "a1.large",
            "a1.xlarge",
            "a1.2xlarge",
            "a1.4xlarge",
            "a1.metal",
            "m5dn.large",
            "m5dn.xlarge",
            "m5dn.2xlarge",
            "m5dn.4xlarge",
            "m5dn.8xlarge",
            "m5dn.12xlarge",
            "m5dn.16xlarge",
            "m5dn.24xlarge",
            "m5n.large",
            "m5n.xlarge",
            "m5n.2xlarge",
            "m5n.4xlarge",
            "m5n.8xlarge",
            "m5n.12xlarge",
            "m5n.16xlarge",
            "m5n.24xlarge",
            "r5dn.large",
            "r5dn.xlarge",
            "r5dn.2xlarge",
            "r5dn.4xlarge",
            "r5dn.8xlarge",
            "r5dn.12xlarge",
            "r5dn.16xlarge",
            "r5dn.24xlarge",
            "r5n.large",
            "r5n.xlarge",
            "r5n.2xlarge",
            "r5n.4xlarge",
            "r5n.8xlarge",
            "r5n.12xlarge",
            "r5n.16xlarge",
            "r5n.24xlarge",
            "inf1.xlarge",
            "inf1.2xlarge",
            "inf1.6xlarge",
            "inf1.24xlarge",
            "m6g.metal",
            "m6g.medium",
            "m6g.large",
            "m6g.xlarge",
            "m6g.2xlarge",
            "m6g.4xlarge",
            "m6g.8xlarge",
            "m6g.12xlarge",
            "m6g.16xlarge",
            "m6gd.metal",
            "m6gd.medium",
            "m6gd.large",
            "m6gd.xlarge",
            "m6gd.2xlarge",
            "m6gd.4xlarge",
            "m6gd.8xlarge",
            "m6gd.12xlarge",
            "m6gd.16xlarge",
        ],
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "Placement": "SpotPlacementTypeDef",
        "RamdiskId": str,
        "SubnetId": str,
        "UserData": str,
    },
    total=False,
)

ReservedInstanceLimitPriceTypeDef = TypedDict(
    "ReservedInstanceLimitPriceTypeDef",
    {"Amount": float, "CurrencyCode": Literal["USD"]},
    total=False,
)

ResetEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "ResetEbsDefaultKmsKeyIdResultTypeDef", {"KmsKeyId": str}, total=False
)

ResetFpgaImageAttributeResultTypeDef = TypedDict(
    "ResetFpgaImageAttributeResultTypeDef", {"Return": bool}, total=False
)

RestoreAddressToClassicResultTypeDef = TypedDict(
    "RestoreAddressToClassicResultTypeDef",
    {"PublicIp": str, "Status": Literal["MoveInProgress", "InVpc", "InClassic"]},
    total=False,
)

RestoreManagedPrefixListVersionResultTypeDef = TypedDict(
    "RestoreManagedPrefixListVersionResultTypeDef",
    {"PrefixList": "ManagedPrefixListTypeDef"},
    total=False,
)

RevokeClientVpnIngressResultTypeDef = TypedDict(
    "RevokeClientVpnIngressResultTypeDef",
    {"Status": "ClientVpnAuthorizationRuleStatusTypeDef"},
    total=False,
)

RunScheduledInstancesResultTypeDef = TypedDict(
    "RunScheduledInstancesResultTypeDef", {"InstanceIdSet": List[str]}, total=False
)

ScheduledInstanceRecurrenceRequestTypeDef = TypedDict(
    "ScheduledInstanceRecurrenceRequestTypeDef",
    {
        "Frequency": str,
        "Interval": int,
        "OccurrenceDays": List[int],
        "OccurrenceRelativeToEnd": bool,
        "OccurrenceUnit": str,
    },
    total=False,
)

_RequiredScheduledInstancesLaunchSpecificationTypeDef = TypedDict(
    "_RequiredScheduledInstancesLaunchSpecificationTypeDef", {"ImageId": str}
)
_OptionalScheduledInstancesLaunchSpecificationTypeDef = TypedDict(
    "_OptionalScheduledInstancesLaunchSpecificationTypeDef",
    {
        "BlockDeviceMappings": List["ScheduledInstancesBlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "ScheduledInstancesIamInstanceProfileTypeDef",
        "InstanceType": str,
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "ScheduledInstancesMonitoringTypeDef",
        "NetworkInterfaces": List["ScheduledInstancesNetworkInterfaceTypeDef"],
        "Placement": "ScheduledInstancesPlacementTypeDef",
        "RamdiskId": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "UserData": str,
    },
    total=False,
)


class ScheduledInstancesLaunchSpecificationTypeDef(
    _RequiredScheduledInstancesLaunchSpecificationTypeDef,
    _OptionalScheduledInstancesLaunchSpecificationTypeDef,
):
    pass


SearchLocalGatewayRoutesResultTypeDef = TypedDict(
    "SearchLocalGatewayRoutesResultTypeDef",
    {"Routes": List["LocalGatewayRouteTypeDef"], "NextToken": str},
    total=False,
)

SearchTransitGatewayMulticastGroupsResultTypeDef = TypedDict(
    "SearchTransitGatewayMulticastGroupsResultTypeDef",
    {"MulticastGroups": List["TransitGatewayMulticastGroupTypeDef"], "NextToken": str},
    total=False,
)

SearchTransitGatewayRoutesResultTypeDef = TypedDict(
    "SearchTransitGatewayRoutesResultTypeDef",
    {"Routes": List["TransitGatewayRouteTypeDef"], "AdditionalRoutesAvailable": bool},
    total=False,
)

SlotDateTimeRangeRequestTypeDef = TypedDict(
    "SlotDateTimeRangeRequestTypeDef", {"EarliestTime": datetime, "LatestTime": datetime}
)

SlotStartTimeRangeRequestTypeDef = TypedDict(
    "SlotStartTimeRangeRequestTypeDef",
    {"EarliestTime": datetime, "LatestTime": datetime},
    total=False,
)

SnapshotDiskContainerTypeDef = TypedDict(
    "SnapshotDiskContainerTypeDef",
    {"Description": str, "Format": str, "Url": str, "UserBucket": "UserBucketTypeDef"},
    total=False,
)

SpotOptionsRequestTypeDef = TypedDict(
    "SpotOptionsRequestTypeDef",
    {
        "AllocationStrategy": Literal["lowest-price", "diversified", "capacity-optimized"],
        "InstanceInterruptionBehavior": Literal["hibernate", "stop", "terminate"],
        "InstancePoolsToUseCount": int,
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

StartInstancesResultTypeDef = TypedDict(
    "StartInstancesResultTypeDef",
    {"StartingInstances": List["InstanceStateChangeTypeDef"]},
    total=False,
)

StartVpcEndpointServicePrivateDnsVerificationResultTypeDef = TypedDict(
    "StartVpcEndpointServicePrivateDnsVerificationResultTypeDef", {"ReturnValue": bool}, total=False
)

StopInstancesResultTypeDef = TypedDict(
    "StopInstancesResultTypeDef",
    {"StoppingInstances": List["InstanceStateChangeTypeDef"]},
    total=False,
)

StorageLocationTypeDef = TypedDict(
    "StorageLocationTypeDef", {"Bucket": str, "Key": str}, total=False
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


_RequiredTargetCapacitySpecificationRequestTypeDef = TypedDict(
    "_RequiredTargetCapacitySpecificationRequestTypeDef", {"TotalTargetCapacity": int}
)
_OptionalTargetCapacitySpecificationRequestTypeDef = TypedDict(
    "_OptionalTargetCapacitySpecificationRequestTypeDef",
    {
        "OnDemandTargetCapacity": int,
        "SpotTargetCapacity": int,
        "DefaultTargetCapacityType": Literal["spot", "on-demand"],
    },
    total=False,
)


class TargetCapacitySpecificationRequestTypeDef(
    _RequiredTargetCapacitySpecificationRequestTypeDef,
    _OptionalTargetCapacitySpecificationRequestTypeDef,
):
    pass


_RequiredTargetConfigurationRequestTypeDef = TypedDict(
    "_RequiredTargetConfigurationRequestTypeDef", {"OfferingId": str}
)
_OptionalTargetConfigurationRequestTypeDef = TypedDict(
    "_OptionalTargetConfigurationRequestTypeDef", {"InstanceCount": int}, total=False
)


class TargetConfigurationRequestTypeDef(
    _RequiredTargetConfigurationRequestTypeDef, _OptionalTargetConfigurationRequestTypeDef
):
    pass


TerminateClientVpnConnectionsResultTypeDef = TypedDict(
    "TerminateClientVpnConnectionsResultTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Username": str,
        "ConnectionStatuses": List["TerminateConnectionStatusTypeDef"],
    },
    total=False,
)

TerminateInstancesResultTypeDef = TypedDict(
    "TerminateInstancesResultTypeDef",
    {"TerminatingInstances": List["InstanceStateChangeTypeDef"]},
    total=False,
)

TrafficMirrorPortRangeRequestTypeDef = TypedDict(
    "TrafficMirrorPortRangeRequestTypeDef", {"FromPort": int, "ToPort": int}, total=False
)

TransitGatewayRequestOptionsTypeDef = TypedDict(
    "TransitGatewayRequestOptionsTypeDef",
    {
        "AmazonSideAsn": int,
        "AutoAcceptSharedAttachments": Literal["enable", "disable"],
        "DefaultRouteTableAssociation": Literal["enable", "disable"],
        "DefaultRouteTablePropagation": Literal["enable", "disable"],
        "VpnEcmpSupport": Literal["enable", "disable"],
        "DnsSupport": Literal["enable", "disable"],
        "MulticastSupport": Literal["enable", "disable"],
    },
    total=False,
)

UnassignIpv6AddressesResultTypeDef = TypedDict(
    "UnassignIpv6AddressesResultTypeDef",
    {"NetworkInterfaceId": str, "UnassignedIpv6Addresses": List[str]},
    total=False,
)

UnmonitorInstancesResultTypeDef = TypedDict(
    "UnmonitorInstancesResultTypeDef",
    {"InstanceMonitorings": List["InstanceMonitoringTypeDef"]},
    total=False,
)

UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef", {"Return": bool}, total=False
)

UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef", {"Return": bool}, total=False
)

VpnConnectionOptionsSpecificationTypeDef = TypedDict(
    "VpnConnectionOptionsSpecificationTypeDef",
    {
        "EnableAcceleration": bool,
        "StaticRoutesOnly": bool,
        "TunnelInsideIpVersion": Literal["ipv4", "ipv6"],
        "TunnelOptions": List["VpnTunnelOptionsSpecificationTypeDef"],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

WithdrawByoipCidrResultTypeDef = TypedDict(
    "WithdrawByoipCidrResultTypeDef", {"ByoipCidr": "ByoipCidrTypeDef"}, total=False
)
