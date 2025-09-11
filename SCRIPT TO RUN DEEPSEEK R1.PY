!pip install -q bitsandbytes accelerate transformers #FIRST SHELL
#SECOND SHELL
!apt -qq install git-lfs
!git lfs install
!git clone https://huggingface.co/Amar-89/DeepSeek-R1-Distill-Llama-8B-8bit
#THIRD SHELL
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline

model_name = "./DeepSeek-R1-Distill-Llama-8B-8bit"

bnb_config = BitsAndBytesConfig(load_in_8bit=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto"
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

def deepthink(prompt_text):
    deepthink_prompt = (
        "You are a deeply reasoning assistant. Think step by step, explain your reasoning, show your thought process.\n"
        + prompt_text
    )
    output = pipe(
        deepthink_prompt,
        max_new_tokens=1024,     # increase as per your GPU allows
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        do_sample=True
    )
    return output[0]["generated_text"]

# Example usage
question = "QUESTION?"
print(deepthink(question))


