# FinalPriceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.final_price_command import FinalPriceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of FinalPriceCommand from a JSON string
final_price_command_instance = FinalPriceCommand.from_json(json)
# print the JSON string representation of the object
print(FinalPriceCommand.to_json())

# convert the object into a dict
final_price_command_dict = final_price_command_instance.to_dict()
# create an instance of FinalPriceCommand from a dict
final_price_command_from_dict = FinalPriceCommand.from_dict(final_price_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


