# DeleteRepositoryCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_repo_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_repository_command import DeleteRepositoryCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRepositoryCommand from a JSON string
delete_repository_command_instance = DeleteRepositoryCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteRepositoryCommand.to_json())

# convert the object into a dict
delete_repository_command_dict = delete_repository_command_instance.to_dict()
# create an instance of DeleteRepositoryCommand from a dict
delete_repository_command_from_dict = DeleteRepositoryCommand.from_dict(delete_repository_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


