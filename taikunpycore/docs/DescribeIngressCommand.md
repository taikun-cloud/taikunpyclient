# DescribeIngressCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_ingress_command import DescribeIngressCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeIngressCommand from a JSON string
describe_ingress_command_instance = DescribeIngressCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeIngressCommand.to_json())

# convert the object into a dict
describe_ingress_command_dict = describe_ingress_command_instance.to_dict()
# create an instance of DescribeIngressCommand from a dict
describe_ingress_command_from_dict = DescribeIngressCommand.from_dict(describe_ingress_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


