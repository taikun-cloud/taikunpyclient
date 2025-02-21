# Ingresses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IngressDto]**](IngressDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.ingresses import Ingresses

# TODO update the JSON string below
json = "{}"
# create an instance of Ingresses from a JSON string
ingresses_instance = Ingresses.from_json(json)
# print the JSON string representation of the object
print(Ingresses.to_json())

# convert the object into a dict
ingresses_dict = ingresses_instance.to_dict()
# create an instance of Ingresses from a dict
ingresses_from_dict = Ingresses.from_dict(ingresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


