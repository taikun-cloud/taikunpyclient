# EstimatedInfracost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**projects** | [**List[ProjectInfracost]**](ProjectInfracost.md) |  | [optional] 
**total_hourly_cost** | **str** |  | [optional] 
**total_monthly_cost** | **str** |  | [optional] 
**total_monthly_usage_cost** | **str** |  | [optional] 
**past_total_hourly_cost** | **str** |  | [optional] 
**past_total_monthly_cost** | **str** |  | [optional] 
**past_total_monthly_usage_cost** | **str** |  | [optional] 
**diff_total_hourly_cost** | **str** |  | [optional] 
**diff_total_monthly_cost** | **str** |  | [optional] 
**diff_total_monthly_usage_cost** | **str** |  | [optional] 
**time_generated** | **str** |  | [optional] 
**summary** | [**Summary**](Summary.md) |  | [optional] 

## Example

```python
from taikunpycore.models.estimated_infracost import EstimatedInfracost

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedInfracost from a JSON string
estimated_infracost_instance = EstimatedInfracost.from_json(json)
# print the JSON string representation of the object
print(EstimatedInfracost.to_json())

# convert the object into a dict
estimated_infracost_dict = estimated_infracost_instance.to_dict()
# create an instance of EstimatedInfracost from a dict
estimated_infracost_from_dict = EstimatedInfracost.from_dict(estimated_infracost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


