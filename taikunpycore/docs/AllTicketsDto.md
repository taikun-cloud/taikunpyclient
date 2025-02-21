# AllTicketsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**created_by** | **str** |  | 
**current_status_date** | **str** |  | 
**last_modifier** | **str** |  | 
**number** | **int** |  | 
**partner_logo** | **str** |  | 
**description** | **str** |  | 
**partner_name** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from taikunpycore.models.all_tickets_dto import AllTicketsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AllTicketsDto from a JSON string
all_tickets_dto_instance = AllTicketsDto.from_json(json)
# print the JSON string representation of the object
print(AllTicketsDto.to_json())

# convert the object into a dict
all_tickets_dto_dict = all_tickets_dto_instance.to_dict()
# create an instance of AllTicketsDto from a dict
all_tickets_dto_from_dict = AllTicketsDto.from_dict(all_tickets_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


