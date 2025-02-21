# SshUserCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ssh_public_key** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.ssh_user_create_dto import SshUserCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SshUserCreateDto from a JSON string
ssh_user_create_dto_instance = SshUserCreateDto.from_json(json)
# print the JSON string representation of the object
print(SshUserCreateDto.to_json())

# convert the object into a dict
ssh_user_create_dto_dict = ssh_user_create_dto_instance.to_dict()
# create an instance of SshUserCreateDto from a dict
ssh_user_create_dto_from_dict = SshUserCreateDto.from_dict(ssh_user_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


