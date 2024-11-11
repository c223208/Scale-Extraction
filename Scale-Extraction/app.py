import librosa
import numpy as np
import json

def extract_f0(file_path):
    # 音声ファイルを読み込む
    y, sr = librosa.load(file_path)
    
    # ピッチを抽出
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    
    # 最も強いピッチを取得
    f0 = np.max(pitches)
    
    return f0