
# Collaborative Filtering

	1. Collaborative filtering: 
	
		a. models that use data based on users' similarity
		b. Behavioral based model

    There are 2 methods of collaborative filtering discussed here:
    1. Matix Factorisation
    2. Using K-Nearest-Neighbours



## Matrix Factorization

    <img width="1280" height="599" alt="Image" src="https://github.com/user-attachments/assets/f721b150-4fe2-4a1c-8c61-c3955abb4ffd" />
    <img width="1762" height="627" alt="Image" src="https://github.com/user-attachments/assets/ee6997e3-2c21-4269-9d6b-d6c4216e23ad" />
    This algorithm uses SVD
    <img width="1577" height="828" alt="Image" src="https://github.com/user-attachments/assets/e97c8f5a-c94a-4ebb-a27b-7eba914579cc" />


## Using K-Nearest-Neighbours

    <img width="1671" height="815" alt="Image" src="https://github.com/user-attachments/assets/a21a712c-7329-49c8-8ca8-dbfe70ca1ed4" />

    In KNN we have further 2 methods:

    <img width="1033" height="1026" alt="Image" src="https://github.com/user-attachments/assets/df9b2176-9271-4cc2-83b6-03304185b7c8" />

## Experiments

    This directory contains code for collaborative filtering 
    - Using K-Nearest-Neighbours for user based method
    - Using K-Nearest-Nearest-Neighbours for item based method
    - Using Matrix Factorisation (SVD)

## Tech stack used
    - numpy
    - pandas
    - mlflow
    - surprise


## Dataset
MovieLens Dataset

## Evaluation metrics
- Mean Absolute Error
- Root Mean Square Error

## Steps to setup


1. Setup python virtual environment.
`python -m venv myenv` 

`myenv\Scripts\activate` 

`pip install -r requirements.txt`

2. To run MLFlow UI:
`mlflow UI`

`Click on http://127.0.0.1:5000/`

3. On terminal,

`python main.py`

## Results
<img width="1629" height="454" alt="Image" src="https://github.com/user-attachments/assets/196f76a6-42e0-45de-b6c6-cce7c20b8453" />






    




