# Resource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**tags** | **Dict[str, Optional[str]]** |  | [optional] 
**metadata** | **Dict[str, Optional[object]]** |  | [optional] 
**hourly_cost** | **str** |  | [optional] 
**monthly_cost** | **str** |  | [optional] 
**monthly_usage_cost** | **str** |  | [optional] 
**cost_components** | [**List[CostComponent]**](CostComponent.md) |  | [optional] 
**subresources** | [**List[Subresource]**](Subresource.md) |  | [optional] 

## Example

```python
from taikunpycore.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print(Resource.to_json())

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_from_dict = Resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


