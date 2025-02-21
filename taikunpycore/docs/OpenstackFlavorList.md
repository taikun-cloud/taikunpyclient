# OpenstackFlavorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OpenstackFlavorListDto]**](OpenstackFlavorListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.openstack_flavor_list import OpenstackFlavorList

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackFlavorList from a JSON string
openstack_flavor_list_instance = OpenstackFlavorList.from_json(json)
# print the JSON string representation of the object
print(OpenstackFlavorList.to_json())

# convert the object into a dict
openstack_flavor_list_dict = openstack_flavor_list_instance.to_dict()
# create an instance of OpenstackFlavorList from a dict
openstack_flavor_list_from_dict = OpenstackFlavorList.from_dict(openstack_flavor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


