properties([parameters([choice(choices: 'apply\ndelete', name: 'action')])])

pipeline {
    agent any
    
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
        stage ("Deploy app to EKS") {
            steps {
                sh "aws eks update-kubeconfig --name eks_cluster --region us-east-1"
                sh "kubectl ${params.action} -f manifest.yaml" 
            }           
        }
        
        stage ("docker logout") {
            steps {
                sh "docker logout"
            }
        }
    }
}