# DescribeKubernetesResourceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**kind** | [**EKubernetesResource**](EKubernetesResource.md) |  | 

## Example

```python
from taikunpycore.models.describe_kubernetes_resource_command import DescribeKubernetesResourceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeKubernetesResourceCommand from a JSON string
describe_kubernetes_resource_command_instance = DescribeKubernetesResourceCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeKubernetesResourceCommand.to_json())

# convert the object into a dict
describe_kubernetes_resource_command_dict = describe_kubernetes_resource_command_instance.to_dict()
# create an instance of DescribeKubernetesResourceCommand from a dict
describe_kubernetes_resource_command_from_dict = DescribeKubernetesResourceCommand.from_dict(describe_kubernetes_resource_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


