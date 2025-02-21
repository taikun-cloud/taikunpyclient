# UserGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserGroupDetailsListDto]**](UserGroupDetailsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.user_group_list import UserGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupList from a JSON string
user_group_list_instance = UserGroupList.from_json(json)
# print the JSON string representation of the object
print(UserGroupList.to_json())

# convert the object into a dict
user_group_list_dict = user_group_list_instance.to_dict()
# create an instance of UserGroupList from a dict
user_group_list_from_dict = UserGroupList.from_dict(user_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


