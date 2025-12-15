from dataset_reader import preprocess_data
from dataset_metrics import compute_all_metrics
from visualization import plot_time_series

if __name__ == "__main__":
    df = preprocess_data("test_001.csv")

    metrics = compute_all_metrics(df)
    print(metrics)

    for signal in ["air_speed", "pressure", "downforce"]:
        plot_time_series(df, signal)
