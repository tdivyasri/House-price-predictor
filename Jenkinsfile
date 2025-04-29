pipeline {
    agent any

    environment {
        // Define Docker Hub credentials (replace with your Docker Hub username and password)
        DOCKERHUB_USERNAME = 'divyasri02'
        DOCKERHUB_PASSWORD = '102@TVLDr'
        IMAGE_NAME = 'house-price-predictor'  // Change to your image name
        IMAGE_TAG = 'latest'  // Or any version tag you want
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pull the latest code from GitHub repository
                git 'https://github.com/tdivyasri/House-price-predictor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image from Dockerfile
                    bat 'docker build -t %DOCKERHUB_USERNAME%/%IMAGE_NAME%:%IMAGE_TAG% .'
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub
                    bat '''echo %DOCKERHUB_PASSWORD% | docker login -u %DOCKERHUB_USERNAME% --password-stdin'''
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    bat 'docker push %DOCKERHUB_USERNAME%/%IMAGE_NAME%:%IMAGE_TAG%'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Pull the latest image (just to be sure the latest one is pulled)
                    bat 'docker pull %DOCKERHUB_USERNAME%/%IMAGE_NAME%:%IMAGE_TAG%'

                    // Run the Docker container
                    bat 'docker run -d -p 5000:5000 --name house-container %DOCKERHUB_USERNAME%/%IMAGE_NAME%:%IMAGE_TAG%'
                }
            }
        }
    }

    post {
        always {
            // Cleanup: Remove the Docker container if it exists
            bat 'docker rm -f house-container || true'

            // Remove the Docker image if needed
            bat 'docker rmi -f %DOCKERHUB_USERNAME%/%IMAGE_NAME%:%IMAGE_TAG% || true'
        }
    }
}
