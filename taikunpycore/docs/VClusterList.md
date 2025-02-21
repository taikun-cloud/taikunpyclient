# VClusterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VClusterListDto]**](VClusterListDto.md) |  | 
**total_count** | **int** |  | 
**project** | [**ProjectDetailsForVmsDto**](ProjectDetailsForVmsDto.md) |  | 

## Example

```python
from taikunpycore.models.v_cluster_list import VClusterList

# TODO update the JSON string below
json = "{}"
# create an instance of VClusterList from a JSON string
v_cluster_list_instance = VClusterList.from_json(json)
# print the JSON string representation of the object
print(VClusterList.to_json())

# convert the object into a dict
v_cluster_list_dict = v_cluster_list_instance.to_dict()
# create an instance of VClusterList from a dict
v_cluster_list_from_dict = VClusterList.from_dict(v_cluster_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


