# NodesSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NodeSearchResponseData]**](NodeSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.nodes_search_list import NodesSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of NodesSearchList from a JSON string
nodes_search_list_instance = NodesSearchList.from_json(json)
# print the JSON string representation of the object
print(NodesSearchList.to_json())

# convert the object into a dict
nodes_search_list_dict = nodes_search_list_instance.to_dict()
# create an instance of NodesSearchList from a dict
nodes_search_list_from_dict = NodesSearchList.from_dict(nodes_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


