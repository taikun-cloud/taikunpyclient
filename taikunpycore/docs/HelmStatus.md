# HelmStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[HelmCondition]**](HelmCondition.md) |  | [optional] 
**failures** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.helm_status import HelmStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HelmStatus from a JSON string
helm_status_instance = HelmStatus.from_json(json)
# print the JSON string representation of the object
print(HelmStatus.to_json())

# convert the object into a dict
helm_status_dict = helm_status_instance.to_dict()
# create an instance of HelmStatus from a dict
helm_status_from_dict = HelmStatus.from_dict(helm_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


