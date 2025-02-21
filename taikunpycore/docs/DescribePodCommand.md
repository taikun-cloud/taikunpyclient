# DescribePodCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_pod_command import DescribePodCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribePodCommand from a JSON string
describe_pod_command_instance = DescribePodCommand.from_json(json)
# print the JSON string representation of the object
print(DescribePodCommand.to_json())

# convert the object into a dict
describe_pod_command_dict = describe_pod_command_instance.to_dict()
# create an instance of DescribePodCommand from a dict
describe_pod_command_from_dict = DescribePodCommand.from_dict(describe_pod_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


