# ExportKubeConfigCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.export_kube_config_command import ExportKubeConfigCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ExportKubeConfigCommand from a JSON string
export_kube_config_command_instance = ExportKubeConfigCommand.from_json(json)
# print the JSON string representation of the object
print(ExportKubeConfigCommand.to_json())

# convert the object into a dict
export_kube_config_command_dict = export_kube_config_command_instance.to_dict()
# create an instance of ExportKubeConfigCommand from a dict
export_kube_config_command_from_dict = ExportKubeConfigCommand.from_dict(export_kube_config_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


