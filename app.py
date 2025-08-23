import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load model từ Hugging Face Hub
repo_id = "Thuan14/t5-finetuned-english-by-tnd"  # 👉 đổi thành repo của bạn
tokenizer = T5Tokenizer.from_pretrained(repo_id)
model = T5ForConditionalGeneration.from_pretrained(repo_id)

def chat(user_input):
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
    outputs = model.generate(
        inputs["input_ids"], 
        max_length=100, 
        num_beams=5, 
        early_stopping=True
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Giao diện Gradio
iface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(lines=2, placeholder="Nhập tin nhắn..."),
    outputs="text",
    title="T5 Finetuned English Chatbot",
    description="Chatbot fine-tuned từ T5, deploy bằng Render 🚀"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=8080)
