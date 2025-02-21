# DescribeCronJobCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_cron_job_command import DescribeCronJobCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeCronJobCommand from a JSON string
describe_cron_job_command_instance = DescribeCronJobCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeCronJobCommand.to_json())

# convert the object into a dict
describe_cron_job_command_dict = describe_cron_job_command_instance.to_dict()
# create an instance of DescribeCronJobCommand from a dict
describe_cron_job_command_from_dict = DescribeCronJobCommand.from_dict(describe_cron_job_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


