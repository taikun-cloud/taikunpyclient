# EditProjectAppExtraValuesCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_app_id** | **int** |  | [optional] 
**extra_values** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_project_app_extra_values_command import EditProjectAppExtraValuesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EditProjectAppExtraValuesCommand from a JSON string
edit_project_app_extra_values_command_instance = EditProjectAppExtraValuesCommand.from_json(json)
# print the JSON string representation of the object
print(EditProjectAppExtraValuesCommand.to_json())

# convert the object into a dict
edit_project_app_extra_values_command_dict = edit_project_app_extra_values_command_instance.to_dict()
# create an instance of EditProjectAppExtraValuesCommand from a dict
edit_project_app_extra_values_command_from_dict = EditProjectAppExtraValuesCommand.from_dict(edit_project_app_extra_values_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


