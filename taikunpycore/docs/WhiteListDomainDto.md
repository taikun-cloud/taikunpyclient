# WhiteListDomainDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from taikunpycore.models.white_list_domain_dto import WhiteListDomainDto

# TODO update the JSON string below
json = "{}"
# create an instance of WhiteListDomainDto from a JSON string
white_list_domain_dto_instance = WhiteListDomainDto.from_json(json)
# print the JSON string representation of the object
print(WhiteListDomainDto.to_json())

# convert the object into a dict
white_list_domain_dto_dict = white_list_domain_dto_instance.to_dict()
# create an instance of WhiteListDomainDto from a dict
white_list_domain_dto_from_dict = WhiteListDomainDto.from_dict(white_list_domain_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


