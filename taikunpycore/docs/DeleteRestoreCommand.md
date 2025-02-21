# DeleteRestoreCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_restore_command import DeleteRestoreCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRestoreCommand from a JSON string
delete_restore_command_instance = DeleteRestoreCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteRestoreCommand.to_json())

# convert the object into a dict
delete_restore_command_dict = delete_restore_command_instance.to_dict()
# create an instance of DeleteRestoreCommand from a dict
delete_restore_command_from_dict = DeleteRestoreCommand.from_dict(delete_restore_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


