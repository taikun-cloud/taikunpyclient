# AddPrometheusRulesToOrganizationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**discount_rate** | **float** |  | [optional] 

## Example

```python
from taikunpycore.models.add_prometheus_rules_to_organization_dto import AddPrometheusRulesToOrganizationDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddPrometheusRulesToOrganizationDto from a JSON string
add_prometheus_rules_to_organization_dto_instance = AddPrometheusRulesToOrganizationDto.from_json(json)
# print the JSON string representation of the object
print(AddPrometheusRulesToOrganizationDto.to_json())

# convert the object into a dict
add_prometheus_rules_to_organization_dto_dict = add_prometheus_rules_to_organization_dto_instance.to_dict()
# create an instance of AddPrometheusRulesToOrganizationDto from a dict
add_prometheus_rules_to_organization_dto_from_dict = AddPrometheusRulesToOrganizationDto.from_dict(add_prometheus_rules_to_organization_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


