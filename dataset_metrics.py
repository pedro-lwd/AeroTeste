import pandas as pd

def compute_global_metrics(df: pd.DataFrame) -> dict:
    metrics = {}
    
    signals = ["air_speed", "pressure", "downforce"]
    
    for signal in signals:
        metrics[signal] = {
            "mean": df[signal].mean(), # média do sinal
            "max": df[signal].max(), # máxima do sinal
            "std": df[signal].std() # desvio padrão
        }
        
    return metrics


# estado estacionario (parado ou em equilibrio)
def compute_steady_state_metrics(
    df: pd.DataFrame,
    steady_start_ms: int = 10000
) -> dict:
    steady_df = df[df["time_ms"] >=steady_start_ms]
    
    metrics = {
        "downforce_mean_steady": steady_df["downforce"].mean(), # media da força descendente em estado estacionario
        "downforce_std_steady": steady_df["downforce"].std()    # desvio da força descendente em estado estacionario
    }
    
    return metrics



def compute_all_metrics(df: pd.DataFrame) -> dict:
    metrics = {}
    
    
    metrics["global"] = compute_global_metrics(df)
    metrics["steady_state"] = compute_steady_state_metrics(df)
    
    return metrics


if __name__ == "__main__":
    
    from dataset_reader import preprocess_data
    
    df = preprocess_data("test_001.csv")
    metrics = compute_all_metrics(df)
    
    for category, values in metrics.items():
        print(f"\n{category.upper()}")
        for key,value in values.items():
            print(f"\n{key}: {value}")