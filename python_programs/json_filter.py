import json
import pprint

data = json.loads('''
{
  "results": [
    {
      "subnets": [
        {
          "ip_addresses": [
            "100.64.16.0"
          ],
          "prefix_length": 31
        },
        {
          "ip_addresses": [
            "fce5:cec3:5d9b:9800::1"
          ],
          "prefix_length": 64
        },
        {
          "ip_addresses": [
            "fe80::050:56ff:fe56:4452"
          ],
          "prefix_length": 64
        }
      ],
      "linked_logical_router_port_id": "6cdace33-8d9b-4f4f-bc11-bc840d80a48c",
      "mac_address": "02:50:56:56:44:52",
      "resource_type": "LogicalRouterLinkPortOnTIER0",
      "id": "14c88cf1-0304-47a8-a380-3308ddc8df06",
      "display_name": "Tier0Gateway1-Tier1Gateway1-t0_lrp",
      "description": "LogicalRouterLinkPortOnTIER0 on provider logical router Tier0Gateway1-t0 to connect to network logical router Tier1Gateway1-t1",
      "logical_router_id": "a6c54889-45e0-4855-97e0-203fae92e58d",
      "_create_user": "nsx_policy",
      "_create_time": 1586762045733,
      "_last_modified_user": "nsx_policy",
      "_last_modified_time": 1586762045733,
      "_system_owned": false,
      "_protection": "REQUIRE_OVERRIDE",
      "_revision": 0
    },
    {
      "subnets": [
        {
          "ip_addresses": [
            "100.64.16.1"
          ],
          "prefix_length": 31
        },
        {
          "ip_addresses": [
            "fce5:cec3:5d9b:9800::2"
          ],
          "prefix_length": 64
        },
        {
          "ip_addresses": [
            "fe80::050:56ff:fe56:4455"
          ],
          "prefix_length": 64
        }
      ],
      "edge_cluster_member_index": [
        1,
        0
      ],
      "linked_logical_router_port_id": {
        "target_id": "14c88cf1-0304-47a8-a380-3308ddc8df06",
        "target_display_name": "Tier0Gateway1-Tier1Gateway1-t0_lrp",
        "target_type": "LogicalRouterLinkPortOnTIER0",
        "is_valid": true
      },
      "mac_address": "02:50:56:56:44:55",
      "resource_type": "LogicalRouterLinkPortOnTIER1",
      "id": "6cdace33-8d9b-4f4f-bc11-bc840d80a48c",
      "display_name": "Tier0Gateway1-Tier1Gateway1-t1_lrp",
      "description": "LogicalRouterLinkPortOnTIER1 on network logical router Tier0Gateway1-t0 to connect to provider logical router Tier1Gateway1-t1",
      "logical_router_id": "78941d1b-3147-430e-8e27-3f6f09dc0bd3",
      "_create_user": "nsx_policy",
      "_create_time": 1586762046762,
      "_last_modified_user": "nsx_policy",
      "_last_modified_time": 1586762046762,
      "_system_owned": false,
      "_protection": "REQUIRE_OVERRIDE",
      "_revision": 0
    },
    {
      "subnets": [
        {
          "ip_addresses": [
            "192.168.50.1"
          ],
          "prefix_length": 24
        }
      ],
      "edge_cluster_member_index": [
        1
      ],
      "linked_logical_switch_port_id": {
        "target_id": "316de6ff-1acb-4bc2-9664-3fb444e9fd0b",
        "target_display_name": "Tier0Gateway1-Tier0Interface1-ulp",
        "target_type": "LogicalPort",
        "is_valid": true
      },
      "urpf_mode": "STRICT",
      "mac_address": "00:0c:29:e4:55:05",
      "mode": "UNTAGGED",
      "resource_type": "LogicalRouterUpLinkPort",
      "id": "8a0e9fb0-daf8-471f-9f80-9b5232872130",
      "display_name": "Tier0Interface1",
      "description": "Logical router port for interface /global-infra/tier-0s/Tier0Gateway1/locale-services/Tier0LocalServices-1/interfaces/Tier0Interface1",
      "tags": [
        {
          "scope": "policyPath",
          "tag": "/global-infra/tier-0s/Tier0Gateway1/locale-services/Tier0LocalServices-1/interfaces/Tier0Interface1"
        }
      ],
      "logical_router_id": "a6c54889-45e0-4855-97e0-203fae92e58d",
      "_create_user": "nsx_policy",
      "_create_time": 1586762345328,
      "_last_modified_user": "nsx_policy",
      "_last_modified_time": 1586762345328,
      "_system_owned": false,
      "_protection": "REQUIRE_OVERRIDE",
      "_revision": 0
    },
    {
      "subnets": [
        {
          "ip_addresses": [
            "192.168.60.1"
          ],
          "prefix_length": 24
        }
      ],
      "edge_cluster_member_index": [
        0
      ],
      "linked_logical_switch_port_id": {
        "target_id": "0fab401f-e65f-4235-8cf0-4757e75c8141",
        "target_display_name": "Tier0Gateway1-Tier0Interface2-ulp",
        "target_type": "LogicalPort",
        "is_valid": true
      },
      "urpf_mode": "STRICT",
      "mac_address": "00:0c:29:e6:96:7f",
      "mode": "UNTAGGED",
      "resource_type": "LogicalRouterUpLinkPort",
      "id": "3b02aa49-7923-4382-9631-c38dedcc90a3",
      "display_name": "Tier0Interface2",
      "description": "Logical router port for interface /global-infra/tier-0s/Tier0Gateway1/locale-services/Tier0LocalServices-1/interfaces/Tier0Interface2",
      "tags": [
        {
          "scope": "policyPath",
          "tag": "/global-infra/tier-0s/Tier0Gateway1/locale-services/Tier0LocalServices-1/interfaces/Tier0Interface2"
        }
      ],
      "logical_router_id": "a6c54889-45e0-4855-97e0-203fae92e58d",
      "_create_user": "nsx_policy",
      "_create_time": 1586762346241,
      "_last_modified_user": "nsx_policy",
      "_last_modified_time": 1586762346241,
      "_system_owned": false,
      "_protection": "REQUIRE_OVERRIDE",
      "_revision": 0
    },
    {
      "subnets": [
        {
          "ip_addresses": [
            "172.16.10.1"
          ],
          "prefix_length": 24
        }
      ],
      "linked_logical_switch_port_id": {
        "target_id": "2c73adf1-38b1-4841-8cec-7ce09e504427",
        "target_display_name": "infra-LS-103-lp",
        "target_type": "LogicalPort",
        "is_valid": true
      },
      "urpf_mode": "STRICT",
      "mac_address": "02:50:56:56:44:52",
      "enable_multicast": true,
      "resource_type": "LogicalRouterDownLinkPort",
      "id": "df037abc-c779-419d-8eaa-6d2c5076e4d1",
      "display_name": "infra-LS-103-dlrp",
      "description": "Logical port on logical router /global-infra/realized-state/enforcement-points/default/tier-0-logical-routers/Tier0Gateway1-t0 to connect to segment logical switch infra-LS-103-ls",
      "logical_router_id": "a6c54889-45e0-4855-97e0-203fae92e58d",
      "_create_user": "nsx_policy",
      "_create_time": 1586762042420,
      "_last_modified_user": "nsx_policy",
      "_last_modified_time": 1586762051540,
      "_system_owned": false,
      "_protection": "REQUIRE_OVERRIDE",
      "_revision": 3
    },
    {
      "subnets": [
        {
          "ip_addresses": [
            "172.16.20.1"
          ],
          "prefix_length": 24
        }
      ],
      "linked_logical_switch_port_id": {
        "target_id": "74175cd1-5cb4-4634-b521-3337827f05b4",
        "target_display_name": "infra-LS-104-lp",
        "target_type": "LogicalPort",
        "is_valid": true
      },
      "urpf_mode": "STRICT",
      "mac_address": "02:50:56:56:44:52",
      "enable_multicast": true,
      "resource_type": "LogicalRouterDownLinkPort",
      "id": "ccbf4205-5cfb-4255-ada4-5f110b8667ef",
      "display_name": "infra-LS-104-dlrp",
      "description": "Logical port on logical router /global-infra/realized-state/enforcement-points/default/tier-0-logical-routers/Tier0Gateway1-t0 to connect to segment logical switch infra-LS-104-ls",
      "logical_router_id": "a6c54889-45e0-4855-97e0-203fae92e58d",
      "_create_user": "nsx_policy",
      "_create_time": 1586762042418,
      "_last_modified_user": "nsx_policy",
      "_last_modified_time": 1586762052305,
      "_system_owned": false,
      "_protection": "REQUIRE_OVERRIDE",
      "_revision": 3
    },
    {
      "subnets": [
        {
          "ip_addresses": [
            "172.16.30.1"
          ],
          "prefix_length": 24
        }
      ],
      "linked_logical_switch_port_id": {
        "target_id": "dcd7bb5c-b46d-4715-b4ff-23187c3164e2",
        "target_display_name": "infra-LS-105-lp",
        "target_type": "LogicalPort",
        "is_valid": true
      },
      "urpf_mode": "STRICT",
      "mac_address": "02:50:56:56:44:52",
      "resource_type": "LogicalRouterDownLinkPort",
      "id": "f1f538e6-c266-4972-a9c8-868101f09a71",
      "display_name": "infra-LS-105-dlrp",
      "description": "Logical port on logical router /global-infra/realized-state/enforcement-points/default/tier-1-logical-routers/Tier1Gateway1-t1 to connect to segment logical switch infra-LS-105-ls",
      "logical_router_id": "78941d1b-3147-430e-8e27-3f6f09dc0bd3",
      "_create_user": "nsx_policy",
      "_create_time": 1586762044537,
      "_last_modified_user": "nsx_policy",
      "_last_modified_time": 1586762343496,
      "_system_owned": false,
      "_protection": "REQUIRE_OVERRIDE",
      "_revision": 3
    },
    {
      "subnets": [
        {
          "ip_addresses": [
            "172.16.40.1"
          ],
          "prefix_length": 24
        }
      ],
      "linked_logical_switch_port_id": {
        "target_id": "8f4c3dfa-d1a9-4c72-8243-866938e7b9ba",
        "target_display_name": "infra-LS-106-lp",
        "target_type": "LogicalPort",
        "is_valid": true
      },
      "urpf_mode": "STRICT",
      "mac_address": "02:50:56:56:44:52",
      "resource_type": "LogicalRouterDownLinkPort",
      "id": "3e3b0ea0-afdc-4a63-8001-b0f76458f09b",
      "display_name": "infra-LS-106-dlrp",
      "description": "Logical port on logical router /global-infra/realized-state/enforcement-points/default/tier-1-logical-routers/Tier1Gateway1-t1 to connect to segment logical switch infra-LS-106-ls",
      "logical_router_id": "78941d1b-3147-430e-8e27-3f6f09dc0bd3",
      "_create_user": "nsx_policy",
      "_create_time": 1586762044402,
      "_last_modified_user": "nsx_policy",
      "_last_modified_time": 1586762343485,
      "_system_owned": false,
      "_protection": "REQUIRE_OVERRIDE",
      "_revision": 3
    }
  ],
  "result_count": 8
}
''')

results = data['results']


# print id, resource_type, display name for all
print_data = [(record['id'], record['display_name'], record['resource_type']) for record in results]
print(*print_data, sep='\n')

# filter the results
results = [i for i in results if i['resource_type']=='LogicalRouterLinkPortOnTIER1']

# sort using id
results = sorted(results, key=lambda x: x['id'])


pprint.pprint(results)
print(len(results))