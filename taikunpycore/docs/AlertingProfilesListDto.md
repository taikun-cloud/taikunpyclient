# AlertingProfilesListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**slack_configuration_id** | **int** |  | 
**slack_configuration_name** | **str** |  | 
**is_locked** | **bool** |  | 
**emails** | [**List[AlertingEmailDto]**](AlertingEmailDto.md) |  | 
**webhooks** | [**List[AlertingWebhookDto]**](AlertingWebhookDto.md) |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**reminder** | [**AlertingReminder**](AlertingReminder.md) |  | 
**created_at** | **str** |  | 

## Example

```python
from taikunpycore.models.alerting_profiles_list_dto import AlertingProfilesListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingProfilesListDto from a JSON string
alerting_profiles_list_dto_instance = AlertingProfilesListDto.from_json(json)
# print the JSON string representation of the object
print(AlertingProfilesListDto.to_json())

# convert the object into a dict
alerting_profiles_list_dto_dict = alerting_profiles_list_dto_instance.to_dict()
# create an instance of AlertingProfilesListDto from a dict
alerting_profiles_list_dto_from_dict = AlertingProfilesListDto.from_dict(alerting_profiles_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


