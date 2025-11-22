def select_candidates_by_data(models, names, data_size, thresholds):
    eligible, eligible_names = [], []
    for model, name in zip(models, names):
        min_data = thresholds.get(name, 0)
        if data_size >= min_data:
            eligible.append(model)
            eligible_names.append(name)
    return eligible, eligible_names