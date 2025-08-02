import whisper
import torchaudio
import torch
import os
import pandas as pd
from jiwer import wer, cer
from tqdm import tqdm
import time

# Load model
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("large", device=device)

# Load test file
df = pd.read_csv("test.tsv", sep="\t")
results = []

for i, row in tqdm(df.iterrows(), total=len(df), desc="Đang xử lý"):
    audio_path = row['path']
    ground_truth = row['sentence']

    try:
        # Đo thời gian bắt đầu
        start_time = time.time()

        # Tải và chuẩn hóa âm thanh
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(device)

        # Dịch với ngôn ngữ tiếng Việt
        options = whisper.DecodingOptions(language="vi", fp16=torch.cuda.is_available())
        result = whisper.decode(model, mel, options)

        # Đo thời gian kết thúc
        end_time = time.time()
        duration = audio.shape[0] / whisper.audio.SAMPLE_RATE
        rtf = (end_time - start_time) / duration

        # Tính WER & CER
        pred = result.text.strip()
        ref = ground_truth.strip()
        result_wer = wer(ref, pred)
        result_cer = cer(ref, pred)

        results.append({
            "path": audio_path,
            "original_text": ref,
            "transcript": pred,
            "WER": result_wer,
            "CER": result_cer,
            "RTF": rtf
        })

    except Exception as e:
        print(f"[LỖI] File: {audio_path} -> {e}")

# Ghi kết quả ra Excel
df_result = pd.DataFrame(results)
df_result.to_excel("whisper_medium_vi_evaluation.xlsx", index=False)
print("\n✅ Hoàn tất! Kết quả đã lưu vào: whisper_medium_vi_evaluation.xlsx")
