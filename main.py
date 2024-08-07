

from huggingface_hub import login
import solara
from transformers import AutoTokenizer
from transformers import PretrainedConfig
import reacton.ipyvuetify as v
import tiktoken
from prod_pages.token_counter import TokenCounter
from prod_pages.chunk_viewer import ChunkViewer

# reactive variables will trigger a component rerender
# when changed.
# When you change the default (now 0), hit the embedded browser
# refresh button to reset the state

routes = [
    solara.Route(path="/", component=TokenCounter, label="Token Counter"),
    solara.Route(path="about", component=ChunkViewer, label="Chunk Viewer"),
]