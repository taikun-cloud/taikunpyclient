# CreateTicketCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**priority** | [**TicketPriority**](TicketPriority.md) |  | [optional] 

## Example

```python
from taikunpycore.models.create_ticket_command import CreateTicketCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTicketCommand from a JSON string
create_ticket_command_instance = CreateTicketCommand.from_json(json)
# print the JSON string representation of the object
print(CreateTicketCommand.to_json())

# convert the object into a dict
create_ticket_command_dict = create_ticket_command_instance.to_dict()
# create an instance of CreateTicketCommand from a dict
create_ticket_command_from_dict = CreateTicketCommand.from_dict(create_ticket_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


