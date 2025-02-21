# IngressDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**hosts** | **str** |  | 
**namespace** | **str** |  | 
**age** | **str** |  | 

## Example

```python
from taikunpycore.models.ingress_dto import IngressDto

# TODO update the JSON string below
json = "{}"
# create an instance of IngressDto from a JSON string
ingress_dto_instance = IngressDto.from_json(json)
# print the JSON string representation of the object
print(IngressDto.to_json())

# convert the object into a dict
ingress_dto_dict = ingress_dto_instance.to_dict()
# create an instance of IngressDto from a dict
ingress_dto_from_dict = IngressDto.from_dict(ingress_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


