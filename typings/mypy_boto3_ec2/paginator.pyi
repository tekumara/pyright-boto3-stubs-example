# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for ec2 service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_ec2 import EC2Client
    from mypy_boto3_ec2.paginator import (
        DescribeByoipCidrsPaginator,
        DescribeCapacityReservationsPaginator,
        DescribeCarrierGatewaysPaginator,
        DescribeClassicLinkInstancesPaginator,
        DescribeClientVpnAuthorizationRulesPaginator,
        DescribeClientVpnConnectionsPaginator,
        DescribeClientVpnEndpointsPaginator,
        DescribeClientVpnRoutesPaginator,
        DescribeClientVpnTargetNetworksPaginator,
        DescribeCoipPoolsPaginator,
        DescribeDhcpOptionsPaginator,
        DescribeEgressOnlyInternetGatewaysPaginator,
        DescribeExportImageTasksPaginator,
        DescribeFastSnapshotRestoresPaginator,
        DescribeFleetsPaginator,
        DescribeFlowLogsPaginator,
        DescribeFpgaImagesPaginator,
        DescribeHostReservationOfferingsPaginator,
        DescribeHostReservationsPaginator,
        DescribeHostsPaginator,
        DescribeIamInstanceProfileAssociationsPaginator,
        DescribeImportImageTasksPaginator,
        DescribeImportSnapshotTasksPaginator,
        DescribeInstanceCreditSpecificationsPaginator,
        DescribeInstanceStatusPaginator,
        DescribeInstanceTypeOfferingsPaginator,
        DescribeInstanceTypesPaginator,
        DescribeInstancesPaginator,
        DescribeInternetGatewaysPaginator,
        DescribeIpv6PoolsPaginator,
        DescribeLaunchTemplateVersionsPaginator,
        DescribeLaunchTemplatesPaginator,
        DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
        DescribeLocalGatewayRouteTableVpcAssociationsPaginator,
        DescribeLocalGatewayRouteTablesPaginator,
        DescribeLocalGatewayVirtualInterfaceGroupsPaginator,
        DescribeLocalGatewayVirtualInterfacesPaginator,
        DescribeLocalGatewaysPaginator,
        DescribeManagedPrefixListsPaginator,
        DescribeMovingAddressesPaginator,
        DescribeNatGatewaysPaginator,
        DescribeNetworkAclsPaginator,
        DescribeNetworkInterfacePermissionsPaginator,
        DescribeNetworkInterfacesPaginator,
        DescribePrefixListsPaginator,
        DescribePrincipalIdFormatPaginator,
        DescribePublicIpv4PoolsPaginator,
        DescribeReservedInstancesModificationsPaginator,
        DescribeReservedInstancesOfferingsPaginator,
        DescribeRouteTablesPaginator,
        DescribeScheduledInstanceAvailabilityPaginator,
        DescribeScheduledInstancesPaginator,
        DescribeSecurityGroupsPaginator,
        DescribeSnapshotsPaginator,
        DescribeSpotFleetInstancesPaginator,
        DescribeSpotFleetRequestsPaginator,
        DescribeSpotInstanceRequestsPaginator,
        DescribeSpotPriceHistoryPaginator,
        DescribeStaleSecurityGroupsPaginator,
        DescribeSubnetsPaginator,
        DescribeTagsPaginator,
        DescribeTrafficMirrorFiltersPaginator,
        DescribeTrafficMirrorSessionsPaginator,
        DescribeTrafficMirrorTargetsPaginator,
        DescribeTransitGatewayAttachmentsPaginator,
        DescribeTransitGatewayMulticastDomainsPaginator,
        DescribeTransitGatewayPeeringAttachmentsPaginator,
        DescribeTransitGatewayRouteTablesPaginator,
        DescribeTransitGatewayVpcAttachmentsPaginator,
        DescribeTransitGatewaysPaginator,
        DescribeVolumeStatusPaginator,
        DescribeVolumesPaginator,
        DescribeVolumesModificationsPaginator,
        DescribeVpcClassicLinkDnsSupportPaginator,
        DescribeVpcEndpointConnectionNotificationsPaginator,
        DescribeVpcEndpointConnectionsPaginator,
        DescribeVpcEndpointServiceConfigurationsPaginator,
        DescribeVpcEndpointServicePermissionsPaginator,
        DescribeVpcEndpointServicesPaginator,
        DescribeVpcEndpointsPaginator,
        DescribeVpcPeeringConnectionsPaginator,
        DescribeVpcsPaginator,
        GetAssociatedIpv6PoolCidrsPaginator,
        GetGroupsForCapacityReservationPaginator,
        GetManagedPrefixListAssociationsPaginator,
        GetManagedPrefixListEntriesPaginator,
        GetTransitGatewayAttachmentPropagationsPaginator,
        GetTransitGatewayMulticastDomainAssociationsPaginator,
        GetTransitGatewayRouteTableAssociationsPaginator,
        GetTransitGatewayRouteTablePropagationsPaginator,
        SearchLocalGatewayRoutesPaginator,
        SearchTransitGatewayMulticastGroupsPaginator,
    )

    client: EC2Client = boto3.client("ec2")

    describe_byoip_cidrs_paginator: DescribeByoipCidrsPaginator = client.get_paginator("describe_byoip_cidrs")
    describe_capacity_reservations_paginator: DescribeCapacityReservationsPaginator = client.get_paginator("describe_capacity_reservations")
    describe_carrier_gateways_paginator: DescribeCarrierGatewaysPaginator = client.get_paginator("describe_carrier_gateways")
    describe_classic_link_instances_paginator: DescribeClassicLinkInstancesPaginator = client.get_paginator("describe_classic_link_instances")
    describe_client_vpn_authorization_rules_paginator: DescribeClientVpnAuthorizationRulesPaginator = client.get_paginator("describe_client_vpn_authorization_rules")
    describe_client_vpn_connections_paginator: DescribeClientVpnConnectionsPaginator = client.get_paginator("describe_client_vpn_connections")
    describe_client_vpn_endpoints_paginator: DescribeClientVpnEndpointsPaginator = client.get_paginator("describe_client_vpn_endpoints")
    describe_client_vpn_routes_paginator: DescribeClientVpnRoutesPaginator = client.get_paginator("describe_client_vpn_routes")
    describe_client_vpn_target_networks_paginator: DescribeClientVpnTargetNetworksPaginator = client.get_paginator("describe_client_vpn_target_networks")
    describe_coip_pools_paginator: DescribeCoipPoolsPaginator = client.get_paginator("describe_coip_pools")
    describe_dhcp_options_paginator: DescribeDhcpOptionsPaginator = client.get_paginator("describe_dhcp_options")
    describe_egress_only_internet_gateways_paginator: DescribeEgressOnlyInternetGatewaysPaginator = client.get_paginator("describe_egress_only_internet_gateways")
    describe_export_image_tasks_paginator: DescribeExportImageTasksPaginator = client.get_paginator("describe_export_image_tasks")
    describe_fast_snapshot_restores_paginator: DescribeFastSnapshotRestoresPaginator = client.get_paginator("describe_fast_snapshot_restores")
    describe_fleets_paginator: DescribeFleetsPaginator = client.get_paginator("describe_fleets")
    describe_flow_logs_paginator: DescribeFlowLogsPaginator = client.get_paginator("describe_flow_logs")
    describe_fpga_images_paginator: DescribeFpgaImagesPaginator = client.get_paginator("describe_fpga_images")
    describe_host_reservation_offerings_paginator: DescribeHostReservationOfferingsPaginator = client.get_paginator("describe_host_reservation_offerings")
    describe_host_reservations_paginator: DescribeHostReservationsPaginator = client.get_paginator("describe_host_reservations")
    describe_hosts_paginator: DescribeHostsPaginator = client.get_paginator("describe_hosts")
    describe_iam_instance_profile_associations_paginator: DescribeIamInstanceProfileAssociationsPaginator = client.get_paginator("describe_iam_instance_profile_associations")
    describe_import_image_tasks_paginator: DescribeImportImageTasksPaginator = client.get_paginator("describe_import_image_tasks")
    describe_import_snapshot_tasks_paginator: DescribeImportSnapshotTasksPaginator = client.get_paginator("describe_import_snapshot_tasks")
    describe_instance_credit_specifications_paginator: DescribeInstanceCreditSpecificationsPaginator = client.get_paginator("describe_instance_credit_specifications")
    describe_instance_status_paginator: DescribeInstanceStatusPaginator = client.get_paginator("describe_instance_status")
    describe_instance_type_offerings_paginator: DescribeInstanceTypeOfferingsPaginator = client.get_paginator("describe_instance_type_offerings")
    describe_instance_types_paginator: DescribeInstanceTypesPaginator = client.get_paginator("describe_instance_types")
    describe_instances_paginator: DescribeInstancesPaginator = client.get_paginator("describe_instances")
    describe_internet_gateways_paginator: DescribeInternetGatewaysPaginator = client.get_paginator("describe_internet_gateways")
    describe_ipv6_pools_paginator: DescribeIpv6PoolsPaginator = client.get_paginator("describe_ipv6_pools")
    describe_launch_template_versions_paginator: DescribeLaunchTemplateVersionsPaginator = client.get_paginator("describe_launch_template_versions")
    describe_launch_templates_paginator: DescribeLaunchTemplatesPaginator = client.get_paginator("describe_launch_templates")
    describe_local_gateway_route_table_virtual_interface_group_associations_paginator: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator = client.get_paginator("describe_local_gateway_route_table_virtual_interface_group_associations")
    describe_local_gateway_route_table_vpc_associations_paginator: DescribeLocalGatewayRouteTableVpcAssociationsPaginator = client.get_paginator("describe_local_gateway_route_table_vpc_associations")
    describe_local_gateway_route_tables_paginator: DescribeLocalGatewayRouteTablesPaginator = client.get_paginator("describe_local_gateway_route_tables")
    describe_local_gateway_virtual_interface_groups_paginator: DescribeLocalGatewayVirtualInterfaceGroupsPaginator = client.get_paginator("describe_local_gateway_virtual_interface_groups")
    describe_local_gateway_virtual_interfaces_paginator: DescribeLocalGatewayVirtualInterfacesPaginator = client.get_paginator("describe_local_gateway_virtual_interfaces")
    describe_local_gateways_paginator: DescribeLocalGatewaysPaginator = client.get_paginator("describe_local_gateways")
    describe_managed_prefix_lists_paginator: DescribeManagedPrefixListsPaginator = client.get_paginator("describe_managed_prefix_lists")
    describe_moving_addresses_paginator: DescribeMovingAddressesPaginator = client.get_paginator("describe_moving_addresses")
    describe_nat_gateways_paginator: DescribeNatGatewaysPaginator = client.get_paginator("describe_nat_gateways")
    describe_network_acls_paginator: DescribeNetworkAclsPaginator = client.get_paginator("describe_network_acls")
    describe_network_interface_permissions_paginator: DescribeNetworkInterfacePermissionsPaginator = client.get_paginator("describe_network_interface_permissions")
    describe_network_interfaces_paginator: DescribeNetworkInterfacesPaginator = client.get_paginator("describe_network_interfaces")
    describe_prefix_lists_paginator: DescribePrefixListsPaginator = client.get_paginator("describe_prefix_lists")
    describe_principal_id_format_paginator: DescribePrincipalIdFormatPaginator = client.get_paginator("describe_principal_id_format")
    describe_public_ipv4_pools_paginator: DescribePublicIpv4PoolsPaginator = client.get_paginator("describe_public_ipv4_pools")
    describe_reserved_instances_modifications_paginator: DescribeReservedInstancesModificationsPaginator = client.get_paginator("describe_reserved_instances_modifications")
    describe_reserved_instances_offerings_paginator: DescribeReservedInstancesOfferingsPaginator = client.get_paginator("describe_reserved_instances_offerings")
    describe_route_tables_paginator: DescribeRouteTablesPaginator = client.get_paginator("describe_route_tables")
    describe_scheduled_instance_availability_paginator: DescribeScheduledInstanceAvailabilityPaginator = client.get_paginator("describe_scheduled_instance_availability")
    describe_scheduled_instances_paginator: DescribeScheduledInstancesPaginator = client.get_paginator("describe_scheduled_instances")
    describe_security_groups_paginator: DescribeSecurityGroupsPaginator = client.get_paginator("describe_security_groups")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_spot_fleet_instances_paginator: DescribeSpotFleetInstancesPaginator = client.get_paginator("describe_spot_fleet_instances")
    describe_spot_fleet_requests_paginator: DescribeSpotFleetRequestsPaginator = client.get_paginator("describe_spot_fleet_requests")
    describe_spot_instance_requests_paginator: DescribeSpotInstanceRequestsPaginator = client.get_paginator("describe_spot_instance_requests")
    describe_spot_price_history_paginator: DescribeSpotPriceHistoryPaginator = client.get_paginator("describe_spot_price_history")
    describe_stale_security_groups_paginator: DescribeStaleSecurityGroupsPaginator = client.get_paginator("describe_stale_security_groups")
    describe_subnets_paginator: DescribeSubnetsPaginator = client.get_paginator("describe_subnets")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    describe_traffic_mirror_filters_paginator: DescribeTrafficMirrorFiltersPaginator = client.get_paginator("describe_traffic_mirror_filters")
    describe_traffic_mirror_sessions_paginator: DescribeTrafficMirrorSessionsPaginator = client.get_paginator("describe_traffic_mirror_sessions")
    describe_traffic_mirror_targets_paginator: DescribeTrafficMirrorTargetsPaginator = client.get_paginator("describe_traffic_mirror_targets")
    describe_transit_gateway_attachments_paginator: DescribeTransitGatewayAttachmentsPaginator = client.get_paginator("describe_transit_gateway_attachments")
    describe_transit_gateway_multicast_domains_paginator: DescribeTransitGatewayMulticastDomainsPaginator = client.get_paginator("describe_transit_gateway_multicast_domains")
    describe_transit_gateway_peering_attachments_paginator: DescribeTransitGatewayPeeringAttachmentsPaginator = client.get_paginator("describe_transit_gateway_peering_attachments")
    describe_transit_gateway_route_tables_paginator: DescribeTransitGatewayRouteTablesPaginator = client.get_paginator("describe_transit_gateway_route_tables")
    describe_transit_gateway_vpc_attachments_paginator: DescribeTransitGatewayVpcAttachmentsPaginator = client.get_paginator("describe_transit_gateway_vpc_attachments")
    describe_transit_gateways_paginator: DescribeTransitGatewaysPaginator = client.get_paginator("describe_transit_gateways")
    describe_volume_status_paginator: DescribeVolumeStatusPaginator = client.get_paginator("describe_volume_status")
    describe_volumes_paginator: DescribeVolumesPaginator = client.get_paginator("describe_volumes")
    describe_volumes_modifications_paginator: DescribeVolumesModificationsPaginator = client.get_paginator("describe_volumes_modifications")
    describe_vpc_classic_link_dns_support_paginator: DescribeVpcClassicLinkDnsSupportPaginator = client.get_paginator("describe_vpc_classic_link_dns_support")
    describe_vpc_endpoint_connection_notifications_paginator: DescribeVpcEndpointConnectionNotificationsPaginator = client.get_paginator("describe_vpc_endpoint_connection_notifications")
    describe_vpc_endpoint_connections_paginator: DescribeVpcEndpointConnectionsPaginator = client.get_paginator("describe_vpc_endpoint_connections")
    describe_vpc_endpoint_service_configurations_paginator: DescribeVpcEndpointServiceConfigurationsPaginator = client.get_paginator("describe_vpc_endpoint_service_configurations")
    describe_vpc_endpoint_service_permissions_paginator: DescribeVpcEndpointServicePermissionsPaginator = client.get_paginator("describe_vpc_endpoint_service_permissions")
    describe_vpc_endpoint_services_paginator: DescribeVpcEndpointServicesPaginator = client.get_paginator("describe_vpc_endpoint_services")
    describe_vpc_endpoints_paginator: DescribeVpcEndpointsPaginator = client.get_paginator("describe_vpc_endpoints")
    describe_vpc_peering_connections_paginator: DescribeVpcPeeringConnectionsPaginator = client.get_paginator("describe_vpc_peering_connections")
    describe_vpcs_paginator: DescribeVpcsPaginator = client.get_paginator("describe_vpcs")
    get_associated_ipv6_pool_cidrs_paginator: GetAssociatedIpv6PoolCidrsPaginator = client.get_paginator("get_associated_ipv6_pool_cidrs")
    get_groups_for_capacity_reservation_paginator: GetGroupsForCapacityReservationPaginator = client.get_paginator("get_groups_for_capacity_reservation")
    get_managed_prefix_list_associations_paginator: GetManagedPrefixListAssociationsPaginator = client.get_paginator("get_managed_prefix_list_associations")
    get_managed_prefix_list_entries_paginator: GetManagedPrefixListEntriesPaginator = client.get_paginator("get_managed_prefix_list_entries")
    get_transit_gateway_attachment_propagations_paginator: GetTransitGatewayAttachmentPropagationsPaginator = client.get_paginator("get_transit_gateway_attachment_propagations")
    get_transit_gateway_multicast_domain_associations_paginator: GetTransitGatewayMulticastDomainAssociationsPaginator = client.get_paginator("get_transit_gateway_multicast_domain_associations")
    get_transit_gateway_route_table_associations_paginator: GetTransitGatewayRouteTableAssociationsPaginator = client.get_paginator("get_transit_gateway_route_table_associations")
    get_transit_gateway_route_table_propagations_paginator: GetTransitGatewayRouteTablePropagationsPaginator = client.get_paginator("get_transit_gateway_route_table_propagations")
    search_local_gateway_routes_paginator: SearchLocalGatewayRoutesPaginator = client.get_paginator("search_local_gateway_routes")
    search_transit_gateway_multicast_groups_paginator: SearchTransitGatewayMulticastGroupsPaginator = client.get_paginator("search_transit_gateway_multicast_groups")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_ec2.type_defs import (
    DescribeByoipCidrsResultTypeDef,
    DescribeCapacityReservationsResultTypeDef,
    DescribeCarrierGatewaysResultTypeDef,
    DescribeClassicLinkInstancesResultTypeDef,
    DescribeClientVpnAuthorizationRulesResultTypeDef,
    DescribeClientVpnConnectionsResultTypeDef,
    DescribeClientVpnEndpointsResultTypeDef,
    DescribeClientVpnRoutesResultTypeDef,
    DescribeClientVpnTargetNetworksResultTypeDef,
    DescribeCoipPoolsResultTypeDef,
    DescribeDhcpOptionsResultTypeDef,
    DescribeEgressOnlyInternetGatewaysResultTypeDef,
    DescribeExportImageTasksResultTypeDef,
    DescribeFastSnapshotRestoresResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeFlowLogsResultTypeDef,
    DescribeFpgaImagesResultTypeDef,
    DescribeHostReservationOfferingsResultTypeDef,
    DescribeHostReservationsResultTypeDef,
    DescribeHostsResultTypeDef,
    DescribeIamInstanceProfileAssociationsResultTypeDef,
    DescribeImportImageTasksResultTypeDef,
    DescribeImportSnapshotTasksResultTypeDef,
    DescribeInstanceCreditSpecificationsResultTypeDef,
    DescribeInstancesResultTypeDef,
    DescribeInstanceStatusResultTypeDef,
    DescribeInstanceTypeOfferingsResultTypeDef,
    DescribeInstanceTypesResultTypeDef,
    DescribeInternetGatewaysResultTypeDef,
    DescribeIpv6PoolsResultTypeDef,
    DescribeLaunchTemplatesResultTypeDef,
    DescribeLaunchTemplateVersionsResultTypeDef,
    DescribeLocalGatewayRouteTablesResultTypeDef,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef,
    DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef,
    DescribeLocalGatewaysResultTypeDef,
    DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef,
    DescribeLocalGatewayVirtualInterfacesResultTypeDef,
    DescribeManagedPrefixListsResultTypeDef,
    DescribeMovingAddressesResultTypeDef,
    DescribeNatGatewaysResultTypeDef,
    DescribeNetworkAclsResultTypeDef,
    DescribeNetworkInterfacePermissionsResultTypeDef,
    DescribeNetworkInterfacesResultTypeDef,
    DescribePrefixListsResultTypeDef,
    DescribePrincipalIdFormatResultTypeDef,
    DescribePublicIpv4PoolsResultTypeDef,
    DescribeReservedInstancesModificationsResultTypeDef,
    DescribeReservedInstancesOfferingsResultTypeDef,
    DescribeRouteTablesResultTypeDef,
    DescribeScheduledInstanceAvailabilityResultTypeDef,
    DescribeScheduledInstancesResultTypeDef,
    DescribeSecurityGroupsResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeSpotFleetInstancesResponseTypeDef,
    DescribeSpotFleetRequestsResponseTypeDef,
    DescribeSpotInstanceRequestsResultTypeDef,
    DescribeSpotPriceHistoryResultTypeDef,
    DescribeStaleSecurityGroupsResultTypeDef,
    DescribeSubnetsResultTypeDef,
    DescribeTagsResultTypeDef,
    DescribeTrafficMirrorFiltersResultTypeDef,
    DescribeTrafficMirrorSessionsResultTypeDef,
    DescribeTrafficMirrorTargetsResultTypeDef,
    DescribeTransitGatewayAttachmentsResultTypeDef,
    DescribeTransitGatewayMulticastDomainsResultTypeDef,
    DescribeTransitGatewayPeeringAttachmentsResultTypeDef,
    DescribeTransitGatewayRouteTablesResultTypeDef,
    DescribeTransitGatewaysResultTypeDef,
    DescribeTransitGatewayVpcAttachmentsResultTypeDef,
    DescribeVolumesModificationsResultTypeDef,
    DescribeVolumesResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcClassicLinkDnsSupportResultTypeDef,
    DescribeVpcEndpointConnectionNotificationsResultTypeDef,
    DescribeVpcEndpointConnectionsResultTypeDef,
    DescribeVpcEndpointServiceConfigurationsResultTypeDef,
    DescribeVpcEndpointServicePermissionsResultTypeDef,
    DescribeVpcEndpointServicesResultTypeDef,
    DescribeVpcEndpointsResultTypeDef,
    DescribeVpcPeeringConnectionsResultTypeDef,
    DescribeVpcsResultTypeDef,
    FilterTypeDef,
    GetAssociatedIpv6PoolCidrsResultTypeDef,
    GetGroupsForCapacityReservationResultTypeDef,
    GetManagedPrefixListAssociationsResultTypeDef,
    GetManagedPrefixListEntriesResultTypeDef,
    GetTransitGatewayAttachmentPropagationsResultTypeDef,
    GetTransitGatewayMulticastDomainAssociationsResultTypeDef,
    GetTransitGatewayRouteTableAssociationsResultTypeDef,
    GetTransitGatewayRouteTablePropagationsResultTypeDef,
    PaginatorConfigTypeDef,
    ScheduledInstanceRecurrenceRequestTypeDef,
    SearchLocalGatewayRoutesResultTypeDef,
    SearchTransitGatewayMulticastGroupsResultTypeDef,
    SlotDateTimeRangeRequestTypeDef,
    SlotStartTimeRangeRequestTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeByoipCidrsPaginator",
    "DescribeCapacityReservationsPaginator",
    "DescribeCarrierGatewaysPaginator",
    "DescribeClassicLinkInstancesPaginator",
    "DescribeClientVpnAuthorizationRulesPaginator",
    "DescribeClientVpnConnectionsPaginator",
    "DescribeClientVpnEndpointsPaginator",
    "DescribeClientVpnRoutesPaginator",
    "DescribeClientVpnTargetNetworksPaginator",
    "DescribeCoipPoolsPaginator",
    "DescribeDhcpOptionsPaginator",
    "DescribeEgressOnlyInternetGatewaysPaginator",
    "DescribeExportImageTasksPaginator",
    "DescribeFastSnapshotRestoresPaginator",
    "DescribeFleetsPaginator",
    "DescribeFlowLogsPaginator",
    "DescribeFpgaImagesPaginator",
    "DescribeHostReservationOfferingsPaginator",
    "DescribeHostReservationsPaginator",
    "DescribeHostsPaginator",
    "DescribeIamInstanceProfileAssociationsPaginator",
    "DescribeImportImageTasksPaginator",
    "DescribeImportSnapshotTasksPaginator",
    "DescribeInstanceCreditSpecificationsPaginator",
    "DescribeInstanceStatusPaginator",
    "DescribeInstanceTypeOfferingsPaginator",
    "DescribeInstanceTypesPaginator",
    "DescribeInstancesPaginator",
    "DescribeInternetGatewaysPaginator",
    "DescribeIpv6PoolsPaginator",
    "DescribeLaunchTemplateVersionsPaginator",
    "DescribeLaunchTemplatesPaginator",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator",
    "DescribeLocalGatewayRouteTableVpcAssociationsPaginator",
    "DescribeLocalGatewayRouteTablesPaginator",
    "DescribeLocalGatewayVirtualInterfaceGroupsPaginator",
    "DescribeLocalGatewayVirtualInterfacesPaginator",
    "DescribeLocalGatewaysPaginator",
    "DescribeManagedPrefixListsPaginator",
    "DescribeMovingAddressesPaginator",
    "DescribeNatGatewaysPaginator",
    "DescribeNetworkAclsPaginator",
    "DescribeNetworkInterfacePermissionsPaginator",
    "DescribeNetworkInterfacesPaginator",
    "DescribePrefixListsPaginator",
    "DescribePrincipalIdFormatPaginator",
    "DescribePublicIpv4PoolsPaginator",
    "DescribeReservedInstancesModificationsPaginator",
    "DescribeReservedInstancesOfferingsPaginator",
    "DescribeRouteTablesPaginator",
    "DescribeScheduledInstanceAvailabilityPaginator",
    "DescribeScheduledInstancesPaginator",
    "DescribeSecurityGroupsPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeSpotFleetInstancesPaginator",
    "DescribeSpotFleetRequestsPaginator",
    "DescribeSpotInstanceRequestsPaginator",
    "DescribeSpotPriceHistoryPaginator",
    "DescribeStaleSecurityGroupsPaginator",
    "DescribeSubnetsPaginator",
    "DescribeTagsPaginator",
    "DescribeTrafficMirrorFiltersPaginator",
    "DescribeTrafficMirrorSessionsPaginator",
    "DescribeTrafficMirrorTargetsPaginator",
    "DescribeTransitGatewayAttachmentsPaginator",
    "DescribeTransitGatewayMulticastDomainsPaginator",
    "DescribeTransitGatewayPeeringAttachmentsPaginator",
    "DescribeTransitGatewayRouteTablesPaginator",
    "DescribeTransitGatewayVpcAttachmentsPaginator",
    "DescribeTransitGatewaysPaginator",
    "DescribeVolumeStatusPaginator",
    "DescribeVolumesPaginator",
    "DescribeVolumesModificationsPaginator",
    "DescribeVpcClassicLinkDnsSupportPaginator",
    "DescribeVpcEndpointConnectionNotificationsPaginator",
    "DescribeVpcEndpointConnectionsPaginator",
    "DescribeVpcEndpointServiceConfigurationsPaginator",
    "DescribeVpcEndpointServicePermissionsPaginator",
    "DescribeVpcEndpointServicesPaginator",
    "DescribeVpcEndpointsPaginator",
    "DescribeVpcPeeringConnectionsPaginator",
    "DescribeVpcsPaginator",
    "GetAssociatedIpv6PoolCidrsPaginator",
    "GetGroupsForCapacityReservationPaginator",
    "GetManagedPrefixListAssociationsPaginator",
    "GetManagedPrefixListEntriesPaginator",
    "GetTransitGatewayAttachmentPropagationsPaginator",
    "GetTransitGatewayMulticastDomainAssociationsPaginator",
    "GetTransitGatewayRouteTableAssociationsPaginator",
    "GetTransitGatewayRouteTablePropagationsPaginator",
    "SearchLocalGatewayRoutesPaginator",
    "SearchTransitGatewayMulticastGroupsPaginator",
)


class DescribeByoipCidrsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeByoipCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs)
    """

    def paginate(
        self, DryRun: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeByoipCidrsResultTypeDef]:
        """
        [DescribeByoipCidrs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs.paginate)
        """


class DescribeCapacityReservationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCapacityReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations)
    """

    def paginate(
        self,
        CapacityReservationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeCapacityReservationsResultTypeDef]:
        """
        [DescribeCapacityReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations.paginate)
        """


class DescribeCarrierGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCarrierGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeCarrierGateways)
    """

    def paginate(
        self,
        CarrierGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeCarrierGatewaysResultTypeDef]:
        """
        [DescribeCarrierGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeCarrierGateways.paginate)
        """


class DescribeClassicLinkInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClassicLinkInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InstanceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeClassicLinkInstancesResultTypeDef]:
        """
        [DescribeClassicLinkInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances.paginate)
        """


class DescribeClientVpnAuthorizationRulesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClientVpnAuthorizationRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules)
    """

    def paginate(
        self,
        ClientVpnEndpointId: str,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeClientVpnAuthorizationRulesResultTypeDef]:
        """
        [DescribeClientVpnAuthorizationRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules.paginate)
        """


class DescribeClientVpnConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClientVpnConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections)
    """

    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeClientVpnConnectionsResultTypeDef]:
        """
        [DescribeClientVpnConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections.paginate)
        """


class DescribeClientVpnEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClientVpnEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints)
    """

    def paginate(
        self,
        ClientVpnEndpointIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeClientVpnEndpointsResultTypeDef]:
        """
        [DescribeClientVpnEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints.paginate)
        """


class DescribeClientVpnRoutesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClientVpnRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes)
    """

    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeClientVpnRoutesResultTypeDef]:
        """
        [DescribeClientVpnRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes.paginate)
        """


class DescribeClientVpnTargetNetworksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClientVpnTargetNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks)
    """

    def paginate(
        self,
        ClientVpnEndpointId: str,
        AssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeClientVpnTargetNetworksResultTypeDef]:
        """
        [DescribeClientVpnTargetNetworks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks.paginate)
        """


class DescribeCoipPoolsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCoipPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeCoipPools)
    """

    def paginate(
        self,
        PoolIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeCoipPoolsResultTypeDef]:
        """
        [DescribeCoipPools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeCoipPools.paginate)
        """


class DescribeDhcpOptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDhcpOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions)
    """

    def paginate(
        self,
        DhcpOptionsIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeDhcpOptionsResultTypeDef]:
        """
        [DescribeDhcpOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions.paginate)
        """


class DescribeEgressOnlyInternetGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEgressOnlyInternetGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways)
    """

    def paginate(
        self,
        DryRun: bool = None,
        EgressOnlyInternetGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeEgressOnlyInternetGatewaysResultTypeDef]:
        """
        [DescribeEgressOnlyInternetGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways.paginate)
        """


class DescribeExportImageTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeExportImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ExportImageTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeExportImageTasksResultTypeDef]:
        """
        [DescribeExportImageTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks.paginate)
        """


class DescribeFastSnapshotRestoresPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFastSnapshotRestores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeFastSnapshotRestoresResultTypeDef]:
        """
        [DescribeFastSnapshotRestores.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores.paginate)
        """


class DescribeFleetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeFleets)
    """

    def paginate(
        self,
        DryRun: bool = None,
        FleetIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeFleetsResultTypeDef]:
        """
        [DescribeFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeFleets.paginate)
        """


class DescribeFlowLogsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFlowLogs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        FlowLogIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeFlowLogsResultTypeDef]:
        """
        [DescribeFlowLogs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs.paginate)
        """


class DescribeFpgaImagesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFpgaImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages)
    """

    def paginate(
        self,
        DryRun: bool = None,
        FpgaImageIds: List[str] = None,
        Owners: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeFpgaImagesResultTypeDef]:
        """
        [DescribeFpgaImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages.paginate)
        """


class DescribeHostReservationOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeHostReservationOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxDuration: int = None,
        MinDuration: int = None,
        OfferingId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeHostReservationOfferingsResultTypeDef]:
        """
        [DescribeHostReservationOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings.paginate)
        """


class DescribeHostReservationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeHostReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        HostReservationIdSet: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeHostReservationsResultTypeDef]:
        """
        [DescribeHostReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations.paginate)
        """


class DescribeHostsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeHosts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeHosts)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        HostIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeHostsResultTypeDef]:
        """
        [DescribeHosts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeHosts.paginate)
        """


class DescribeIamInstanceProfileAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeIamInstanceProfileAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations)
    """

    def paginate(
        self,
        AssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeIamInstanceProfileAssociationsResultTypeDef]:
        """
        [DescribeIamInstanceProfileAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations.paginate)
        """


class DescribeImportImageTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImportImageTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ImportTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeImportImageTasksResultTypeDef]:
        """
        [DescribeImportImageTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks.paginate)
        """


class DescribeImportSnapshotTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeImportSnapshotTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ImportTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeImportSnapshotTasksResultTypeDef]:
        """
        [DescribeImportSnapshotTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks.paginate)
        """


class DescribeInstanceCreditSpecificationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstanceCreditSpecifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeInstanceCreditSpecificationsResultTypeDef]:
        """
        [DescribeInstanceCreditSpecifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications.paginate)
        """


class DescribeInstanceStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstanceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeInstanceStatusResultTypeDef]:
        """
        [DescribeInstanceStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus.paginate)
        """


class DescribeInstanceTypeOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstanceTypeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypeOfferings)
    """

    def paginate(
        self,
        DryRun: bool = None,
        LocationType: Literal["region", "availability-zone", "availability-zone-id"] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeInstanceTypeOfferingsResultTypeDef]:
        """
        [DescribeInstanceTypeOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypeOfferings.paginate)
        """


class DescribeInstanceTypesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstanceTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypes)
    """

    def paginate(
        self,
        DryRun: bool = None,
        InstanceTypes: List[
            Literal[
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
            ]
        ] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeInstanceTypesResultTypeDef]:
        """
        [DescribeInstanceTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypes.paginate)
        """


class DescribeInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInstances)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeInstancesResultTypeDef]:
        """
        [DescribeInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInstances.paginate)
        """


class DescribeInternetGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInternetGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeInternetGatewaysResultTypeDef]:
        """
        [DescribeInternetGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways.paginate)
        """


class DescribeIpv6PoolsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeIpv6Pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeIpv6Pools)
    """

    def paginate(
        self,
        PoolIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeIpv6PoolsResultTypeDef]:
        """
        [DescribeIpv6Pools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeIpv6Pools.paginate)
        """


class DescribeLaunchTemplateVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLaunchTemplateVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions)
    """

    def paginate(
        self,
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        Versions: List[str] = None,
        MinVersion: str = None,
        MaxVersion: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeLaunchTemplateVersionsResultTypeDef]:
        """
        [DescribeLaunchTemplateVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions.paginate)
        """


class DescribeLaunchTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLaunchTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates)
    """

    def paginate(
        self,
        DryRun: bool = None,
        LaunchTemplateIds: List[str] = None,
        LaunchTemplateNames: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeLaunchTemplatesResultTypeDef]:
        """
        [DescribeLaunchTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates.paginate)
        """


class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations)
    """

    def paginate(
        self,
        LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef]:
        """
        [DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations.paginate)
        """


class DescribeLocalGatewayRouteTableVpcAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLocalGatewayRouteTableVpcAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations)
    """

    def paginate(
        self,
        LocalGatewayRouteTableVpcAssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef]:
        """
        [DescribeLocalGatewayRouteTableVpcAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations.paginate)
        """


class DescribeLocalGatewayRouteTablesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLocalGatewayRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTables)
    """

    def paginate(
        self,
        LocalGatewayRouteTableIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeLocalGatewayRouteTablesResultTypeDef]:
        """
        [DescribeLocalGatewayRouteTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTables.paginate)
        """


class DescribeLocalGatewayVirtualInterfaceGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLocalGatewayVirtualInterfaceGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups)
    """

    def paginate(
        self,
        LocalGatewayVirtualInterfaceGroupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef]:
        """
        [DescribeLocalGatewayVirtualInterfaceGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups.paginate)
        """


class DescribeLocalGatewayVirtualInterfacesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLocalGatewayVirtualInterfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaces)
    """

    def paginate(
        self,
        LocalGatewayVirtualInterfaceIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeLocalGatewayVirtualInterfacesResultTypeDef]:
        """
        [DescribeLocalGatewayVirtualInterfaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaces.paginate)
        """


class DescribeLocalGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLocalGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGateways)
    """

    def paginate(
        self,
        LocalGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeLocalGatewaysResultTypeDef]:
        """
        [DescribeLocalGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeLocalGateways.paginate)
        """


class DescribeManagedPrefixListsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeManagedPrefixLists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeManagedPrefixLists)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PrefixListIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeManagedPrefixListsResultTypeDef]:
        """
        [DescribeManagedPrefixLists.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeManagedPrefixLists.paginate)
        """


class DescribeMovingAddressesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMovingAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PublicIps: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMovingAddressesResultTypeDef]:
        """
        [DescribeMovingAddresses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses.paginate)
        """


class DescribeNatGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNatGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        NatGatewayIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeNatGatewaysResultTypeDef]:
        """
        [DescribeNatGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways.paginate)
        """


class DescribeNetworkAclsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNetworkAcls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeNetworkAclsResultTypeDef]:
        """
        [DescribeNetworkAcls.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls.paginate)
        """


class DescribeNetworkInterfacePermissionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNetworkInterfacePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions)
    """

    def paginate(
        self,
        NetworkInterfacePermissionIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeNetworkInterfacePermissionsResultTypeDef]:
        """
        [DescribeNetworkInterfacePermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions.paginate)
        """


class DescribeNetworkInterfacesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNetworkInterfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeNetworkInterfacesResultTypeDef]:
        """
        [DescribeNetworkInterfaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces.paginate)
        """


class DescribePrefixListsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePrefixLists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PrefixListIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribePrefixListsResultTypeDef]:
        """
        [DescribePrefixLists.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists.paginate)
        """


class DescribePrincipalIdFormatPaginator(Boto3Paginator):
    """
    [Paginator.DescribePrincipalIdFormat documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Resources: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribePrincipalIdFormatResultTypeDef]:
        """
        [DescribePrincipalIdFormat.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat.paginate)
        """


class DescribePublicIpv4PoolsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePublicIpv4Pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools)
    """

    def paginate(
        self,
        PoolIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribePublicIpv4PoolsResultTypeDef]:
        """
        [DescribePublicIpv4Pools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools.paginate)
        """


class DescribeReservedInstancesModificationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedInstancesModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        ReservedInstancesModificationIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeReservedInstancesModificationsResultTypeDef]:
        """
        [DescribeReservedInstancesModifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications.paginate)
        """


class DescribeReservedInstancesOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedInstancesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings)
    """

    def paginate(
        self,
        AvailabilityZone: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeMarketplace: bool = None,
        InstanceType: Literal[
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
        ] = None,
        MaxDuration: int = None,
        MaxInstanceCount: int = None,
        MinDuration: int = None,
        OfferingClass: Literal["standard", "convertible"] = None,
        ProductDescription: Literal[
            "Linux/UNIX", "Linux/UNIX (Amazon VPC)", "Windows", "Windows (Amazon VPC)"
        ] = None,
        ReservedInstancesOfferingIds: List[str] = None,
        DryRun: bool = None,
        InstanceTenancy: Literal["default", "dedicated", "host"] = None,
        OfferingType: Literal[
            "Heavy Utilization",
            "Medium Utilization",
            "Light Utilization",
            "No Upfront",
            "Partial Upfront",
            "All Upfront",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeReservedInstancesOfferingsResultTypeDef]:
        """
        [DescribeReservedInstancesOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings.paginate)
        """


class DescribeRouteTablesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeRouteTablesResultTypeDef]:
        """
        [DescribeRouteTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables.paginate)
        """


class DescribeScheduledInstanceAvailabilityPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScheduledInstanceAvailability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability)
    """

    def paginate(
        self,
        FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef,
        Recurrence: ScheduledInstanceRecurrenceRequestTypeDef,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxSlotDurationInHours: int = None,
        MinSlotDurationInHours: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeScheduledInstanceAvailabilityResultTypeDef]:
        """
        [DescribeScheduledInstanceAvailability.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability.paginate)
        """


class DescribeScheduledInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScheduledInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ScheduledInstanceIds: List[str] = None,
        SlotStartTimeRange: SlotStartTimeRangeRequestTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeScheduledInstancesResultTypeDef]:
        """
        [DescribeScheduledInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances.paginate)
        """


class DescribeSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSecurityGroupsResultTypeDef]:
        """
        [DescribeSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups.paginate)
        """


class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSnapshotsResultTypeDef]:
        """
        [DescribeSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots.paginate)
        """


class DescribeSpotFleetInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSpotFleetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances)
    """

    def paginate(
        self,
        SpotFleetRequestId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSpotFleetInstancesResponseTypeDef]:
        """
        [DescribeSpotFleetInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances.paginate)
        """


class DescribeSpotFleetRequestsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSpotFleetRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests)
    """

    def paginate(
        self,
        DryRun: bool = None,
        SpotFleetRequestIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSpotFleetRequestsResponseTypeDef]:
        """
        [DescribeSpotFleetRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests.paginate)
        """


class DescribeSpotInstanceRequestsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSpotInstanceRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSpotInstanceRequestsResultTypeDef]:
        """
        [DescribeSpotInstanceRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests.paginate)
        """


class DescribeSpotPriceHistoryPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSpotPriceHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        AvailabilityZone: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        InstanceTypes: List[
            Literal[
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
            ]
        ] = None,
        ProductDescriptions: List[str] = None,
        StartTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSpotPriceHistoryResultTypeDef]:
        """
        [DescribeSpotPriceHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory.paginate)
        """


class DescribeStaleSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeStaleSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups)
    """

    def paginate(
        self, VpcId: str, DryRun: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStaleSecurityGroupsResultTypeDef]:
        """
        [DescribeStaleSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups.paginate)
        """


class DescribeSubnetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSubnets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSubnets)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSubnetsResultTypeDef]:
        """
        [DescribeSubnets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeSubnets.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTags)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTagsResultTypeDef]:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTags.paginate)
        """


class DescribeTrafficMirrorFiltersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTrafficMirrorFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters)
    """

    def paginate(
        self,
        TrafficMirrorFilterIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTrafficMirrorFiltersResultTypeDef]:
        """
        [DescribeTrafficMirrorFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters.paginate)
        """


class DescribeTrafficMirrorSessionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTrafficMirrorSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions)
    """

    def paginate(
        self,
        TrafficMirrorSessionIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTrafficMirrorSessionsResultTypeDef]:
        """
        [DescribeTrafficMirrorSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions.paginate)
        """


class DescribeTrafficMirrorTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTrafficMirrorTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets)
    """

    def paginate(
        self,
        TrafficMirrorTargetIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTrafficMirrorTargetsResultTypeDef]:
        """
        [DescribeTrafficMirrorTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets.paginate)
        """


class DescribeTransitGatewayAttachmentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTransitGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments)
    """

    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTransitGatewayAttachmentsResultTypeDef]:
        """
        [DescribeTransitGatewayAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments.paginate)
        """


class DescribeTransitGatewayMulticastDomainsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTransitGatewayMulticastDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayMulticastDomains)
    """

    def paginate(
        self,
        TransitGatewayMulticastDomainIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTransitGatewayMulticastDomainsResultTypeDef]:
        """
        [DescribeTransitGatewayMulticastDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayMulticastDomains.paginate)
        """


class DescribeTransitGatewayPeeringAttachmentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTransitGatewayPeeringAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayPeeringAttachments)
    """

    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTransitGatewayPeeringAttachmentsResultTypeDef]:
        """
        [DescribeTransitGatewayPeeringAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayPeeringAttachments.paginate)
        """


class DescribeTransitGatewayRouteTablesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTransitGatewayRouteTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables)
    """

    def paginate(
        self,
        TransitGatewayRouteTableIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTransitGatewayRouteTablesResultTypeDef]:
        """
        [DescribeTransitGatewayRouteTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables.paginate)
        """


class DescribeTransitGatewayVpcAttachmentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTransitGatewayVpcAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments)
    """

    def paginate(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTransitGatewayVpcAttachmentsResultTypeDef]:
        """
        [DescribeTransitGatewayVpcAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments.paginate)
        """


class DescribeTransitGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTransitGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways)
    """

    def paginate(
        self,
        TransitGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTransitGatewaysResultTypeDef]:
        """
        [DescribeTransitGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways.paginate)
        """


class DescribeVolumeStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVolumeStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVolumeStatusResultTypeDef]:
        """
        [DescribeVolumeStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus.paginate)
        """


class DescribeVolumesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVolumes)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVolumesResultTypeDef]:
        """
        [DescribeVolumes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVolumes.paginate)
        """


class DescribeVolumesModificationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVolumesModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications)
    """

    def paginate(
        self,
        DryRun: bool = None,
        VolumeIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVolumesModificationsResultTypeDef]:
        """
        [DescribeVolumesModifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications.paginate)
        """


class DescribeVpcClassicLinkDnsSupportPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcClassicLinkDnsSupport documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport)
    """

    def paginate(
        self, VpcIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcClassicLinkDnsSupportResultTypeDef]:
        """
        [DescribeVpcClassicLinkDnsSupport.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport.paginate)
        """


class DescribeVpcEndpointConnectionNotificationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpointConnectionNotifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications)
    """

    def paginate(
        self,
        DryRun: bool = None,
        ConnectionNotificationId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVpcEndpointConnectionNotificationsResultTypeDef]:
        """
        [DescribeVpcEndpointConnectionNotifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications.paginate)
        """


class DescribeVpcEndpointConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpointConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections)
    """

    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVpcEndpointConnectionsResultTypeDef]:
        """
        [DescribeVpcEndpointConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections.paginate)
        """


class DescribeVpcEndpointServiceConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpointServiceConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations)
    """

    def paginate(
        self,
        DryRun: bool = None,
        ServiceIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVpcEndpointServiceConfigurationsResultTypeDef]:
        """
        [DescribeVpcEndpointServiceConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations.paginate)
        """


class DescribeVpcEndpointServicePermissionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpointServicePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions)
    """

    def paginate(
        self,
        ServiceId: str,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVpcEndpointServicePermissionsResultTypeDef]:
        """
        [DescribeVpcEndpointServicePermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions.paginate)
        """


class DescribeVpcEndpointServicesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpointServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices)
    """

    def paginate(
        self,
        DryRun: bool = None,
        ServiceNames: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVpcEndpointServicesResultTypeDef]:
        """
        [DescribeVpcEndpointServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices.paginate)
        """


class DescribeVpcEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints)
    """

    def paginate(
        self,
        DryRun: bool = None,
        VpcEndpointIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVpcEndpointsResultTypeDef]:
        """
        [DescribeVpcEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints.paginate)
        """


class DescribeVpcPeeringConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcPeeringConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVpcPeeringConnectionsResultTypeDef]:
        """
        [DescribeVpcPeeringConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections.paginate)
        """


class DescribeVpcsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVpcs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcs)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVpcsResultTypeDef]:
        """
        [DescribeVpcs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.DescribeVpcs.paginate)
        """


class GetAssociatedIpv6PoolCidrsPaginator(Boto3Paginator):
    """
    [Paginator.GetAssociatedIpv6PoolCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetAssociatedIpv6PoolCidrs)
    """

    def paginate(
        self, PoolId: str, DryRun: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAssociatedIpv6PoolCidrsResultTypeDef]:
        """
        [GetAssociatedIpv6PoolCidrs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetAssociatedIpv6PoolCidrs.paginate)
        """


class GetGroupsForCapacityReservationPaginator(Boto3Paginator):
    """
    [Paginator.GetGroupsForCapacityReservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetGroupsForCapacityReservation)
    """

    def paginate(
        self,
        CapacityReservationId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetGroupsForCapacityReservationResultTypeDef]:
        """
        [GetGroupsForCapacityReservation.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetGroupsForCapacityReservation.paginate)
        """


class GetManagedPrefixListAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetManagedPrefixListAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListAssociations)
    """

    def paginate(
        self,
        PrefixListId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetManagedPrefixListAssociationsResultTypeDef]:
        """
        [GetManagedPrefixListAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListAssociations.paginate)
        """


class GetManagedPrefixListEntriesPaginator(Boto3Paginator):
    """
    [Paginator.GetManagedPrefixListEntries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListEntries)
    """

    def paginate(
        self,
        PrefixListId: str,
        DryRun: bool = None,
        TargetVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetManagedPrefixListEntriesResultTypeDef]:
        """
        [GetManagedPrefixListEntries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListEntries.paginate)
        """


class GetTransitGatewayAttachmentPropagationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayAttachmentPropagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations)
    """

    def paginate(
        self,
        TransitGatewayAttachmentId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetTransitGatewayAttachmentPropagationsResultTypeDef]:
        """
        [GetTransitGatewayAttachmentPropagations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations.paginate)
        """


class GetTransitGatewayMulticastDomainAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayMulticastDomainAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayMulticastDomainAssociations)
    """

    def paginate(
        self,
        TransitGatewayMulticastDomainId: str = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetTransitGatewayMulticastDomainAssociationsResultTypeDef]:
        """
        [GetTransitGatewayMulticastDomainAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayMulticastDomainAssociations.paginate)
        """


class GetTransitGatewayRouteTableAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayRouteTableAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations)
    """

    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetTransitGatewayRouteTableAssociationsResultTypeDef]:
        """
        [GetTransitGatewayRouteTableAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations.paginate)
        """


class GetTransitGatewayRouteTablePropagationsPaginator(Boto3Paginator):
    """
    [Paginator.GetTransitGatewayRouteTablePropagations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations)
    """

    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetTransitGatewayRouteTablePropagationsResultTypeDef]:
        """
        [GetTransitGatewayRouteTablePropagations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations.paginate)
        """


class SearchLocalGatewayRoutesPaginator(Boto3Paginator):
    """
    [Paginator.SearchLocalGatewayRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.SearchLocalGatewayRoutes)
    """

    def paginate(
        self,
        LocalGatewayRouteTableId: str,
        Filters: List[FilterTypeDef],
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchLocalGatewayRoutesResultTypeDef]:
        """
        [SearchLocalGatewayRoutes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.SearchLocalGatewayRoutes.paginate)
        """


class SearchTransitGatewayMulticastGroupsPaginator(Boto3Paginator):
    """
    [Paginator.SearchTransitGatewayMulticastGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.SearchTransitGatewayMulticastGroups)
    """

    def paginate(
        self,
        TransitGatewayMulticastDomainId: str = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchTransitGatewayMulticastGroupsResultTypeDef]:
        """
        [SearchTransitGatewayMulticastGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2.html#EC2.Paginator.SearchTransitGatewayMulticastGroups.paginate)
        """
