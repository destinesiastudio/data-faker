import os
import gradio as gr
from uuid import UUID
from data_faker.anonymiser_manager import AnonymiserManager

# device = 0 if torch.cuda.is_available() else "cpu"

theme = gr.themes.Base(
    font=[gr.themes.GoogleFont('Libre Franklin'), gr.themes.GoogleFont('Public Sans'), 'system-ui', 'sans-serif'],
)

manager = AnonymiserManager()

def anonymise_text(id: UUID, input_text: str):
    if input_text is None:
        raise gr.Error("No text found! Please write something in the input box first.")

    if id == None:
        gr.Info('Using a new anonymiser instance')
    else:
        gr.Info(f'Running anonymise on existing instance ({id})')

    anon_text, id = manager.add(id, input_text)
    return id, anon_text

def deanonymise_text(id: UUID, input_text: str):
    if input_text is None:
        raise gr.Error("No text found! Please write something in the input box first.")

    if id == None:
        raise gr.Error("Unable to deanonymise without anonymising something first.")
    
    deanon_text = manager.revert(id, input_text)
    return deanon_text

def clear_instance(id: UUID):
    if id is None:
        raise gr.Error("No anonymising recorded yet, nothing to clear.")
    
    if manager.clear(id) == True:
        gr.Info(f'Anonymiser instance remove successfully ({id})')
    else:
        gr.Info(f'Anonymiser instance ({id}) cannot be found')

    return None, '', ''

with gr.Blocks() as text_to_text:
    state = gr.State()
    with gr.Row():
        with gr.Column(scale=1):
            input_text = gr.TextArea(label="Text to Convert", show_copy_button=True)
            with gr.Row():
                anon_btn = gr.Button("Generate Fake", variant="primary")
                denon_btn = gr.Button("Revert Fake", variant="primary")
        with gr.Column(scale=1):
            output_text = gr.TextArea(label="Output Text", show_copy_button=True)
            clear_btn = gr.Button("Reset")
        anon_btn.click(anonymise_text, inputs=[state, input_text], outputs=[state, output_text], concurrency_limit=4)
        denon_btn.click(deanonymise_text, inputs=[state, input_text], outputs=[output_text], concurrency_limit=4)
        clear_btn.click(clear_instance, inputs=[state], outputs=[state, input_text, output_text], concurrency_limit=4)

with gr.Blocks(title="Data Faker", theme=theme) as demo:
    gr.Markdown("""# Data Faker
        A crucial data faking tool before passing information to a language model like GPT-4 to help protect privacy and maintain confidentiality""")
    gr.TabbedInterface(
        [text_to_text],
        ["Text to Text"]
    )
    
if __name__ == "__main__":
    demo.queue(api_open=True).launch(show_api=True)