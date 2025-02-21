# AllowedHostList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AllowedHostListDto]**](AllowedHostListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.allowed_host_list import AllowedHostList

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedHostList from a JSON string
allowed_host_list_instance = AllowedHostList.from_json(json)
# print the JSON string representation of the object
print(AllowedHostList.to_json())

# convert the object into a dict
allowed_host_list_dict = allowed_host_list_instance.to_dict()
# create an instance of AllowedHostList from a dict
allowed_host_list_from_dict = AllowedHostList.from_dict(allowed_host_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


