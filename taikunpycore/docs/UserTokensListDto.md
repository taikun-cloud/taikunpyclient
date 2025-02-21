# UserTokensListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**created_at** | **str** |  | 
**is_readonly** | **bool** |  | 
**expire_date** | **str** |  | 
**access_key** | **str** |  | 

## Example

```python
from taikunpycore.models.user_tokens_list_dto import UserTokensListDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserTokensListDto from a JSON string
user_tokens_list_dto_instance = UserTokensListDto.from_json(json)
# print the JSON string representation of the object
print(UserTokensListDto.to_json())

# convert the object into a dict
user_tokens_list_dto_dict = user_tokens_list_dto_instance.to_dict()
# create an instance of UserTokensListDto from a dict
user_tokens_list_dto_from_dict = UserTokensListDto.from_dict(user_tokens_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


