# OpenshiftCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**kube_config** | **str** |  | [optional] 
**pull_secret** | **str** |  | [optional] 
**storage_class** | **str** |  | [optional] 
**base_domain** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.openshift_create_command import OpenshiftCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of OpenshiftCreateCommand from a JSON string
openshift_create_command_instance = OpenshiftCreateCommand.from_json(json)
# print the JSON string representation of the object
print(OpenshiftCreateCommand.to_json())

# convert the object into a dict
openshift_create_command_dict = openshift_create_command_instance.to_dict()
# create an instance of OpenshiftCreateCommand from a dict
openshift_create_command_from_dict = OpenshiftCreateCommand.from_dict(openshift_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


