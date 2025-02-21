# VsphereFlavorData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cpu** | **int** |  | 
**ram** | **float** |  | 

## Example

```python
from taikunpycore.models.vsphere_flavor_data import VsphereFlavorData

# TODO update the JSON string below
json = "{}"
# create an instance of VsphereFlavorData from a JSON string
vsphere_flavor_data_instance = VsphereFlavorData.from_json(json)
# print the JSON string representation of the object
print(VsphereFlavorData.to_json())

# convert the object into a dict
vsphere_flavor_data_dict = vsphere_flavor_data_instance.to_dict()
# create an instance of VsphereFlavorData from a dict
vsphere_flavor_data_from_dict = VsphereFlavorData.from_dict(vsphere_flavor_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


