"""
modelling.py - MLflow Project Entry Point
Supports CLI arguments for automated training via GitHub Actions CI

Perubahan dari versi original:
1. Menambahkan argparse untuk CLI arguments
2. Menghapus hardcoded tracking URI agar compatible dengan GitHub Actions
3. Parameter n_estimators dan max_depth dapat dikonfigurasi
"""

import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report, accuracy_score, 
    precision_score, recall_score, f1_score
)
import mlflow
import mlflow.sklearn

def parse_args():
    """Parse command line arguments sesuai dengan MLProject entry_points"""
    parser = argparse.ArgumentParser(description="Train Random Forest for Telco Churn")
    parser.add_argument("--n_estimators", type=int, default=100, 
                        help="Number of trees in the forest")
    parser.add_argument("--max_depth", type=int, default=10, 
                        help="Maximum depth of the tree (0 = unlimited)")
    parser.add_argument("--data_path", type=str, default="preprocessed_data.csv",
                        help="Path to preprocessed data CSV")
    return parser.parse_args()

def main():
    # Parse arguments dari command line
    args = parse_args()
    
    print("=" * 50)
    print("TELCO CHURN MODEL TRAINING - CI PIPELINE")
    print("=" * 50)
    print(f"n_estimators: {args.n_estimators}")
    print(f"max_depth: {args.max_depth}")
    print(f"data_path: {args.data_path}")
    print("=" * 50)
    
    # Set experiment name (tanpa tracking URI agar flexible)
    mlflow.set_experiment("Telco_Churn_CI_Training")
    
    # Load preprocessed data
    df = pd.read_csv(args.data_path)
    print(f"\nDataset loaded: {len(df)} rows, {len(df.columns)} columns")
    
    # Split features and target
    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Train size: {len(X_train)}, Test size: {len(X_test)}")
    
    # Start MLflow run dengan nama yang descriptive
    run_name = f"RF_estimators{args.n_estimators}_depth{args.max_depth}"
    
    with mlflow.start_run(run_name=run_name):
        # Log hyperparameters
        mlflow.log_param("n_estimators", args.n_estimators)
        mlflow.log_param("max_depth", args.max_depth)
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("random_state", 42)
        
        # Train model dengan parameter dari CLI
        model = RandomForestClassifier(
            n_estimators=args.n_estimators,
            max_depth=args.max_depth if args.max_depth > 0 else None,
            random_state=42,
            n_jobs=-1
        )
        
        print("\nTraining model...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        # Log metrics ke MLflow
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)
        
        # Log model artifact
        mlflow.sklearn.log_model(model, "model")
        
        # Print results
        print("\n" + "=" * 50)
        print("EVALUATION METRICS")
        print("=" * 50)
        print(f"Accuracy:  {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")
        print(f"F1 Score:  {f1:.4f}")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        print("\n✅ Training completed and logged to MLflow!")
        print(f"Run name: {run_name}")

if __name__ == "__main__":
    main()
