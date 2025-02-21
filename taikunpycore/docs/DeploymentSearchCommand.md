# DeploymentSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.deployment_search_command import DeploymentSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentSearchCommand from a JSON string
deployment_search_command_instance = DeploymentSearchCommand.from_json(json)
# print the JSON string representation of the object
print(DeploymentSearchCommand.to_json())

# convert the object into a dict
deployment_search_command_dict = deployment_search_command_instance.to_dict()
# create an instance of DeploymentSearchCommand from a dict
deployment_search_command_from_dict = DeploymentSearchCommand.from_dict(deployment_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


