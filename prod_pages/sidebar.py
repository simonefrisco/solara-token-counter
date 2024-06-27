
import solara

@solara.component
def CustomSidebar():
    with solara.Sidebar():
        with solara.Link("/"):
            solara.Button("Token Counter",style={'width':'100%', 'align':'start'})
            
        if use_hf_model.value: 
            solara.InputText('HuggingFace Token', value=hf_token)
            solara.Button('login',on_click=hf_login)
        
        solara.Checkbox(label = 'Use HuggingFace Model', value=use_hf_model)