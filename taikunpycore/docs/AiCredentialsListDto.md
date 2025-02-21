# AiCredentialsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**url** | **str** |  | 
**name** | **str** |  | 
**type** | [**AiType**](AiType.md) |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**is_default** | **bool** |  | 

## Example

```python
from taikunpycore.models.ai_credentials_list_dto import AiCredentialsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiCredentialsListDto from a JSON string
ai_credentials_list_dto_instance = AiCredentialsListDto.from_json(json)
# print the JSON string representation of the object
print(AiCredentialsListDto.to_json())

# convert the object into a dict
ai_credentials_list_dto_dict = ai_credentials_list_dto_instance.to_dict()
# create an instance of AiCredentialsListDto from a dict
ai_credentials_list_dto_from_dict = AiCredentialsListDto.from_dict(ai_credentials_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


