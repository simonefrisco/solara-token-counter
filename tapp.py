
#%% []
from llama_index.core import Document

document = Document.example()

#%% []
print(document.__doc__)
# %%
print(document.id_)
# %%
print(document.as_related_node_info())
#%% []
print(document.metadata)
# %%
print(document.embedding)
# %%
print(document.get_content())
# %%
document.dict()
# %%
