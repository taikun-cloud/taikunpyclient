# CloseTicketCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.close_ticket_command import CloseTicketCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CloseTicketCommand from a JSON string
close_ticket_command_instance = CloseTicketCommand.from_json(json)
# print the JSON string representation of the object
print(CloseTicketCommand.to_json())

# convert the object into a dict
close_ticket_command_dict = close_ticket_command_instance.to_dict()
# create an instance of CloseTicketCommand from a dict
close_ticket_command_from_dict = CloseTicketCommand.from_dict(close_ticket_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


