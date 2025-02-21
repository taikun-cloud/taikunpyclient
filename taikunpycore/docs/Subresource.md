# Subresource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**metadata** | **Dict[str, Optional[object]]** |  | [optional] 
**hourly_cost** | **str** |  | [optional] 
**monthly_cost** | **str** |  | [optional] 
**cost_components** | [**List[CostComponent]**](CostComponent.md) |  | [optional] 

## Example

```python
from taikunpycore.models.subresource import Subresource

# TODO update the JSON string below
json = "{}"
# create an instance of Subresource from a JSON string
subresource_instance = Subresource.from_json(json)
# print the JSON string representation of the object
print(Subresource.to_json())

# convert the object into a dict
subresource_dict = subresource_instance.to_dict()
# create an instance of Subresource from a dict
subresource_from_dict = Subresource.from_dict(subresource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


