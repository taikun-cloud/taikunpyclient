# PrometheusDashboardDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**expression_decoded** | **str** |  | 
**expression_encoded** | **str** |  | 
**description** | **str** |  | 
**is_readonly** | **bool** |  | 

## Example

```python
from taikunpycore.models.prometheus_dashboard_dto import PrometheusDashboardDto

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusDashboardDto from a JSON string
prometheus_dashboard_dto_instance = PrometheusDashboardDto.from_json(json)
# print the JSON string representation of the object
print(PrometheusDashboardDto.to_json())

# convert the object into a dict
prometheus_dashboard_dto_dict = prometheus_dashboard_dto_instance.to_dict()
# create an instance of PrometheusDashboardDto from a dict
prometheus_dashboard_dto_from_dict = PrometheusDashboardDto.from_dict(prometheus_dashboard_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


