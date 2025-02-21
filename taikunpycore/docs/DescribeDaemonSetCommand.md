# DescribeDaemonSetCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_daemon_set_command import DescribeDaemonSetCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeDaemonSetCommand from a JSON string
describe_daemon_set_command_instance = DescribeDaemonSetCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeDaemonSetCommand.to_json())

# convert the object into a dict
describe_daemon_set_command_dict = describe_daemon_set_command_instance.to_dict()
# create an instance of DescribeDaemonSetCommand from a dict
describe_daemon_set_command_from_dict = DescribeDaemonSetCommand.from_dict(describe_daemon_set_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


