# EditAllowedHostDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**mask_bits** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_allowed_host_dto import EditAllowedHostDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditAllowedHostDto from a JSON string
edit_allowed_host_dto_instance = EditAllowedHostDto.from_json(json)
# print the JSON string representation of the object
print(EditAllowedHostDto.to_json())

# convert the object into a dict
edit_allowed_host_dto_dict = edit_allowed_host_dto_instance.to_dict()
# create an instance of EditAllowedHostDto from a dict
edit_allowed_host_dto_from_dict = EditAllowedHostDto.from_dict(edit_allowed_host_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


