# ZadaraAvailabilityZonesCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**zadara_access_key_id** | **str** |  | [optional] 
**zadara_secret_access_key** | **str** |  | [optional] 
**cloud_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.zadara_availability_zones_command import ZadaraAvailabilityZonesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ZadaraAvailabilityZonesCommand from a JSON string
zadara_availability_zones_command_instance = ZadaraAvailabilityZonesCommand.from_json(json)
# print the JSON string representation of the object
print(ZadaraAvailabilityZonesCommand.to_json())

# convert the object into a dict
zadara_availability_zones_command_dict = zadara_availability_zones_command_instance.to_dict()
# create an instance of ZadaraAvailabilityZonesCommand from a dict
zadara_availability_zones_command_from_dict = ZadaraAvailabilityZonesCommand.from_dict(zadara_availability_zones_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


