# ArchiveTicketCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.archive_ticket_command import ArchiveTicketCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveTicketCommand from a JSON string
archive_ticket_command_instance = ArchiveTicketCommand.from_json(json)
# print the JSON string representation of the object
print(ArchiveTicketCommand.to_json())

# convert the object into a dict
archive_ticket_command_dict = archive_ticket_command_instance.to_dict()
# create an instance of ArchiveTicketCommand from a dict
archive_ticket_command_from_dict = ArchiveTicketCommand.from_dict(archive_ticket_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


