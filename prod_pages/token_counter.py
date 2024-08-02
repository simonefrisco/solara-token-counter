
from huggingface_hub import login
import solara
from transformers import AutoTokenizer, PretrainedConfig
import reacton.ipyvuetify as v
import tiktoken
from .sidebar import CustomSidebar
hf_token     = solara.reactive(''     )
use_hf_model = solara.reactive(False  )
llms = [
    "gpt-3.5-turbo",
]
current_llm  = solara.reactive(llms[0])
hf_token     = solara.reactive(''     )
use_hf_model = solara.reactive(False  )

def get_available_models():
    config_mappings = PretrainedConfig.pretrained_config_archive_map
    return list(config_mappings.keys())
    
@solara.component
def TokenCounter():
    print('hit TokenCounter() component')
    custom_text, set_custom_text = solara.use_state("Change this text ...")
    def hf_login():
        login(hf_token.value)
    def count_openai_token(text, model):
        encoding = tiktoken.encoding_for_model(model)
        tokens = encoding.encode(text)
        return tokens, len(tokens)
    
    CustomSidebar()
    
    with solara.Columns([3,3]):

        with solara.Column(style={'width':'100%'}):
            with solara.Card():
                solara.Markdown("""
                                # Token Counter
                                ### Usage:
                                Select LLM to use and paste any text in the following textbox : 
                            """)
            solara.Checkbox(label = 'Use HuggingFace Model', value=use_hf_model)
                
            if use_hf_model.value: 
                solara.InputText('HuggingFace Token', value=hf_token)
                solara.Button('login',on_click=hf_login)
            else:
                solara.Select(label="Food", value=current_llm, values=llms)

            # with solara.Card(style={'overflow-y':'scroll','position':'relative','min-height':'250px'}):
                # with v.Card(height=500, max_height=600 ) :
            with v.CardText():
                # solara.MarkdownEditor(value=custom_text, on_value=set_custom_text)
                solara.InputText(label='Text',value=custom_text, on_value=set_custom_text,)

        with solara.Column():
            solara.Markdown(f"""
                                ## Model :  
                                **{current_llm}**
                            
                            """)
            # model_list = get_available_models()
            # solara.Markdown(f'## Token counter for {model_list}')
            current_tokens, current_num_tokens = count_openai_token(custom_text, model = current_llm.value)

            solara.Markdown(f"""
                                ### Tokens: 
                                {current_tokens}

                                ### Number of tokens: 
                                {current_num_tokens}
                            """) 