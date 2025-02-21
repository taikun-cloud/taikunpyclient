# ChangeCardCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.change_card_command import ChangeCardCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeCardCommand from a JSON string
change_card_command_instance = ChangeCardCommand.from_json(json)
# print the JSON string representation of the object
print(ChangeCardCommand.to_json())

# convert the object into a dict
change_card_command_dict = change_card_command_instance.to_dict()
# create an instance of ChangeCardCommand from a dict
change_card_command_from_dict = ChangeCardCommand.from_dict(change_card_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


