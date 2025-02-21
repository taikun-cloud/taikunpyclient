# ProxmoxFlavorData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cpu** | **int** |  | 
**ram** | **float** |  | 

## Example

```python
from taikunpycore.models.proxmox_flavor_data import ProxmoxFlavorData

# TODO update the JSON string below
json = "{}"
# create an instance of ProxmoxFlavorData from a JSON string
proxmox_flavor_data_instance = ProxmoxFlavorData.from_json(json)
# print the JSON string representation of the object
print(ProxmoxFlavorData.to_json())

# convert the object into a dict
proxmox_flavor_data_dict = proxmox_flavor_data_instance.to_dict()
# create an instance of ProxmoxFlavorData from a dict
proxmox_flavor_data_from_dict = ProxmoxFlavorData.from_dict(proxmox_flavor_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


