# RegionListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_access_key_id** | **str** |  | [optional] 
**aws_secret_access_key** | **str** |  | [optional] 
**cloud_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.region_list_command import RegionListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RegionListCommand from a JSON string
region_list_command_instance = RegionListCommand.from_json(json)
# print the JSON string representation of the object
print(RegionListCommand.to_json())

# convert the object into a dict
region_list_command_dict = region_list_command_instance.to_dict()
# create an instance of RegionListCommand from a dict
region_list_command_from_dict = RegionListCommand.from_dict(region_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


