# TransferList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**user_name** | **str** |  | 
**role** | [**UserRole**](UserRole.md) |  | 

## Example

```python
from taikunpycore.models.transfer_list import TransferList

# TODO update the JSON string below
json = "{}"
# create an instance of TransferList from a JSON string
transfer_list_instance = TransferList.from_json(json)
# print the JSON string representation of the object
print(TransferList.to_json())

# convert the object into a dict
transfer_list_dict = transfer_list_instance.to_dict()
# create an instance of TransferList from a dict
transfer_list_from_dict = TransferList.from_dict(transfer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


