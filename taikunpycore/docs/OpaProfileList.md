# OpaProfileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OpaProfileListDto]**](OpaProfileListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.opa_profile_list import OpaProfileList

# TODO update the JSON string below
json = "{}"
# create an instance of OpaProfileList from a JSON string
opa_profile_list_instance = OpaProfileList.from_json(json)
# print the JSON string representation of the object
print(OpaProfileList.to_json())

# convert the object into a dict
opa_profile_list_dict = opa_profile_list_instance.to_dict()
# create an instance of OpaProfileList from a dict
opa_profile_list_from_dict = OpaProfileList.from_dict(opa_profile_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


