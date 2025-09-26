import gradio as gr

def hello(name):
    return f"Bonjour {name} 👋 !"

demo = gr.Interface(
    fn=hello,
    inputs="text",
    outputs="text",
    title="Test Gradio"
)
