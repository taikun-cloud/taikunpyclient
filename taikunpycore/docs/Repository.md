# Repository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**kind** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**official** | **bool** |  | [optional] 
**repository_id** | **str** |  | [optional] 
**scanner_disabled** | **bool** |  | [optional] 
**is_imported** | **bool** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**verified_publisher** | **bool** |  | [optional] 
**organization_display_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.repository import Repository

# TODO update the JSON string below
json = "{}"
# create an instance of Repository from a JSON string
repository_instance = Repository.from_json(json)
# print the JSON string representation of the object
print(Repository.to_json())

# convert the object into a dict
repository_dict = repository_instance.to_dict()
# create an instance of Repository from a dict
repository_from_dict = Repository.from_dict(repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


