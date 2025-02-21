# PrometheusDashboardCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.prometheus_dashboard_create_command import PrometheusDashboardCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusDashboardCreateCommand from a JSON string
prometheus_dashboard_create_command_instance = PrometheusDashboardCreateCommand.from_json(json)
# print the JSON string representation of the object
print(PrometheusDashboardCreateCommand.to_json())

# convert the object into a dict
prometheus_dashboard_create_command_dict = prometheus_dashboard_create_command_instance.to_dict()
# create an instance of PrometheusDashboardCreateCommand from a dict
prometheus_dashboard_create_command_from_dict = PrometheusDashboardCreateCommand.from_dict(prometheus_dashboard_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


