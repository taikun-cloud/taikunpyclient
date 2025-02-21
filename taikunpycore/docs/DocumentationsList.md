# DocumentationsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DocumentationData]**](DocumentationData.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.documentations_list import DocumentationsList

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentationsList from a JSON string
documentations_list_instance = DocumentationsList.from_json(json)
# print the JSON string representation of the object
print(DocumentationsList.to_json())

# convert the object into a dict
documentations_list_dict = documentations_list_instance.to_dict()
# create an instance of DocumentationsList from a dict
documentations_list_from_dict = DocumentationsList.from_dict(documentations_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


