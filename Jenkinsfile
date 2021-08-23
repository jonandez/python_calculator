pipeline {
    agent any
    // tools {
    //     terraform 'terraform'
    // }
    
    environment {
        DOCKERHUB_CREDENTIALS_PASSWS = credentials('dockerhub')
    }

    stages {
        stage ("checkout from git"){
            steps {
                git 'https://github.com/jonandez/python_calculator.git'
            }
        }
        stage ("docker build image") {
            steps {
                sh "docker build -t josegrelnx/python-calc:latest ."
            }
        }
        stage ("docker login") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER')]) {
                    sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USER} --password-stdin"
                }                
            }
        }
        stage ("docker push") {
            steps {
                sh "docker push josegrelnx/python-calc:latest"
            }
        }
        stage ("docker logout") {
            steps {
                sh "docker logout"
            }
        }
    }
}