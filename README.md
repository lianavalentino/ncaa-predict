# NCAA Basketball Predictor

This application predicts the winner of NCAA basketball games based on historical data using a logistic regression model deployed in BigQuery ML.

## Features
- Predict game outcomes using team stats and historical data.
- Cloud-native application deployed on Google Cloud Platform (GCP).
- REST API served using Google App Engine.

## How to Use
1. **Deploy the App**:
   - Push your changes to the `main` branch to trigger deployment via GitHub Actions.
2. **API Endpoint**:
   - `/predict`: POST endpoint to get predictions.
   - Example Payload:
     ```json
     {
       "season": 2018,
       "team1": "Villanova",
       "team2": "Michigan"
     }
     ```

## Project Structure
- `app.py`: Flask app serving the API.
- `requirements.txt`: Python dependencies.
- `app.yaml`: App Engine configuration.
- `.github/workflows/deploy.yml`: GitHub Actions for CI/CD.

## Prerequisites
- GCP project with BigQuery, Cloud Storage, and App Engine enabled.
- Historical NCAA basketball data loaded into BigQuery.

## Deployment
- Continuous deployment via GitHub Actions.
