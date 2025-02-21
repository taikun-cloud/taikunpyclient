# StsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StsDto]**](StsDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.sts_list import StsList

# TODO update the JSON string below
json = "{}"
# create an instance of StsList from a JSON string
sts_list_instance = StsList.from_json(json)
# print the JSON string representation of the object
print(StsList.to_json())

# convert the object into a dict
sts_list_dict = sts_list_instance.to_dict()
# create an instance of StsList from a dict
sts_list_from_dict = StsList.from_dict(sts_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


