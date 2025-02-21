# SetTicketPriorityCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**priority** | [**TicketPriority**](TicketPriority.md) |  | [optional] 

## Example

```python
from taikunpycore.models.set_ticket_priority_command import SetTicketPriorityCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SetTicketPriorityCommand from a JSON string
set_ticket_priority_command_instance = SetTicketPriorityCommand.from_json(json)
# print the JSON string representation of the object
print(SetTicketPriorityCommand.to_json())

# convert the object into a dict
set_ticket_priority_command_dict = set_ticket_priority_command_instance.to_dict()
# create an instance of SetTicketPriorityCommand from a dict
set_ticket_priority_command_from_dict = SetTicketPriorityCommand.from_dict(set_ticket_priority_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


