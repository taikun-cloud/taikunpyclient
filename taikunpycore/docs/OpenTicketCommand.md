# OpenTicketCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.open_ticket_command import OpenTicketCommand

# TODO update the JSON string below
json = "{}"
# create an instance of OpenTicketCommand from a JSON string
open_ticket_command_instance = OpenTicketCommand.from_json(json)
# print the JSON string representation of the object
print(OpenTicketCommand.to_json())

# convert the object into a dict
open_ticket_command_dict = open_ticket_command_instance.to_dict()
# create an instance of OpenTicketCommand from a dict
open_ticket_command_from_dict = OpenTicketCommand.from_dict(open_ticket_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


