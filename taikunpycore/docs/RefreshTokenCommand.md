# RefreshTokenCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.refresh_token_command import RefreshTokenCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenCommand from a JSON string
refresh_token_command_instance = RefreshTokenCommand.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenCommand.to_json())

# convert the object into a dict
refresh_token_command_dict = refresh_token_command_instance.to_dict()
# create an instance of RefreshTokenCommand from a dict
refresh_token_command_from_dict = RefreshTokenCommand.from_dict(refresh_token_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


