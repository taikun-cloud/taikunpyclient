# StandaloneProfileSecurityGroupListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**protocol** | **str** |  | 
**port_min_range** | **int** |  | 
**port_max_range** | **int** |  | 
**remote_ip_prefix** | **str** |  | 

## Example

```python
from taikunpycore.models.standalone_profile_security_group_list_dto import StandaloneProfileSecurityGroupListDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneProfileSecurityGroupListDto from a JSON string
standalone_profile_security_group_list_dto_instance = StandaloneProfileSecurityGroupListDto.from_json(json)
# print the JSON string representation of the object
print(StandaloneProfileSecurityGroupListDto.to_json())

# convert the object into a dict
standalone_profile_security_group_list_dto_dict = standalone_profile_security_group_list_dto_instance.to_dict()
# create an instance of StandaloneProfileSecurityGroupListDto from a dict
standalone_profile_security_group_list_dto_from_dict = StandaloneProfileSecurityGroupListDto.from_dict(standalone_profile_security_group_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


