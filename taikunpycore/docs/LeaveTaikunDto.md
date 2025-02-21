# LeaveTaikunDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_intent_id** | **str** |  | [optional] 
**payment_client_secret** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.leave_taikun_dto import LeaveTaikunDto

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveTaikunDto from a JSON string
leave_taikun_dto_instance = LeaveTaikunDto.from_json(json)
# print the JSON string representation of the object
print(LeaveTaikunDto.to_json())

# convert the object into a dict
leave_taikun_dto_dict = leave_taikun_dto_instance.to_dict()
# create an instance of LeaveTaikunDto from a dict
leave_taikun_dto_from_dict = LeaveTaikunDto.from_dict(leave_taikun_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


