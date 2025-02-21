# StandaloneVmsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StandaloneVmListDto]**](StandaloneVmListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.standalone_vms_list import StandaloneVmsList

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneVmsList from a JSON string
standalone_vms_list_instance = StandaloneVmsList.from_json(json)
# print the JSON string representation of the object
print(StandaloneVmsList.to_json())

# convert the object into a dict
standalone_vms_list_dict = standalone_vms_list_instance.to_dict()
# create an instance of StandaloneVmsList from a dict
standalone_vms_list_from_dict = StandaloneVmsList.from_dict(standalone_vms_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


