
from huggingface_hub import login
import solara
from transformers import AutoTokenizer, PretrainedConfig
import reacton.ipyvuetify as v
import tiktoken
from .sidebar import CustomSidebar
# from llama_index import SimpleTextSplitter, ParagraphSplitter

from langchain_text_splitters  import CharacterTextSplitter, RecursiveCharacterTextSplitter,TokenTextSplitter

llms = [
    "gpt-3.5-turbo",
]
current_llm  = solara.reactive(llms[0])

chunk_splitters = {
    "CharacterTextSplitter": CharacterTextSplitter,
    "RecursiveCharacterTextSplitter": RecursiveCharacterTextSplitter,
    "TokenTextSplitter": TokenTextSplitter,
}

input_text = solara.reactive("")
chunk_size = solara.reactive(1000)
chunk_overlap = solara.reactive(100)
selected_splitter = solara.reactive("CharacterTextSplitter")
output_chunks = solara.reactive([])

@solara.component
def ChunkViewer():


    def process_text():
        splitter_class = chunk_splitters[selected_splitter.value]
        splitter = splitter_class(chunk_size=chunk_size.value, chunk_overlap=chunk_overlap.value)  # Example parameter
        output_chunks.value = splitter.create_documents([input_text.value])


    with solara.Columns([3,3]):
        with solara.Column(style={'width':'100%'}):

            solara.Markdown("## Chunk Splitter Test")
            solara.InputText("Input Text", value=input_text)
            solara.InputText("Chunk Size", value=chunk_size)
            solara.InputText("Chunk Overlap", value=chunk_overlap)
            solara.Select("Select Chunk Type", values=list(chunk_splitters.keys()), value=selected_splitter)
            solara.Button("Process", on_click=process_text)

        with solara.Column(style={'width':'100%'}):
            if output_chunks.value:
                solara.Markdown("## Output Chunks")
                for chunk in output_chunks.value:
                    with solara.Card():
                        solara.Text(chunk.page_content)
                        with solara.CardActions():
                            solara.Text(str(chunk.metadata))
