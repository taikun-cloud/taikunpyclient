# PrometheusLabelListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from taikunpycore.models.prometheus_label_list_dto import PrometheusLabelListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusLabelListDto from a JSON string
prometheus_label_list_dto_instance = PrometheusLabelListDto.from_json(json)
# print the JSON string representation of the object
print(PrometheusLabelListDto.to_json())

# convert the object into a dict
prometheus_label_list_dto_dict = prometheus_label_list_dto_instance.to_dict()
# create an instance of PrometheusLabelListDto from a dict
prometheus_label_list_dto_from_dict = PrometheusLabelListDto.from_dict(prometheus_label_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


