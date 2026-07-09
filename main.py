
import whisper

model = whisper.load_model("medium")
result = model.transcribe("part_01.webm")
print(result["text"])

