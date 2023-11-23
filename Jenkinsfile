pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run API Test') {
            steps {
                sh 'python api_test.py'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf venv'
        }
    }
}
