# UserListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from taikunpycore.models.user_list_dto import UserListDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserListDto from a JSON string
user_list_dto_instance = UserListDto.from_json(json)
# print the JSON string representation of the object
print(UserListDto.to_json())

# convert the object into a dict
user_list_dto_dict = user_list_dto_instance.to_dict()
# create an instance of UserListDto from a dict
user_list_dto_from_dict = UserListDto.from_dict(user_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


