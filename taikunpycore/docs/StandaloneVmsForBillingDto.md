# StandaloneVmsForBillingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** |  | 
**ram** | **int** |  | 

## Example

```python
from taikunpycore.models.standalone_vms_for_billing_dto import StandaloneVmsForBillingDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneVmsForBillingDto from a JSON string
standalone_vms_for_billing_dto_instance = StandaloneVmsForBillingDto.from_json(json)
# print the JSON string representation of the object
print(StandaloneVmsForBillingDto.to_json())

# convert the object into a dict
standalone_vms_for_billing_dto_dict = standalone_vms_for_billing_dto_instance.to_dict()
# create an instance of StandaloneVmsForBillingDto from a dict
standalone_vms_for_billing_dto_from_dict = StandaloneVmsForBillingDto.from_dict(standalone_vms_for_billing_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


