# GetToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**refresh_token_expire_time** | **datetime** |  | [optional] 
**temp_token** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.get_token import GetToken

# TODO update the JSON string below
json = "{}"
# create an instance of GetToken from a JSON string
get_token_instance = GetToken.from_json(json)
# print the JSON string representation of the object
print(GetToken.to_json())

# convert the object into a dict
get_token_dict = get_token_instance.to_dict()
# create an instance of GetToken from a dict
get_token_from_dict = GetToken.from_dict(get_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


