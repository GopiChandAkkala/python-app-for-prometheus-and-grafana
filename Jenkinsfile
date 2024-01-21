pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
       
    }

    stages {
        stage('Docker Build') {
            steps {
                sh 'docker build -t akkalagopi/python-app-monitoring:latest .'
            }
        }

        stage('Docker Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Docker Push') {
            steps {
                sh 'docker push akkalagopi/python-app-monitoring:latest'
            }
        }  
               
    }

    
}
