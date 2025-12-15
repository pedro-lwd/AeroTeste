import matplotlib.pylab as plt
import pandas as pd 

def plot_time_series(
    df: pd.DataFrame,
    signal: str,
    steady_start_ms: int = 10000
) -> None:
    time_s = df["time_ms"] / 1000 # conversão para segundos
    plt.figure(figsize=(10,5))
    
    # sinal bruto
    plt.plot(time_s, df[signal], label=f"{signal} (raw)", alpha=0.5)
    
    #sinal suavizado
    smoothed_col = f"{signal}_smoothed"
    if smoothed_col in df.columns:
        plt.plot(time_s, df[smoothed_col], label=f"{signal} (smoothed), linewidth=3.5")
        
    
    # estacionariedade
    plt.axvline(
        x=steady_start_ms / 1000,
        color="black",
        linestyle="--",
        label="Steady-state-start/Inicio no estado estacionário"
    )
    plt.xlabel("Time [s]")
    plt.ylabel(signal.replace("_", " ").title())
    plt.title(f"{signal.replace('_', ' ').title()} Time History")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
