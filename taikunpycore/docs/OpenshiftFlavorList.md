# OpenshiftFlavorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OpenshiftFlavorData]**](OpenshiftFlavorData.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.openshift_flavor_list import OpenshiftFlavorList

# TODO update the JSON string below
json = "{}"
# create an instance of OpenshiftFlavorList from a JSON string
openshift_flavor_list_instance = OpenshiftFlavorList.from_json(json)
# print the JSON string representation of the object
print(OpenshiftFlavorList.to_json())

# convert the object into a dict
openshift_flavor_list_dict = openshift_flavor_list_instance.to_dict()
# create an instance of OpenshiftFlavorList from a dict
openshift_flavor_list_from_dict = OpenshiftFlavorList.from_dict(openshift_flavor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


