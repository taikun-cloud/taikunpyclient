# DescribeDeploymentCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_deployment_command import DescribeDeploymentCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeDeploymentCommand from a JSON string
describe_deployment_command_instance = DescribeDeploymentCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeDeploymentCommand.to_json())

# convert the object into a dict
describe_deployment_command_dict = describe_deployment_command_instance.to_dict()
# create an instance of DescribeDeploymentCommand from a dict
describe_deployment_command_from_dict = DescribeDeploymentCommand.from_dict(describe_deployment_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


