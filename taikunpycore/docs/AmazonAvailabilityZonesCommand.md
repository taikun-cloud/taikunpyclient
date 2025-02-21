# AmazonAvailabilityZonesCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** |  | [optional] 
**aws_access_key_id** | **str** |  | [optional] 
**aws_secret_access_key** | **str** |  | [optional] 
**cloud_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.amazon_availability_zones_command import AmazonAvailabilityZonesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonAvailabilityZonesCommand from a JSON string
amazon_availability_zones_command_instance = AmazonAvailabilityZonesCommand.from_json(json)
# print the JSON string representation of the object
print(AmazonAvailabilityZonesCommand.to_json())

# convert the object into a dict
amazon_availability_zones_command_dict = amazon_availability_zones_command_instance.to_dict()
# create an instance of AmazonAvailabilityZonesCommand from a dict
amazon_availability_zones_command_from_dict = AmazonAvailabilityZonesCommand.from_dict(amazon_availability_zones_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


