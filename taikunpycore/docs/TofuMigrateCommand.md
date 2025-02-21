# TofuMigrateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**force** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.tofu_migrate_command import TofuMigrateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of TofuMigrateCommand from a JSON string
tofu_migrate_command_instance = TofuMigrateCommand.from_json(json)
# print the JSON string representation of the object
print(TofuMigrateCommand.to_json())

# convert the object into a dict
tofu_migrate_command_dict = tofu_migrate_command_instance.to_dict()
# create an instance of TofuMigrateCommand from a dict
tofu_migrate_command_from_dict = TofuMigrateCommand.from_dict(tofu_migrate_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


