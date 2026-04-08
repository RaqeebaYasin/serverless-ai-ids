import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

# --- 1. Simulation of Serverless Metadata ---
# Features: [Duration(ms), MemoryUsage(MB), RequestRate(req/sec)]
def generate_mock_data():
    # Normal traffic: Low duration, steady memory, low request rate
    benign = np.random.normal(loc=[100, 128, 1], scale=[10, 5, 0.2], size=(1000, 3))
    
    # Attack traffic: High duration (Injection) or High Rate (DDoS/DoW)
    attacks = np.array([
        [5000, 512, 1],   # Possible Injection (Long execution)
        [120, 130, 50],   # Possible DDoS (High frequency)
        [150, 400, 2]     # Possible Memory Leak/Injection
    ])
    return benign, attacks

# --- 2. Preprocessing ---
benign_data, attack_samples = generate_mock_data()
scaler = MinMaxScaler()
scaler.fit(benign_data)
X_train = scaler.transform(benign_data)

# --- 3. Autoencoder Architecture (As described in the Research Paper) ---
input_dim = X_train.shape[1]
input_layer = Input(shape=(input_dim,))

# Encoder
encoder = Dense(2, activation="relu")(input_layer) 
# Decoder
decoder = Dense(input_dim, activation="sigmoid")(encoder)

autoencoder = Model(inputs=input_layer, outputs=decoder)
autoencoder.compile(optimizer='adam', loss='mse')

# --- 4. Training on Benign Traffic Only ---
# This establishes the "Behavioral Baseline"
print("Establishing behavioral baseline...")
autoencoder.fit(X_train, X_train, epochs=20, batch_size=16, verbose=0)

# --- 5. Anomaly Detection Logic ---
def predict_threat(sample):
    scaled_sample = scaler.transform([sample])
    reconstruction = autoencoder.predict(scaled_sample)
    mse = np.mean(np.square(scaled_sample - reconstruction))
    
    # Threshold for Denial-of-Wallet / Injection
    threshold = 0.02 
    return "MALICIOUS (Threat Detected)" if mse > threshold else "BENIGN (Safe)"

# --- 6. Results ---
print("\n--- Real-time Analysis Result ---")
print(f"Normal Request: {predict_threat([105, 125, 1.1])}")
print(f"Attack Request (DoW): {predict_threat([120, 130, 80.0])}")
