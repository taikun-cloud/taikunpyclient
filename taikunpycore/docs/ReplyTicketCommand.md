# ReplyTicketCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** |  | [optional] 
**body** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.reply_ticket_command import ReplyTicketCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ReplyTicketCommand from a JSON string
reply_ticket_command_instance = ReplyTicketCommand.from_json(json)
# print the JSON string representation of the object
print(ReplyTicketCommand.to_json())

# convert the object into a dict
reply_ticket_command_dict = reply_ticket_command_instance.to_dict()
# create an instance of ReplyTicketCommand from a dict
reply_ticket_command_from_dict = ReplyTicketCommand.from_dict(reply_ticket_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


