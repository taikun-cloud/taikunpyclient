# AlertData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[Group]**](Group.md) |  | [optional] 

## Example

```python
from taikunpycore.models.alert_data import AlertData

# TODO update the JSON string below
json = "{}"
# create an instance of AlertData from a JSON string
alert_data_instance = AlertData.from_json(json)
# print the JSON string representation of the object
print(AlertData.to_json())

# convert the object into a dict
alert_data_dict = alert_data_instance.to_dict()
# create an instance of AlertData from a dict
alert_data_from_dict = AlertData.from_dict(alert_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


