# UpdateOpenStackCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**open_stack_user** | **str** |  | [optional] 
**open_stack_password** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_open_stack_command import UpdateOpenStackCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOpenStackCommand from a JSON string
update_open_stack_command_instance = UpdateOpenStackCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateOpenStackCommand.to_json())

# convert the object into a dict
update_open_stack_command_dict = update_open_stack_command_instance.to_dict()
# create an instance of UpdateOpenStackCommand from a dict
update_open_stack_command_from_dict = UpdateOpenStackCommand.from_dict(update_open_stack_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


