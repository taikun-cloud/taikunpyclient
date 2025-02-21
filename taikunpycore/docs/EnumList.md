# EnumList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_types** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**project_statuses** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**server_roles** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**server_statuses** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**user_roles** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**security_group_rules** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**prometheus_types** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**audit_logs** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**reboot_options** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**availability** | [**List[CommonAvailabilityDto]**](CommonAvailabilityDto.md) |  | 
**slack_types** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**request_logs** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**azure_quotas** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**showback_kinds** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**alert_types** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**reminder_types** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**aws_platforms** | [**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md) |  | 
**cron_periods** | [**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md) |  | 
**validity_periods** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**alerting_integration_types** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**google_image_types** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**standalone_vm_statuses** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**openstack_continents** | [**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md) |  | 
**retention_periods** | [**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md) |  | 
**ticket_priorities** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**proxmox_roles** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 

## Example

```python
from taikunpycore.models.enum_list import EnumList

# TODO update the JSON string below
json = "{}"
# create an instance of EnumList from a JSON string
enum_list_instance = EnumList.from_json(json)
# print the JSON string representation of the object
print(EnumList.to_json())

# convert the object into a dict
enum_list_dict = enum_list_instance.to_dict()
# create an instance of EnumList from a dict
enum_list_from_dict = EnumList.from_dict(enum_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


