# OpenshiftFlavorData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cpu** | **int** |  | 
**ram** | **float** |  | 

## Example

```python
from taikunpycore.models.openshift_flavor_data import OpenshiftFlavorData

# TODO update the JSON string below
json = "{}"
# create an instance of OpenshiftFlavorData from a JSON string
openshift_flavor_data_instance = OpenshiftFlavorData.from_json(json)
# print the JSON string representation of the object
print(OpenshiftFlavorData.to_json())

# convert the object into a dict
openshift_flavor_data_dict = openshift_flavor_data_instance.to_dict()
# create an instance of OpenshiftFlavorData from a dict
openshift_flavor_data_from_dict = OpenshiftFlavorData.from_dict(openshift_flavor_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


