# Pvcs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PvcDto]**](PvcDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.pvcs import Pvcs

# TODO update the JSON string below
json = "{}"
# create an instance of Pvcs from a JSON string
pvcs_instance = Pvcs.from_json(json)
# print the JSON string representation of the object
print(Pvcs.to_json())

# convert the object into a dict
pvcs_dict = pvcs_instance.to_dict()
# create an instance of Pvcs from a dict
pvcs_from_dict = Pvcs.from_dict(pvcs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


