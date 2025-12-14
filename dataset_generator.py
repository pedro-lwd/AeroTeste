import numpy as np
import pandas as pd


# conf// mude para o que quiser

duration_s = 60
sampling_rate = 100 # hz
num_samples = duration_s * sampling_rate

time_ms = np.linspace(0, duration_s * 1000, num_samples)

# velocidade do ar (estabilização com o ramp-up [no caso vai ser a melhora no desempenho])

air_speed = np.minimum(
    50,
    50 * (time_ms/1000)
)
air_speed += np.random.normal(0,0.5, num_samples)

# pressão 

pressure = 0.5* 1.225 * air_speed**2
pressure += np.random.normal(0, 5, num_samples)

# força descendente ou downforce que é o quadrado da velocidade no ar
downforce = -30 * air_speed**2
downforce += np.random.normal(0, 50, num_samples)

df = pd.DataFrame({
    "time_ms": time_ms.astype(int),
    "air_speed": air_speed,
    "pressure": pressure,
    "downforce": downforce
})

df.to_csv("test_001.csv", index=False)