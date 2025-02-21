# AlertingEmailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from taikunpycore.models.alerting_email_dto import AlertingEmailDto

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingEmailDto from a JSON string
alerting_email_dto_instance = AlertingEmailDto.from_json(json)
# print the JSON string representation of the object
print(AlertingEmailDto.to_json())

# convert the object into a dict
alerting_email_dto_dict = alerting_email_dto_instance.to_dict()
# create an instance of AlertingEmailDto from a dict
alerting_email_dto_from_dict = AlertingEmailDto.from_dict(alerting_email_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


