# ProxmoxHypervisorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**is_bound** | **bool** |  | [optional] 
**used_by_server** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.proxmox_hypervisor_dto import ProxmoxHypervisorDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProxmoxHypervisorDto from a JSON string
proxmox_hypervisor_dto_instance = ProxmoxHypervisorDto.from_json(json)
# print the JSON string representation of the object
print(ProxmoxHypervisorDto.to_json())

# convert the object into a dict
proxmox_hypervisor_dto_dict = proxmox_hypervisor_dto_instance.to_dict()
# create an instance of ProxmoxHypervisorDto from a dict
proxmox_hypervisor_dto_from_dict = ProxmoxHypervisorDto.from_dict(proxmox_hypervisor_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


