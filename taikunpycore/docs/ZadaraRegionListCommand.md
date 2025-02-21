# ZadaraRegionListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**zadara_access_key_id** | **str** |  | [optional] 
**zadara_secret_access_key** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.zadara_region_list_command import ZadaraRegionListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ZadaraRegionListCommand from a JSON string
zadara_region_list_command_instance = ZadaraRegionListCommand.from_json(json)
# print the JSON string representation of the object
print(ZadaraRegionListCommand.to_json())

# convert the object into a dict
zadara_region_list_command_dict = zadara_region_list_command_instance.to_dict()
# create an instance of ZadaraRegionListCommand from a dict
zadara_region_list_command_from_dict = ZadaraRegionListCommand.from_dict(zadara_region_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


