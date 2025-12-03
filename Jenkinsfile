pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git credentialsId: 'github-token', url: 'https://github.com/insane-avi/app_launch.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cicdapp:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f cicdapp || true
                docker run -d --name cicdapp -p 8081:8081 cicdapp:latest
                '''
            }
        }
    }
}
