# UserTokenCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.user_token_create_dto import UserTokenCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserTokenCreateDto from a JSON string
user_token_create_dto_instance = UserTokenCreateDto.from_json(json)
# print the JSON string representation of the object
print(UserTokenCreateDto.to_json())

# convert the object into a dict
user_token_create_dto_dict = user_token_create_dto_instance.to_dict()
# create an instance of UserTokenCreateDto from a dict
user_token_create_dto_from_dict = UserTokenCreateDto.from_dict(user_token_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


