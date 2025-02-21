# CreateKubeConfigCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**is_accessible_for_all** | **bool** |  | [optional] 
**is_accessible_for_manager** | **bool** |  | [optional] 
**kube_config_role_id** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**ttl** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_kube_config_command import CreateKubeConfigCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKubeConfigCommand from a JSON string
create_kube_config_command_instance = CreateKubeConfigCommand.from_json(json)
# print the JSON string representation of the object
print(CreateKubeConfigCommand.to_json())

# convert the object into a dict
create_kube_config_command_dict = create_kube_config_command_instance.to_dict()
# create an instance of CreateKubeConfigCommand from a dict
create_kube_config_command_from_dict = CreateKubeConfigCommand.from_dict(create_kube_config_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


