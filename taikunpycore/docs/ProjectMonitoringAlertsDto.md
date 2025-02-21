# ProjectMonitoringAlertsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**AlertData**](AlertData.md) |  | [optional] 

## Example

```python
from taikunpycore.models.project_monitoring_alerts_dto import ProjectMonitoringAlertsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMonitoringAlertsDto from a JSON string
project_monitoring_alerts_dto_instance = ProjectMonitoringAlertsDto.from_json(json)
# print the JSON string representation of the object
print(ProjectMonitoringAlertsDto.to_json())

# convert the object into a dict
project_monitoring_alerts_dto_dict = project_monitoring_alerts_dto_instance.to_dict()
# create an instance of ProjectMonitoringAlertsDto from a dict
project_monitoring_alerts_dto_from_dict = ProjectMonitoringAlertsDto.from_dict(project_monitoring_alerts_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


