# PublicImageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.public_image_list import PublicImageList

# TODO update the JSON string below
json = "{}"
# create an instance of PublicImageList from a JSON string
public_image_list_instance = PublicImageList.from_json(json)
# print the JSON string representation of the object
print(PublicImageList.to_json())

# convert the object into a dict
public_image_list_dict = public_image_list_instance.to_dict()
# create an instance of PublicImageList from a dict
public_image_list_from_dict = PublicImageList.from_dict(public_image_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


