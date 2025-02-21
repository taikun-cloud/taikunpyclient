# UnbindAppRepositoryCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.unbind_app_repository_command import UnbindAppRepositoryCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UnbindAppRepositoryCommand from a JSON string
unbind_app_repository_command_instance = UnbindAppRepositoryCommand.from_json(json)
# print the JSON string representation of the object
print(UnbindAppRepositoryCommand.to_json())

# convert the object into a dict
unbind_app_repository_command_dict = unbind_app_repository_command_instance.to_dict()
# create an instance of UnbindAppRepositoryCommand from a dict
unbind_app_repository_command_from_dict = UnbindAppRepositoryCommand.from_dict(unbind_app_repository_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


