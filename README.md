# NBA Career Longevity Predictor

A machine learning project that predicts whether an NBA rookie will have a career lasting more than 5 years, based on their debut season statistics. This project demonstrates end-to-end data science skills including exploratory data analysis, model selection, training, evaluation, and deployment via REST API.

## Project Overview

This project addresses a real-world investment scenario: helping sports investors identify promising NBA rookies worth investing in for long-term sponsorships and partnerships. By analyzing debut season performance metrics, the classifier predicts career longevity with a focus on maximizing recall to avoid missing potential stars.

### Business Context

The model is designed to advise investors seeking to capitalize on future NBA talents by predicting whether a rookie player will sustain a career of 5+ years based on their first-season statistics. The emphasis is on identifying promising players early in their careers.

## Dataset

The dataset ([data/nba_logreg.csv](data/nba_logreg.csv)) contains statistics for NBA rookie players with the following features:

| Feature | Description |
|---------|-------------|
| Name | Player name |
| GP | Games Played |
| MIN | Minutes Played |
| PTS | Points Per Game |
| FGM | Field Goals Made |
| FGA | Field Goal Attempts |
| FG% | Field Goal Percent |
| 3P Made | 3-Point Field Goals Made |
| 3PA | 3-Point Attempts |
| 3P% | 3-Point Percentage |
| FTM | Free Throws Made |
| FTA | Free Throw Attempts |
| FT% | Free Throw Percentage |
| OREB | Offensive Rebounds |
| DREB | Defensive Rebounds |
| REB | Total Rebounds |
| AST | Assists |
| STL | Steals |
| BLK | Blocks |
| TOV | Turnovers |
| **TARGET_5Yrs** | **Target variable: 1 if career >= 5 years, 0 otherwise** |

## Project Structure

```
.
├── data/
│   ├── nba_logreg.csv                # Dataset with NBA rookie statistics
│   └── players_classifier.pkl        # Trained model (serialized)
├── notebooks/
│   └── classifiers.ipynb             # Jupyter notebook with full ML pipeline
├── python/
│   ├── api.py                        # FastAPI REST API for predictions
│   └── client.py                     # Example client to test the API
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

## Machine Learning Pipeline

### 1. Model Training & Validation

The complete analytical approach is documented in [notebooks/classifiers.ipynb](notebooks/classifiers.ipynb), including:

- **Exploratory Data Analysis (EDA)**: Understanding feature distributions, correlations, and class balance
- **Feature Engineering**: Selection and transformation of relevant statistics
- **Model Selection**: Comparison of multiple classifiers (Logistic Regression, Random Forest, etc.)
- **Hyperparameter Tuning**: Optimization using cross-validation
- **Model Evaluation**: Performance metrics with emphasis on recall (to minimize false negatives)
- **Model Export**: Final model saved as [data/players_classifier.pkl](data/players_classifier.pkl)

### 2. API Deployment

The trained classifier is deployed as a REST API using FastAPI ([python/api.py](python/api.py)), providing two functionalities:

1. **Query by player name**: Retrieve historical statistics for players in the dataset
2. **Predict career longevity**: Submit player statistics to get a prediction

## Installation & Setup

### Prerequisites

```bash
python 3.7+
pip install -r requirements.txt
```

### Required Dependencies

```
fastapi
uvicorn
pandas
numpy
scikit-learn==1.0.1
requests
jupyter
```

**Note**: The trained model was created with scikit-learn 1.0.1. Using a different version may produce warnings but should still work correctly. For production use, consider retraining the model with your current scikit-learn version.

## Usage

### Starting the API Server

Launch the FastAPI server from the project root directory:

```bash
uvicorn python.api:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### POST `/`

**Request Body:**

Option 1 - Query by name:
```json
{
  "name": "Malik Sealy"
}
```

Option 2 - Predict with statistics:
```json
{
  "GP": 58,
  "MIN": 11.6,
  "PTS": 5.7,
  "FGM": 2.3,
  "FGA": 5.5,
  "FTM": 0.9,
  "FTA": 1.3,
  "OREB": 1.0,
  "DREB": 0.9,
  "REB": 1.9,
  "AST": 0.8,
  "STL": 0.6,
  "BLK": 0.1,
  "TOV": 1.0
}
```

**Response:**
```json
{
  "prediction": 1,
  "prediction_proba": 0.87,
  "warnings": ""
}
```

- `prediction`: 1 = career will last 5+ years, 0 = career < 5 years
- `prediction_proba`: Confidence probability for the prediction
- `warnings`: Alerts for missing or zero-valued parameters

### Testing the API

Use the provided test client:

```bash
python python/client.py
```

This sends sample requests to the API and displays the responses.

### Interactive API Documentation

FastAPI provides automatic interactive documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Key Features

- **End-to-end ML pipeline**: From data exploration to production deployment
- **RESTful API**: Easy integration with any application or service
- **Robust error handling**: Warnings for invalid inputs and missing data
- **Model persistence**: Trained model saved for reproducible predictions
- **Interactive documentation**: Auto-generated API docs via FastAPI

## Technical Skills Demonstrated

- **Python**: Pandas, NumPy, Scikit-learn
- **Machine Learning**: Classification, model evaluation, hyperparameter tuning
- **API Development**: FastAPI, RESTful design, Pydantic validation
- **Data Analysis**: EDA, feature engineering, statistical analysis
- **Model Deployment**: Model serialization, serving predictions via HTTP
- **Software Engineering**: Modular code, documentation, testing

## Results & Model Performance

Detailed model performance metrics, including precision, recall, F1-score, and confusion matrix, are available in the [Jupyter notebook](notebooks/classifiers.ipynb). The model prioritizes recall to ensure promising players are not overlooked by investors.

## Future Improvements

- Add model monitoring and retraining pipeline
- Implement A/B testing for model versions
- Expand API with batch prediction endpoints
- Add authentication and rate limiting
- Deploy to cloud platform (AWS, GCP, Azure)
- Create frontend dashboard for predictions

## Author

**Pierre Dal Bianco**

This project was completed as part of a technical assessment and showcases practical data science and software engineering capabilities.

## License

This project is for portfolio and educational purposes.
