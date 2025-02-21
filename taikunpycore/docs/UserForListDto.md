# UserForListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | 
**organization_name** | **str** |  | 
**has_customer_id** | **bool** |  | 
**has_payment_method** | **bool** |  | 
**organization_id** | **int** |  | 
**role** | [**UserRole**](UserRole.md) |  | 
**role_name** | **str** |  | [optional] 
**email** | **str** |  | 
**display_name** | **str** |  | 
**created_at** | **str** |  | 
**created** | **datetime** |  | [optional] 
**is_email_confirmed** | **bool** |  | 
**is_email_notification_enabled** | **bool** |  | 
**is_forced_to_reset_password** | **bool** |  | 
**is_csm** | **bool** |  | 
**is_eligible_update_subscription** | **bool** |  | 
**is_locked** | **bool** |  | 
**is_approved_by_partner** | **bool** |  | 
**owner** | **bool** |  | 
**is_read_only** | **bool** |  | 
**has_repo** | **bool** |  | 
**is_new_organization** | **bool** |  | 
**is2_fa_enabled** | **bool** |  | 
**last_login_at** | **str** |  | 
**bound_projects** | [**List[ProjectDto]**](ProjectDto.md) |  | 
**partner** | [**PartnerDetailsForUserDto**](PartnerDetailsForUserDto.md) |  | 

## Example

```python
from taikunpycore.models.user_for_list_dto import UserForListDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserForListDto from a JSON string
user_for_list_dto_instance = UserForListDto.from_json(json)
# print the JSON string representation of the object
print(UserForListDto.to_json())

# convert the object into a dict
user_for_list_dto_dict = user_for_list_dto_instance.to_dict()
# create an instance of UserForListDto from a dict
user_for_list_dto_from_dict = UserForListDto.from_dict(user_for_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


