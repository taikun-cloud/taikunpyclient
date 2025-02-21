# MonitoringCredentialsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**prometheus_url** | **str** |  | 
**loki_url** | **str** |  | 
**alert_manager_url** | **str** |  | 

## Example

```python
from taikunpycore.models.monitoring_credentials_list_dto import MonitoringCredentialsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoringCredentialsListDto from a JSON string
monitoring_credentials_list_dto_instance = MonitoringCredentialsListDto.from_json(json)
# print the JSON string representation of the object
print(MonitoringCredentialsListDto.to_json())

# convert the object into a dict
monitoring_credentials_list_dto_dict = monitoring_credentials_list_dto_instance.to_dict()
# create an instance of MonitoringCredentialsListDto from a dict
monitoring_credentials_list_dto_from_dict = MonitoringCredentialsListDto.from_dict(monitoring_credentials_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


