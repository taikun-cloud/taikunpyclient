# UserGroupEntityListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from taikunpycore.models.user_group_entity_list_dto import UserGroupEntityListDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupEntityListDto from a JSON string
user_group_entity_list_dto_instance = UserGroupEntityListDto.from_json(json)
# print the JSON string representation of the object
print(UserGroupEntityListDto.to_json())

# convert the object into a dict
user_group_entity_list_dto_dict = user_group_entity_list_dto_instance.to_dict()
# create an instance of UserGroupEntityListDto from a dict
user_group_entity_list_dto_from_dict = UserGroupEntityListDto.from_dict(user_group_entity_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


