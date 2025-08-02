"""
Script tạo file dataset mẫu
Tạo file CSV với cấu trúc: audio_path, ground_truth
"""

import pandas as pd
import os

def create_sample_dataset():
    """
    Tạo file dataset mẫu với cấu trúc cần thiết
    """
    # Dữ liệu mẫu - thay thế bằng dữ liệu thực của bạn
    sample_data = [
        {
            'audio_path': '/path/to/audio1.wav',
            'ground_truth': 'Xin chào, tôi là trợ lý ảo của bạn.'
        },
        {
            'audio_path': '/path/to/audio2.wav', 
            'ground_truth': 'Hôm nay thời tiết rất đẹp.'
        },
        {
            'audio_path': '/path/to/audio3.wav',
            'ground_truth': 'Tôi đang học về trí tuệ nhân tạo.'
        }
    ]
    
    # Tạo DataFrame
    df = pd.DataFrame(sample_data)
    
    # Xuất ra CSV
    df.to_csv('dataset.csv', index=False, encoding='utf-8')
    print("Đã tạo file dataset.csv mẫu")
    print("Cấu trúc file:")
    print(df.head())
    print("\nVui lòng thay thế bằng dữ liệu thực của bạn!")

if __name__ == "__main__":
    create_sample_dataset()
