# InfraProductDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**price_id** | **str** |  | [optional] 
**yearly_price_id** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.infra_product_dto import InfraProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of InfraProductDto from a JSON string
infra_product_dto_instance = InfraProductDto.from_json(json)
# print the JSON string representation of the object
print(InfraProductDto.to_json())

# convert the object into a dict
infra_product_dto_dict = infra_product_dto_instance.to_dict()
# create an instance of InfraProductDto from a dict
infra_product_dto_from_dict = InfraProductDto.from_dict(infra_product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


