# ProxmoxListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**project_count** | **int** |  | 
**is_locked** | **bool** |  | 
**name** | **str** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**created_by** | **str** |  | 
**created_at** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**is_default** | **bool** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**continent_name** | **str** |  | 
**hypervisors** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**token_id** | **str** |  | 
**url** | **str** |  | 
**storage** | **str** |  | 
**vm_template_name** | **str** |  | 
**proxmox_networks** | [**List[ProxmoxNetworkListDto]**](ProxmoxNetworkListDto.md) |  | 
**skip_tls_flag** | **bool** |  | 

## Example

```python
from taikunpycore.models.proxmox_list_dto import ProxmoxListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProxmoxListDto from a JSON string
proxmox_list_dto_instance = ProxmoxListDto.from_json(json)
# print the JSON string representation of the object
print(ProxmoxListDto.to_json())

# convert the object into a dict
proxmox_list_dto_dict = proxmox_list_dto_instance.to_dict()
# create an instance of ProxmoxListDto from a dict
proxmox_list_dto_from_dict = ProxmoxListDto.from_dict(proxmox_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


