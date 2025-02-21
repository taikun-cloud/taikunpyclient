# ImportRepoCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.import_repo_command import ImportRepoCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ImportRepoCommand from a JSON string
import_repo_command_instance = ImportRepoCommand.from_json(json)
# print the JSON string representation of the object
print(ImportRepoCommand.to_json())

# convert the object into a dict
import_repo_command_dict = import_repo_command_instance.to_dict()
# create an instance of ImportRepoCommand from a dict
import_repo_command_from_dict = ImportRepoCommand.from_dict(import_repo_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


