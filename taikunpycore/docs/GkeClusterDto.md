# GkeClusterDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.gke_cluster_dto import GkeClusterDto

# TODO update the JSON string below
json = "{}"
# create an instance of GkeClusterDto from a JSON string
gke_cluster_dto_instance = GkeClusterDto.from_json(json)
# print the JSON string representation of the object
print(GkeClusterDto.to_json())

# convert the object into a dict
gke_cluster_dto_dict = gke_cluster_dto_instance.to_dict()
# create an instance of GkeClusterDto from a dict
gke_cluster_dto_from_dict = GkeClusterDto.from_dict(gke_cluster_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


