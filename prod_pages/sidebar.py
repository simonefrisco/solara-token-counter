from huggingface_hub import login

import solara



@solara.component
def CustomSidebar():

    with solara.Sidebar():
        with solara.Link("/"):
            solara.Button("Token Counter",style={'width':'100%', 'align':'start'})
            
