# SlackConfigurationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SlackConfigurationDto]**](SlackConfigurationDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.slack_configuration_list import SlackConfigurationList

# TODO update the JSON string below
json = "{}"
# create an instance of SlackConfigurationList from a JSON string
slack_configuration_list_instance = SlackConfigurationList.from_json(json)
# print the JSON string representation of the object
print(SlackConfigurationList.to_json())

# convert the object into a dict
slack_configuration_list_dict = slack_configuration_list_instance.to_dict()
# create an instance of SlackConfigurationList from a dict
slack_configuration_list_from_dict = SlackConfigurationList.from_dict(slack_configuration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


