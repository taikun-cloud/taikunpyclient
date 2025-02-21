# ServerActionButtonVisibilityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**reboot** | **bool** |  | [optional] 
**console** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.server_action_button_visibility_dto import ServerActionButtonVisibilityDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerActionButtonVisibilityDto from a JSON string
server_action_button_visibility_dto_instance = ServerActionButtonVisibilityDto.from_json(json)
# print the JSON string representation of the object
print(ServerActionButtonVisibilityDto.to_json())

# convert the object into a dict
server_action_button_visibility_dto_dict = server_action_button_visibility_dto_instance.to_dict()
# create an instance of ServerActionButtonVisibilityDto from a dict
server_action_button_visibility_dto_from_dict = ServerActionButtonVisibilityDto.from_dict(server_action_button_visibility_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


