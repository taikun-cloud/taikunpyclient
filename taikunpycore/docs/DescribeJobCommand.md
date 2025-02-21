# DescribeJobCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_job_command import DescribeJobCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeJobCommand from a JSON string
describe_job_command_instance = DescribeJobCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeJobCommand.to_json())

# convert the object into a dict
describe_job_command_dict = describe_job_command_instance.to_dict()
# create an instance of DescribeJobCommand from a dict
describe_job_command_from_dict = DescribeJobCommand.from_dict(describe_job_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


