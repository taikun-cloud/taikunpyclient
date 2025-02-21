# ProxmoxList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProxmoxListDto]**](ProxmoxListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.proxmox_list import ProxmoxList

# TODO update the JSON string below
json = "{}"
# create an instance of ProxmoxList from a JSON string
proxmox_list_instance = ProxmoxList.from_json(json)
# print the JSON string representation of the object
print(ProxmoxList.to_json())

# convert the object into a dict
proxmox_list_dict = proxmox_list_instance.to_dict()
# create an instance of ProxmoxList from a dict
proxmox_list_from_dict = ProxmoxList.from_dict(proxmox_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


