# PartnerEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **int** |  | [optional] 
**partner_name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.partner_entity import PartnerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerEntity from a JSON string
partner_entity_instance = PartnerEntity.from_json(json)
# print the JSON string representation of the object
print(PartnerEntity.to_json())

# convert the object into a dict
partner_entity_dict = partner_entity_instance.to_dict()
# create an instance of PartnerEntity from a dict
partner_entity_from_dict = PartnerEntity.from_dict(partner_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


