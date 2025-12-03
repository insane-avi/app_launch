pipeline {
    agent any

    environment {
        IMAGE_NAME = "cicdapp:latest"
        CONTAINER_NAME = "cicdapp"
        PORTS = "8081:8081"
    }

    stages {
        stage('Checkout') {
            steps {
                // Code is already fetched by Jenkins (Pipeline from SCM),
                // but this keeps it explicit and reuses the same config.
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Deploy Container') {
            steps {
                sh """
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p ${PORTS} ${IMAGE_NAME}
                """
            }
        }
    }
}
