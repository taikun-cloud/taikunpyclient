# SlackConfigurationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**channel** | **str** |  | 
**organization_name** | **str** |  | 
**organization_id** | **int** |  | 
**slack_type** | [**SlackType**](SlackType.md) |  | 

## Example

```python
from taikunpycore.models.slack_configuration_dto import SlackConfigurationDto

# TODO update the JSON string below
json = "{}"
# create an instance of SlackConfigurationDto from a JSON string
slack_configuration_dto_instance = SlackConfigurationDto.from_json(json)
# print the JSON string representation of the object
print(SlackConfigurationDto.to_json())

# convert the object into a dict
slack_configuration_dto_dict = slack_configuration_dto_instance.to_dict()
# create an instance of SlackConfigurationDto from a dict
slack_configuration_dto_from_dict = SlackConfigurationDto.from_dict(slack_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


