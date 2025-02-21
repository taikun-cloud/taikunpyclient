# GroupedBillings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** |  | [optional] 
**tcu** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.grouped_billings import GroupedBillings

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedBillings from a JSON string
grouped_billings_instance = GroupedBillings.from_json(json)
# print the JSON string representation of the object
print(GroupedBillings.to_json())

# convert the object into a dict
grouped_billings_dict = grouped_billings_instance.to_dict()
# create an instance of GroupedBillings from a dict
grouped_billings_from_dict = GroupedBillings.from_dict(grouped_billings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


