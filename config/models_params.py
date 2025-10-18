from scipy.stats import randint, uniform

LIGHTGM_PARAMS = {
    'n_estimators': randint(100, 500),          # Number of boosting rounds (trees) to build
    'max_depth': randint(5, 50),                # Maximum depth of the tree; controls model complexity
    'learning_rate': uniform(0.01, 0.2),        # Step size shrinkage used in update to prevent overfitting
    'num_leaves': randint(20, 100),             # Maximum number of leaves in one tree
    'boosting_type': ['gbdt', 'dart', 'goss']   # Type of boosting algorithm to use
}

RANDOM_SEARCH_PARAMS = {
    'n_iter': 4,              # Number of parameter settings sampled
    'cv': 2,                  # Number of cross-validation folds
    'n_jobs': -1,             # Number of jobs to run in parallel (-1 means using all processors)
    'verbose': 2,             # Controls the verbosity: the higher, the more messages
    'random_state': 42,       # Seed for reproducibility
    'scoring': 'accuracy'     # Evaluation metric for scoring the model
}