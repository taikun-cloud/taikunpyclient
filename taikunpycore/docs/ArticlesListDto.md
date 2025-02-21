# ArticlesListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_name** | **str** |  | 
**is_csm** | **bool** |  | 
**create_at** | **str** |  | 
**body** | **str** |  | 
**message_id** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from taikunpycore.models.articles_list_dto import ArticlesListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ArticlesListDto from a JSON string
articles_list_dto_instance = ArticlesListDto.from_json(json)
# print the JSON string representation of the object
print(ArticlesListDto.to_json())

# convert the object into a dict
articles_list_dto_dict = articles_list_dto_instance.to_dict()
# create an instance of ArticlesListDto from a dict
articles_list_dto_from_dict = ArticlesListDto.from_dict(articles_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


