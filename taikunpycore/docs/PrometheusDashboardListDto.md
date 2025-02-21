# PrometheusDashboardListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_name** | **str** |  | 
**data** | [**List[PrometheusDashboardDto]**](PrometheusDashboardDto.md) |  | 

## Example

```python
from taikunpycore.models.prometheus_dashboard_list_dto import PrometheusDashboardListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusDashboardListDto from a JSON string
prometheus_dashboard_list_dto_instance = PrometheusDashboardListDto.from_json(json)
# print the JSON string representation of the object
print(PrometheusDashboardListDto.to_json())

# convert the object into a dict
prometheus_dashboard_list_dto_dict = prometheus_dashboard_list_dto_instance.to_dict()
# create an instance of PrometheusDashboardListDto from a dict
prometheus_dashboard_list_dto_from_dict = PrometheusDashboardListDto.from_dict(prometheus_dashboard_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


