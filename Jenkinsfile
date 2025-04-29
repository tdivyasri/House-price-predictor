pipeline {
    agent any

    environment {
        IMAGE_NAME = 'house-price-predictor'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/tdivyasri/House-price-predictor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t divyasri02/%IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat 'echo %PASSWORD% | docker login -u %USERNAME% --password-stdin'
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                bat 'docker push divyasri02/%IMAGE_NAME%:%IMAGE_TAG%'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker pull divyasri02/%IMAGE_NAME%:%IMAGE_TAG%'
                bat 'docker run -d -p 5000:5000 --name house-container divyasri02/%IMAGE_NAME%:%IMAGE_TAG%'
            }
        }
    }

    post {
        always {
            bat 'docker rm -f house-container || true'
            bat 'docker rmi -f divyasri02/%IMAGE_NAME%:%IMAGE_TAG% || true'
        }
    }
}
