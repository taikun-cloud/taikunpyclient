# AllowedHostListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**description** | **str** |  | 
**ip_address** | **str** |  | 
**mask_bits** | **int** |  | 
**access_profile_id** | **int** |  | 
**access_profile_name** | **str** |  | 

## Example

```python
from taikunpycore.models.allowed_host_list_dto import AllowedHostListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedHostListDto from a JSON string
allowed_host_list_dto_instance = AllowedHostListDto.from_json(json)
# print the JSON string representation of the object
print(AllowedHostListDto.to_json())

# convert the object into a dict
allowed_host_list_dto_dict = allowed_host_list_dto_instance.to_dict()
# create an instance of AllowedHostListDto from a dict
allowed_host_list_dto_from_dict = AllowedHostListDto.from_dict(allowed_host_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


