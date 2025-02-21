# ArticleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArticlesListDto]**](ArticlesListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.article_list import ArticleList

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleList from a JSON string
article_list_instance = ArticleList.from_json(json)
# print the JSON string representation of the object
print(ArticleList.to_json())

# convert the object into a dict
article_list_dict = article_list_instance.to_dict()
# create an instance of ArticleList from a dict
article_list_from_dict = ArticleList.from_dict(article_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


