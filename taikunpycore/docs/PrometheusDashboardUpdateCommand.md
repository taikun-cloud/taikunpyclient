# PrometheusDashboardUpdateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.prometheus_dashboard_update_command import PrometheusDashboardUpdateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusDashboardUpdateCommand from a JSON string
prometheus_dashboard_update_command_instance = PrometheusDashboardUpdateCommand.from_json(json)
# print the JSON string representation of the object
print(PrometheusDashboardUpdateCommand.to_json())

# convert the object into a dict
prometheus_dashboard_update_command_dict = prometheus_dashboard_update_command_instance.to_dict()
# create an instance of PrometheusDashboardUpdateCommand from a dict
prometheus_dashboard_update_command_from_dict = PrometheusDashboardUpdateCommand.from_dict(prometheus_dashboard_update_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


