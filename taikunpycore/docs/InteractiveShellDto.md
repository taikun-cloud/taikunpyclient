# InteractiveShellDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kube_config** | **str** |  | [optional] 
**admin_kube_config** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.interactive_shell_dto import InteractiveShellDto

# TODO update the JSON string below
json = "{}"
# create an instance of InteractiveShellDto from a JSON string
interactive_shell_dto_instance = InteractiveShellDto.from_json(json)
# print the JSON string representation of the object
print(InteractiveShellDto.to_json())

# convert the object into a dict
interactive_shell_dto_dict = interactive_shell_dto_instance.to_dict()
# create an instance of InteractiveShellDto from a dict
interactive_shell_dto_from_dict = InteractiveShellDto.from_dict(interactive_shell_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


