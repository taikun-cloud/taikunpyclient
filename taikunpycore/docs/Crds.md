# Crds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CrdListDto]**](CrdListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.crds import Crds

# TODO update the JSON string below
json = "{}"
# create an instance of Crds from a JSON string
crds_instance = Crds.from_json(json)
# print the JSON string representation of the object
print(Crds.to_json())

# convert the object into a dict
crds_dict = crds_instance.to_dict()
# create an instance of Crds from a dict
crds_from_dict = Crds.from_dict(crds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


