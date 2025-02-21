# ProxmoxFlavorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProxmoxFlavorData]**](ProxmoxFlavorData.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.proxmox_flavor_list import ProxmoxFlavorList

# TODO update the JSON string below
json = "{}"
# create an instance of ProxmoxFlavorList from a JSON string
proxmox_flavor_list_instance = ProxmoxFlavorList.from_json(json)
# print the JSON string representation of the object
print(ProxmoxFlavorList.to_json())

# convert the object into a dict
proxmox_flavor_list_dict = proxmox_flavor_list_instance.to_dict()
# create an instance of ProxmoxFlavorList from a dict
proxmox_flavor_list_from_dict = ProxmoxFlavorList.from_dict(proxmox_flavor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


