# NotificationListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**action_message** | **str** |  | 
**action_status** | [**ActionStatus**](ActionStatus.md) |  | 
**username** | **str** |  | 
**category** | [**ActionType**](ActionType.md) |  | 
**project_name** | **str** |  | 
**project_id** | **int** |  | 
**is_deleted** | **bool** |  | 

## Example

```python
from taikunpycore.models.notification_list_dto import NotificationListDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationListDto from a JSON string
notification_list_dto_instance = NotificationListDto.from_json(json)
# print the JSON string representation of the object
print(NotificationListDto.to_json())

# convert the object into a dict
notification_list_dto_dict = notification_list_dto_instance.to_dict()
# create an instance of NotificationListDto from a dict
notification_list_dto_from_dict = NotificationListDto.from_dict(notification_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


