# LeaveTaikunCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.leave_taikun_command import LeaveTaikunCommand

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveTaikunCommand from a JSON string
leave_taikun_command_instance = LeaveTaikunCommand.from_json(json)
# print the JSON string representation of the object
print(LeaveTaikunCommand.to_json())

# convert the object into a dict
leave_taikun_command_dict = leave_taikun_command_instance.to_dict()
# create an instance of LeaveTaikunCommand from a dict
leave_taikun_command_from_dict = LeaveTaikunCommand.from_dict(leave_taikun_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


