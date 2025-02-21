# SshUsersListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**ssh_public_key** | **str** |  | 
**access_profile_name** | **str** |  | 

## Example

```python
from taikunpycore.models.ssh_users_list_dto import SshUsersListDto

# TODO update the JSON string below
json = "{}"
# create an instance of SshUsersListDto from a JSON string
ssh_users_list_dto_instance = SshUsersListDto.from_json(json)
# print the JSON string representation of the object
print(SshUsersListDto.to_json())

# convert the object into a dict
ssh_users_list_dto_dict = ssh_users_list_dto_instance.to_dict()
# create an instance of SshUsersListDto from a dict
ssh_users_list_dto_from_dict = SshUsersListDto.from_dict(ssh_users_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


