import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

# 1. Create dummy "Benign" data (Metadata: Duration, Memory, Request Rate)
# In a real scenario, you'd load your CSV here.
data = np.random.normal(loc=0.5, scale=0.1, size=(1000, 3)) 
df = pd.DataFrame(data, columns=['duration', 'memory', 'rate'])

# 2. Normalize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# 3. Build the Autoencoder Model
input_dim = scaled_data.shape[1]
input_layer = Input(shape=(input_dim,))
encoder = Dense(2, activation="relu")(input_layer) # Latent space
decoder = Dense(input_dim, activation="sigmoid")(encoder)
autoencoder = Model(inputs=input_layer, outputs=decoder)

autoencoder.compile(optimizer='adam', loss='mse')

# 4. Train on Benign data only
autoencoder.fit(scaled_data, scaled_data, epochs=50, batch_size=32, verbose=0)

# 5. Detection Logic
def detect_anomaly(new_request):
    scaled_request = scaler.transform([new_request])
    reconstruction = autoencoder.predict(scaled_request)
    loss = np.mean(np.square(scaled_request - reconstruction))
    
    threshold = 0.05 # Dynamic threshold
    return "ATTACK" if loss > threshold else "NORMAL"

# Test with a "Normal" vs "Attack" (extreme values)
print(f"Normal Check: {detect_anomaly([0.5, 0.5, 0.5])}")
print(f"Attack Check: {detect_anomaly([5.0, 9.0, 10.0])}")
