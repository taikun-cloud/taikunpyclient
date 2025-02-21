# DuplicateNameCheckerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.duplicate_name_checker_command import DuplicateNameCheckerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateNameCheckerCommand from a JSON string
duplicate_name_checker_command_instance = DuplicateNameCheckerCommand.from_json(json)
# print the JSON string representation of the object
print(DuplicateNameCheckerCommand.to_json())

# convert the object into a dict
duplicate_name_checker_command_dict = duplicate_name_checker_command_instance.to_dict()
# create an instance of DuplicateNameCheckerCommand from a dict
duplicate_name_checker_command_from_dict = DuplicateNameCheckerCommand.from_dict(duplicate_name_checker_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


