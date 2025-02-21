# DatacenterSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.datacenter_summary import DatacenterSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterSummary from a JSON string
datacenter_summary_instance = DatacenterSummary.from_json(json)
# print the JSON string representation of the object
print(DatacenterSummary.to_json())

# convert the object into a dict
datacenter_summary_dict = datacenter_summary_instance.to_dict()
# create an instance of DatacenterSummary from a dict
datacenter_summary_from_dict = DatacenterSummary.from_dict(datacenter_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


