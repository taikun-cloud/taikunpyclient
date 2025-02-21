# StandaloneProfileListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**revision** | **int** |  | 
**is_locked** | **bool** |  | 
**stand_alone_profile_security_groups** | [**List[StandaloneProfileSecurityGroupListDto]**](StandaloneProfileSecurityGroupListDto.md) |  | 

## Example

```python
from taikunpycore.models.standalone_profile_list_dto import StandaloneProfileListDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneProfileListDto from a JSON string
standalone_profile_list_dto_instance = StandaloneProfileListDto.from_json(json)
# print the JSON string representation of the object
print(StandaloneProfileListDto.to_json())

# convert the object into a dict
standalone_profile_list_dto_dict = standalone_profile_list_dto_instance.to_dict()
# create an instance of StandaloneProfileListDto from a dict
standalone_profile_list_dto_from_dict = StandaloneProfileListDto.from_dict(standalone_profile_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


