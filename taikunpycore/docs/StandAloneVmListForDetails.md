# StandAloneVmListForDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StandaloneVmsListForDetailsDto]**](StandaloneVmsListForDetailsDto.md) |  | 
**project** | [**ProjectDetailsForVmsDto**](ProjectDetailsForVmsDto.md) |  | 

## Example

```python
from taikunpycore.models.stand_alone_vm_list_for_details import StandAloneVmListForDetails

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneVmListForDetails from a JSON string
stand_alone_vm_list_for_details_instance = StandAloneVmListForDetails.from_json(json)
# print the JSON string representation of the object
print(StandAloneVmListForDetails.to_json())

# convert the object into a dict
stand_alone_vm_list_for_details_dict = stand_alone_vm_list_for_details_instance.to_dict()
# create an instance of StandAloneVmListForDetails from a dict
stand_alone_vm_list_for_details_from_dict = StandAloneVmListForDetails.from_dict(stand_alone_vm_list_for_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


