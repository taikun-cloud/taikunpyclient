# KubesprayCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**kubernetes_version** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.kubespray_create_command import KubesprayCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of KubesprayCreateCommand from a JSON string
kubespray_create_command_instance = KubesprayCreateCommand.from_json(json)
# print the JSON string representation of the object
print(KubesprayCreateCommand.to_json())

# convert the object into a dict
kubespray_create_command_dict = kubespray_create_command_instance.to_dict()
# create an instance of KubesprayCreateCommand from a dict
kubespray_create_command_from_dict = KubesprayCreateCommand.from_dict(kubespray_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


