# DescribeNetworkPolicyCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_network_policy_command import DescribeNetworkPolicyCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeNetworkPolicyCommand from a JSON string
describe_network_policy_command_instance = DescribeNetworkPolicyCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeNetworkPolicyCommand.to_json())

# convert the object into a dict
describe_network_policy_command_dict = describe_network_policy_command_instance.to_dict()
# create an instance of DescribeNetworkPolicyCommand from a dict
describe_network_policy_command_from_dict = DescribeNetworkPolicyCommand.from_dict(describe_network_policy_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


