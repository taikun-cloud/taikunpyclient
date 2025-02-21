# DocumentationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.documentation_data import DocumentationData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentationData from a JSON string
documentation_data_instance = DocumentationData.from_json(json)
# print the JSON string representation of the object
print(DocumentationData.to_json())

# convert the object into a dict
documentation_data_dict = documentation_data_instance.to_dict()
# create an instance of DocumentationData from a dict
documentation_data_from_dict = DocumentationData.from_dict(documentation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


