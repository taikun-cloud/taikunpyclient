# CronJobCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_period** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.cron_job_command import CronJobCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CronJobCommand from a JSON string
cron_job_command_instance = CronJobCommand.from_json(json)
# print the JSON string representation of the object
print(CronJobCommand.to_json())

# convert the object into a dict
cron_job_command_dict = cron_job_command_instance.to_dict()
# create an instance of CronJobCommand from a dict
cron_job_command_from_dict = CronJobCommand.from_dict(cron_job_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


