# PartnersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PartnerDetailsDto]**](PartnerDetailsDto.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.partners_list import PartnersList

# TODO update the JSON string below
json = "{}"
# create an instance of PartnersList from a JSON string
partners_list_instance = PartnersList.from_json(json)
# print the JSON string representation of the object
print(PartnersList.to_json())

# convert the object into a dict
partners_list_dict = partners_list_instance.to_dict()
# create an instance of PartnersList from a dict
partners_list_from_dict = PartnersList.from_dict(partners_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


