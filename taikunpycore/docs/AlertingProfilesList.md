# AlertingProfilesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlertingProfilesListDto]**](AlertingProfilesListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.alerting_profiles_list import AlertingProfilesList

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingProfilesList from a JSON string
alerting_profiles_list_instance = AlertingProfilesList.from_json(json)
# print the JSON string representation of the object
print(AlertingProfilesList.to_json())

# convert the object into a dict
alerting_profiles_list_dict = alerting_profiles_list_instance.to_dict()
# create an instance of AlertingProfilesList from a dict
alerting_profiles_list_from_dict = AlertingProfilesList.from_dict(alerting_profiles_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


