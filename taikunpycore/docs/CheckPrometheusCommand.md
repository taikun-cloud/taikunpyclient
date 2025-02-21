# CheckPrometheusCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.check_prometheus_command import CheckPrometheusCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CheckPrometheusCommand from a JSON string
check_prometheus_command_instance = CheckPrometheusCommand.from_json(json)
# print the JSON string representation of the object
print(CheckPrometheusCommand.to_json())

# convert the object into a dict
check_prometheus_command_dict = check_prometheus_command_instance.to_dict()
# create an instance of CheckPrometheusCommand from a dict
check_prometheus_command_from_dict = CheckPrometheusCommand.from_dict(check_prometheus_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


