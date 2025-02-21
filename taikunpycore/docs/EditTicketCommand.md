# EditTicketCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_ticket_command import EditTicketCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EditTicketCommand from a JSON string
edit_ticket_command_instance = EditTicketCommand.from_json(json)
# print the JSON string representation of the object
print(EditTicketCommand.to_json())

# convert the object into a dict
edit_ticket_command_dict = edit_ticket_command_instance.to_dict()
# create an instance of EditTicketCommand from a dict
edit_ticket_command_from_dict = EditTicketCommand.from_dict(edit_ticket_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


