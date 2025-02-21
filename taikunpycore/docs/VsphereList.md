# VsphereList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VsphereListDto]**](VsphereListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.vsphere_list import VsphereList

# TODO update the JSON string below
json = "{}"
# create an instance of VsphereList from a JSON string
vsphere_list_instance = VsphereList.from_json(json)
# print the JSON string representation of the object
print(VsphereList.to_json())

# convert the object into a dict
vsphere_list_dict = vsphere_list_instance.to_dict()
# create an instance of VsphereList from a dict
vsphere_list_from_dict = VsphereList.from_dict(vsphere_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


