# CreateZadaraCloudCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**zadara_url** | **str** |  | [optional] 
**zadara_secret_access_key** | **str** |  | [optional] 
**zadara_access_key_id** | **str** |  | [optional] 
**zadara_region** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**az_count** | **int** |  | [optional] 
**zadara_continent** | **str** |  | [optional] 
**zadara_volume_type** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_zadara_cloud_command import CreateZadaraCloudCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateZadaraCloudCommand from a JSON string
create_zadara_cloud_command_instance = CreateZadaraCloudCommand.from_json(json)
# print the JSON string representation of the object
print(CreateZadaraCloudCommand.to_json())

# convert the object into a dict
create_zadara_cloud_command_dict = create_zadara_cloud_command_instance.to_dict()
# create an instance of CreateZadaraCloudCommand from a dict
create_zadara_cloud_command_from_dict = CreateZadaraCloudCommand.from_dict(create_zadara_cloud_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


