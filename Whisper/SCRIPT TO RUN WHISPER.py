#LINUX 
#THIS IS .ipynb FILE
%%bash
pip install git+https://github.com/openai/whisper.git 
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
sudo apt update &&
sudo apt install ffmpeg -y && pip install torch

#In second CODE shell.
import whisper
model = whisper.load_model("large")  #Model!…….
result = model.transcribe("my_file_name.mp3", task="translate", language="ml")
print(result["text"])

#Once runned this line "model = whisper.load_model("large")", no need to run it again, just run the line "result = model.transcribe("my_file_name.mp3", task="translate", language="ml")" ,to get the output need atleast 10 GB in GPU.
