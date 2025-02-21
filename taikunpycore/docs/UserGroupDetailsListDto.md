# UserGroupDetailsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**users** | [**List[UserListDto]**](UserListDto.md) |  | 
**project_groups** | [**List[ProjectGroupEntityListDto]**](ProjectGroupEntityListDto.md) |  | 

## Example

```python
from taikunpycore.models.user_group_details_list_dto import UserGroupDetailsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupDetailsListDto from a JSON string
user_group_details_list_dto_instance = UserGroupDetailsListDto.from_json(json)
# print the JSON string representation of the object
print(UserGroupDetailsListDto.to_json())

# convert the object into a dict
user_group_details_list_dto_dict = user_group_details_list_dto_instance.to_dict()
# create an instance of UserGroupDetailsListDto from a dict
user_group_details_list_dto_from_dict = UserGroupDetailsListDto.from_dict(user_group_details_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


