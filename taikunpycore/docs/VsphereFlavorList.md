# VsphereFlavorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VsphereFlavorData]**](VsphereFlavorData.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.vsphere_flavor_list import VsphereFlavorList

# TODO update the JSON string below
json = "{}"
# create an instance of VsphereFlavorList from a JSON string
vsphere_flavor_list_instance = VsphereFlavorList.from_json(json)
# print the JSON string representation of the object
print(VsphereFlavorList.to_json())

# convert the object into a dict
vsphere_flavor_list_dict = vsphere_flavor_list_instance.to_dict()
# create an instance of VsphereFlavorList from a dict
vsphere_flavor_list_from_dict = VsphereFlavorList.from_dict(vsphere_flavor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


