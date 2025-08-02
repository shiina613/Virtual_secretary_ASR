import torch
import torchaudio
import librosa
import pandas as pd
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
from jiwer import wer, cer
from tqdm import tqdm
import time

# Cấu hình thiết bị
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model PhoWhisper của VinAI
model_id = "vinai/PhoWhisper-medium"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id).to(device)

# Đọc danh sách dữ liệu
df = pd.read_csv("test.tsv", sep="\t")

results = []

for i, row in tqdm(df.iterrows(), total=len(df), desc="Đang đánh giá PhoWhisper VinAI"):
    audio_path = row["path"]
    ground_truth = row["sentence"].strip()

    try:
        # Bắt đầu đo thời gian
        start_time = time.time()

        # Load audio và chuẩn hóa
        speech, sr = torchaudio.load(audio_path)
        if sr != 16000:
            speech = torchaudio.functional.resample(speech, sr, 16000)
        speech = speech.squeeze().numpy()

        # Xử lý đầu vào
        inputs = processor(speech, sampling_rate=16000, return_tensors="pt").to(device)
        generated_ids = model.generate(inputs["input_features"])

        # Dự đoán transcript
        transcript = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

        # Tính thời gian & tốc độ
        end_time = time.time()
        audio_duration = len(speech) / 16000.0
        rtf = (end_time - start_time) / audio_duration

        # Tính CER, WER
        wer_score = wer(ground_truth, transcript)
        cer_score = cer(ground_truth, transcript)

        results.append({
            "path": audio_path,
            "original_text": ground_truth,
            "transcript": transcript,
            "WER": wer_score,
            "CER": cer_score,
            "RTF": rtf
        })

    except Exception as e:
        print(f"[LỖI] {audio_path} - {e}")

# Ghi kết quả ra file Excel
df_result = pd.DataFrame(results)
df_result.to_excel("vinai_phowhisper_medium_evaluation.xlsx", index=False)
print("\n✅ Hoàn tất! Kết quả đã lưu: vinai_phowhisper_medium_evaluation.xlsx")
