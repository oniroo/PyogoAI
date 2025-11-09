from timeseries_classifier import LSTMClassifier, TransformerClassifier

def build_timeseries_model(base, selected, num_classes, input_size=10):
    if base == "LSTM":
        return LSTMClassifier(input_size=input_size, hidden_size=64, num_layers=2, num_classes=num_classes)
    elif base == "Transformer":
        return TransformerClassifier(input_size=input_size, d_model=64, nhead=8, num_layers=2, num_classes=num_classes)
    else:
        raise ValueError(f"Unsupported timeseries base: {base}")