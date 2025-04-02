# Dynamic Resource Allocation in Crisis Management

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This project addresses the critical challenge of efficient and timely resource allocation during crises (floods, storms, etc.). Existing systems often suffer from delays and lack real-time integration of multiple data sources. This AI-driven system dynamically processes and analyzes crisis text data (social media posts, tweets) and weather event data to predict resource requirements and streamline allocation.

## Problem Addressed

Inefficient and delayed resource allocation during crises.

Lack of real-time integration of multiple data sources.

Difficulty in identifying and prioritizing the needs of affected areas.

The need for a system that dynamically processes, analyzes, and predicts resource requirements.

## Proposed Solution

This project integrates crisis text data and weather event data. It uses AI and machine learning models classify data and uses weather event data to inform resource allocation effectively.

## Key Features

*   **Real-time Data Integration:** Utilizes real-time data from Twitter, OpenWeatherMap API.
*   **AI-Powered Classification:** Employs a Gradient Boosting Classifier for accurate classification of text data.
*   **Dynamic Prioritization:** Suggests and prioritizes resource allocation based on classified data and weather severity.

## Workflow

1.  **Data Collection:** Gathers crisis text data (social media posts, tweets) and weather event data.

2.  **Preprocessing:** Cleans text data using natural language processing techniques and standardizes weather data.

3.  **Feature Engineering:** Extracts key features such as informativeness, type of information, and weather severity.

4.  **Model Training:** Trains a Gradient Boosting Classifier to classify informativeness and crisis types.

5.  **Integration:** Merges predictions with weather event data.

6.  **Dynamic Resource Allocation:** Provides resource allocation suggestions based on classified data.

## Results

*Example:*

*   **Message:** "Flooding in City A, need immediate rescue teams and food supplies!"
*   **Analysis:**
    *   Classified as "Informative" and "Rescue Information."
    *   Linked with weather data (e.g., weather severity: High).
    *   Suggested priority: High → Allocate rescue teams and food supplies to City A.

## Technologies Used

*   **Python:** primary programming language.
*   **TensorFlow:** Building and training.
*   **OpenWeatherMap API:** weather data.
*   **Twitter API:** social media sentiment extraction.
*   **Pandas:** data manipulation.
*   **Scikit-learn:** machine learning algorithms.

## Setup and Installation

1.  Clone this repository:

    ```
    git clone https://github.com/tanmay-1620/Btech-Project.git
    cd Btech-Project/ResourceAllocation
    ```

2.  Install dependencies:

    ```
    pip install tensorflow pandas tweepy scikit-learn
    ```

3.  Obtain API keys:

    *   Create an account on [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.
    *   Create a Twitter developer account and obtain API keys.

4.  Configure API keys:

    *   Create a `config.py` file:

    ```
    OPENWEATHERMAP_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
    TWITTER_API_KEY = "YOUR_TWITTER_API_KEY"
    TWITTER_API_SECRET = "YOUR_TWITTER_API_SECRET"
    ```

## How to Run

1.  Run the main script:

    ```
    python main.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Tanmay Amrutkar

*   Email: [tanmay.amrutkar16@gmail.com](mailto:tanmay.amrutkar16@gmail.com)
*   LinkedIn: [linkedin.com/in/tanmay-amrutkar](https://www.linkedin.com/in/tanmay-amrutkar)
*   GitHub: [github.com/tanmay-1620](https://github.com/tanmay-1620)

