import numpy as np
from xgboost import XGBClassifier
from sklearn import datasets
from sklearn import model_selection

# 데이터 로드
# wdbc = datasets.load_breast_cancer()
# X, y = wdbc.data, wdbc.target

# torch.cuda.is_available()

# # 파라미터 그리드 설정
# param_grid = {
#     'n_estimators': [50, 100, 150, 200, 250],
#     'learning_rate': [0.01, 0.05, 0.1, 0.15, 0.2],
#     'max_depth': [3, 4, 5, 6, 7],
#     'min_child_weight': [1, 3, 5],
#     'subsample': [0.6, 0.8, 1.0],
#     'colsample_bytree': [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# }

# 교차 검증 설정
# kf = KFold(n_splits=5, shuffle=True, random_state=42)

# 모델 정의

# 교차 검증 수행
# cv_scores = []
# for train_idx, val_idx in kf.split(X):
#     X_train, X_val = X[train_idx], X[val_idx]
#     y_train, y_val = y[train_idx], y[val_idx]

#     # 모델 학습
#     model.fit(X_train, y_train)

#     # 예측 및 정확도 계산
#     preds = model.predict(X_val)
#     acc = accuracy_score(y_val, preds)
#     cv_scores.append(acc)

# # 평균 정확도 계산
# mean_cv_score = np.mean(cv_scores)
# print(f"CV Score: {mean_cv_score}")

if __name__ == "__main__":
    # Load a dataset
    wdbc = datasets.load_breast_cancer()

    # Train a model
    model = XGBClassifier(
        n_estimators=150,
        learning_rate=0.2,
        max_depth=4,
        min_child_weight=3,
        subsample=0.6,
        colsample_bytree=0.4,
        eval_metric="mlogloss",
    )

    cv_results = model_selection.cross_validate(
        model, wdbc.data, wdbc.target, cv=5, return_train_score=True
    )

    # Evaluate the model
    acc_train = np.mean(cv_results["train_score"])
    acc_test = np.mean(cv_results["test_score"])
    print(f"* Accuracy @ training data: {acc_train:.3f}")
    print(f"* Accuracy @ test data: {acc_test:.3f}")
    print(f"* Your score: {max(10 + 100 * (acc_test - 0.9), 0):.0f}")
