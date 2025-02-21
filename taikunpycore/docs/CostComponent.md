# CostComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**hourly_quantity** | **str** |  | [optional] 
**monthly_quantity** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**hourly_cost** | **str** |  | [optional] 
**monthly_cost** | **str** |  | [optional] 
**price_not_found** | **bool** |  | [optional] 
**usage_based** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.cost_component import CostComponent

# TODO update the JSON string below
json = "{}"
# create an instance of CostComponent from a JSON string
cost_component_instance = CostComponent.from_json(json)
# print the JSON string representation of the object
print(CostComponent.to_json())

# convert the object into a dict
cost_component_dict = cost_component_instance.to_dict()
# create an instance of CostComponent from a dict
cost_component_from_dict = CostComponent.from_dict(cost_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


