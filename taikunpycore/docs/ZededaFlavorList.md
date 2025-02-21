# ZededaFlavorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProxmoxFlavorData]**](ProxmoxFlavorData.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.zededa_flavor_list import ZededaFlavorList

# TODO update the JSON string below
json = "{}"
# create an instance of ZededaFlavorList from a JSON string
zededa_flavor_list_instance = ZededaFlavorList.from_json(json)
# print the JSON string representation of the object
print(ZededaFlavorList.to_json())

# convert the object into a dict
zededa_flavor_list_dict = zededa_flavor_list_instance.to_dict()
# create an instance of ZededaFlavorList from a dict
zededa_flavor_list_from_dict = ZededaFlavorList.from_dict(zededa_flavor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


