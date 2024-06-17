
#%% []
from llama_index.core.node_parser import (
    SentenceSplitter,
    SemanticSplitterNodeParser,
)
from llama_index.embeddings.openai import OpenAIEmbedding

from dotenv import load_dotenv
load_dotenv()
#%% []

from llama_index.core import SimpleDirectoryReader

# load documents
documents = SimpleDirectoryReader(input_dir='./knowledge_base').load_data()

# also baseline splitter
base_splitter = SentenceSplitter(chunk_size=512)

nodes = base_splitter.get_nodes_from_documents(documents)


#%% []
print(nodes[1].get_content())

# %%
nodes[1].dict()
# %%
nodes[2].dict()

# %%
nodes[20].dict()

# %%
nodes[21].dict()

# %%
nodes[22].dict()

# %%
nodes[58].dict()

# %%
nodes[57].dict()

# %%
