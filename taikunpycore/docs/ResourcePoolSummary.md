# ResourcePoolSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**resource_pool** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.resource_pool_summary import ResourcePoolSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolSummary from a JSON string
resource_pool_summary_instance = ResourcePoolSummary.from_json(json)
# print the JSON string representation of the object
print(ResourcePoolSummary.to_json())

# convert the object into a dict
resource_pool_summary_dict = resource_pool_summary_instance.to_dict()
# create an instance of ResourcePoolSummary from a dict
resource_pool_summary_from_dict = ResourcePoolSummary.from_dict(resource_pool_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


