# UpdateSlackConfigurationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 
**slack_type** | [**SlackType**](SlackType.md) |  | [optional] 

## Example

```python
from taikunpycore.models.update_slack_configuration_dto import UpdateSlackConfigurationDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSlackConfigurationDto from a JSON string
update_slack_configuration_dto_instance = UpdateSlackConfigurationDto.from_json(json)
# print the JSON string representation of the object
print(UpdateSlackConfigurationDto.to_json())

# convert the object into a dict
update_slack_configuration_dto_dict = update_slack_configuration_dto_instance.to_dict()
# create an instance of UpdateSlackConfigurationDto from a dict
update_slack_configuration_dto_from_dict = UpdateSlackConfigurationDto.from_dict(update_slack_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


