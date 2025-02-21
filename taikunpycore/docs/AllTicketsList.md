# AllTicketsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AllTicketsDto]**](AllTicketsDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.all_tickets_list import AllTicketsList

# TODO update the JSON string below
json = "{}"
# create an instance of AllTicketsList from a JSON string
all_tickets_list_instance = AllTicketsList.from_json(json)
# print the JSON string representation of the object
print(AllTicketsList.to_json())

# convert the object into a dict
all_tickets_list_dict = all_tickets_list_instance.to_dict()
# create an instance of AllTicketsList from a dict
all_tickets_list_from_dict = AllTicketsList.from_dict(all_tickets_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


