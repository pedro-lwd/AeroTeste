import pandas as pd


def load_exdata(csv_path: str) -> pd.DataFrame:
    
    df = pd.read_csv(csv_path)
    
    required_columns = {"time_ms", "air_speed", "pressure", "downforce"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"Missing required columns: {missing}// Coluna(s) necessárias ausentes")
    
    
    # esquema pra organizar pelo tempo
    df = df.sort_values("time_ms").reset_index(drop=True)
    return df


def inspect_data(df: pd.DataFrame) -> None:
    
    print("Dataset info//informações do Dataset:")
    print(df.info())
    print(f"\nMissing values:")
    print(df.isnull().sum)


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.interpolate(method="linear", inplace=True)
    return df
# a interpolação linear nessa caso funciona de uma forma mais tranquila visto que pequenos erros são permitidos
# os sensores também variam bastante então é bom ser feito dessa forma


# suavizar o sinal, fazendo a media movel
def apply_moving_avarage(
    df: pd.DataFrame,
    window_size: int = 10 # 100hz = 0,1 segundos
    ) -> pd.DataFrame:
    df = df.copy()
    
    signals =  ["air_speed", "pressure", "downforce"]
    
    for signal in signals:
        df[f"{signal}_smoothed"] = (
            df[signal]
            .rolling(window=window_size, center=True)
            .mean()
        )
    return df
        # ruido sem distorção do sinal, normalmente utilizado de uma forma mais complexa
        

def preprocess_data(csv_path : str) -> pd.DataFrame:
    """
    Docstring for preprocess_data
    
    :param csv_path: path
    :type csv_path: str
    :return: pipeline de preprocesso da informação
    :rtype: DataFrame
    """
    df = load_exdata(csv_path)
    inspect_data(df)
    df = handle_missing_values(df)
    df = apply_moving_avarage(df)
    return df
    

if __name__ == "__main__":
    df_processed= preprocess_data("test_001.csv")
    print(df_processed)


