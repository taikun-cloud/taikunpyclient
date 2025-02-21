# BindAppRepositoryCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filtering_elements** | [**List[FilteringElementDto]**](FilteringElementDto.md) |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.bind_app_repository_command import BindAppRepositoryCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BindAppRepositoryCommand from a JSON string
bind_app_repository_command_instance = BindAppRepositoryCommand.from_json(json)
# print the JSON string representation of the object
print(BindAppRepositoryCommand.to_json())

# convert the object into a dict
bind_app_repository_command_dict = bind_app_repository_command_instance.to_dict()
# create an instance of BindAppRepositoryCommand from a dict
bind_app_repository_command_from_dict = BindAppRepositoryCommand.from_dict(bind_app_repository_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


