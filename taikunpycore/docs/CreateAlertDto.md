# CreateAlertDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[KubernetesAlertCreateDto]**](KubernetesAlertCreateDto.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_alert_dto import CreateAlertDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlertDto from a JSON string
create_alert_dto_instance = CreateAlertDto.from_json(json)
# print the JSON string representation of the object
print(CreateAlertDto.to_json())

# convert the object into a dict
create_alert_dto_dict = create_alert_dto_instance.to_dict()
# create an instance of CreateAlertDto from a dict
create_alert_dto_from_dict = CreateAlertDto.from_dict(create_alert_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


