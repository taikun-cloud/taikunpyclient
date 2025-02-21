# PrometheusOrganizationDiscountDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**rule_discount_rate** | **float** |  | 
**global_discount_rate** | **float** |  | 

## Example

```python
from taikunpycore.models.prometheus_organization_discount_dto import PrometheusOrganizationDiscountDto

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusOrganizationDiscountDto from a JSON string
prometheus_organization_discount_dto_instance = PrometheusOrganizationDiscountDto.from_json(json)
# print the JSON string representation of the object
print(PrometheusOrganizationDiscountDto.to_json())

# convert the object into a dict
prometheus_organization_discount_dto_dict = prometheus_organization_discount_dto_instance.to_dict()
# create an instance of PrometheusOrganizationDiscountDto from a dict
prometheus_organization_discount_dto_from_dict = PrometheusOrganizationDiscountDto.from_dict(prometheus_organization_discount_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


