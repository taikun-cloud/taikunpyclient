# NotificationHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NotificationListDto]**](NotificationListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.notification_history import NotificationHistory

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationHistory from a JSON string
notification_history_instance = NotificationHistory.from_json(json)
# print the JSON string representation of the object
print(NotificationHistory.to_json())

# convert the object into a dict
notification_history_dict = notification_history_instance.to_dict()
# create an instance of NotificationHistory from a dict
notification_history_from_dict = NotificationHistory.from_dict(notification_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


