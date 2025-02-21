# TransferTicketCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.transfer_ticket_command import TransferTicketCommand

# TODO update the JSON string below
json = "{}"
# create an instance of TransferTicketCommand from a JSON string
transfer_ticket_command_instance = TransferTicketCommand.from_json(json)
# print the JSON string representation of the object
print(TransferTicketCommand.to_json())

# convert the object into a dict
transfer_ticket_command_dict = transfer_ticket_command_instance.to_dict()
# create an instance of TransferTicketCommand from a dict
transfer_ticket_command_from_dict = TransferTicketCommand.from_dict(transfer_ticket_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


