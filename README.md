# solara-token-counter


## Setup Enviroment

- setup conda env with python = 3.10

```
conda create -n llm-ui python=3.10
conda activate llm-ui
pip install -r requirements.txt
```


# LlamaIndex Useful tips

## Documents

- Exclude LLM from reading metadata specific fields (1)[https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/#advanced-metadata-customization]:

```python
document.excluded_llm_metadata_keys = ["file_name"]
document.excluded_embed_metadata_keys = ["file_name"]
```

- How to sent metadata to LLM (2)[https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/#customizing-metadata-format] :
1. Document.metadata_seperator -> default = "\n"
2. Document.metadata_template -> default = "{key}: {value}"
3. Document.text_template -> default = {metadata_str}\n\n{content}