import librosa
import numpy as np

def extract_features(file_path):
    try:
        audio, sample_rate = librosa.load(file_path, sr=None)

        # 🔹 Basic features
        chroma_stft = np.mean(librosa.feature.chroma_stft(y=audio, sr=sample_rate))
        rms = np.mean(librosa.feature.rms(y=audio))
        spec_cent = np.mean(librosa.feature.spectral_centroid(y=audio, sr=sample_rate))
        spec_bw = np.mean(librosa.feature.spectral_bandwidth(y=audio, sr=sample_rate))
        rolloff = np.mean(librosa.feature.spectral_rolloff(y=audio, sr=sample_rate))
        zcr = np.mean(librosa.feature.zero_crossing_rate(audio))

        # 🔹 MFCC (20 features)
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=20)
        mfccs_mean = np.mean(mfccs.T, axis=0)

        # 🔹 Combine all → TOTAL 26
        features = np.hstack([
            chroma_stft,
            rms,
            spec_cent,
            spec_bw,
            rolloff,
            zcr,
            mfccs_mean
        ])

        return features

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None