# DatastoreSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** |  | [optional] 
**datastore** | **str** |  | [optional] 
**free_space** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.datastore_summary import DatastoreSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreSummary from a JSON string
datastore_summary_instance = DatastoreSummary.from_json(json)
# print the JSON string representation of the object
print(DatastoreSummary.to_json())

# convert the object into a dict
datastore_summary_dict = datastore_summary_instance.to_dict()
# create an instance of DatastoreSummary from a dict
datastore_summary_from_dict = DatastoreSummary.from_dict(datastore_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


