# OpenstackFlavorListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ram** | **float** |  | 
**cpu** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from taikunpycore.models.openstack_flavor_list_dto import OpenstackFlavorListDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackFlavorListDto from a JSON string
openstack_flavor_list_dto_instance = OpenstackFlavorListDto.from_json(json)
# print the JSON string representation of the object
print(OpenstackFlavorListDto.to_json())

# convert the object into a dict
openstack_flavor_list_dto_dict = openstack_flavor_list_dto_instance.to_dict()
# create an instance of OpenstackFlavorListDto from a dict
openstack_flavor_list_dto_from_dict = OpenstackFlavorListDto.from_dict(openstack_flavor_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


