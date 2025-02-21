# OpenshiftList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OpenshiftListDto]**](OpenshiftListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.openshift_list import OpenshiftList

# TODO update the JSON string below
json = "{}"
# create an instance of OpenshiftList from a JSON string
openshift_list_instance = OpenshiftList.from_json(json)
# print the JSON string representation of the object
print(OpenshiftList.to_json())

# convert the object into a dict
openshift_list_dict = openshift_list_instance.to_dict()
# create an instance of OpenshiftList from a dict
openshift_list_from_dict = OpenshiftList.from_dict(openshift_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


