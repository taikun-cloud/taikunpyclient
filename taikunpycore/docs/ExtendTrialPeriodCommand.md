# ExtendTrialPeriodCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**days** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.extend_trial_period_command import ExtendTrialPeriodCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendTrialPeriodCommand from a JSON string
extend_trial_period_command_instance = ExtendTrialPeriodCommand.from_json(json)
# print the JSON string representation of the object
print(ExtendTrialPeriodCommand.to_json())

# convert the object into a dict
extend_trial_period_command_dict = extend_trial_period_command_instance.to_dict()
# create an instance of ExtendTrialPeriodCommand from a dict
extend_trial_period_command_from_dict = ExtendTrialPeriodCommand.from_dict(extend_trial_period_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


