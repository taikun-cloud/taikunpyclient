# HelmCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.helm_condition import HelmCondition

# TODO update the JSON string below
json = "{}"
# create an instance of HelmCondition from a JSON string
helm_condition_instance = HelmCondition.from_json(json)
# print the JSON string representation of the object
print(HelmCondition.to_json())

# convert the object into a dict
helm_condition_dict = helm_condition_instance.to_dict()
# create an instance of HelmCondition from a dict
helm_condition_from_dict = HelmCondition.from_dict(helm_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


