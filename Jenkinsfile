pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = 'divyasri02'
        DOCKERHUB_PASSWORD = '102@TVLDr'
        IMAGE_NAME = 'house-price-predictor'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    bat 'git config --global http.sslVerify false'
                    git branch: 'main', url: 'https://github.com/tdivyasri/House-price-predictor.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    bat """
                    echo ${DOCKERHUB_PASSWORD} | docker login -u ${DOCKERHUB_USERNAME} --password-stdin
                    """
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    bat "docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    bat """
                    docker pull ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker ps -q -f name=house-container | findstr house-container && docker rm -f house-container || echo 'No existing container to remove'
                    docker run -d -p 5000:5000 --name house-container ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker logs house-container  # Check logs for errors
                    docker ps -a  # List containers to ensure it's running
                    """
                }
            }
        }
    }
}
