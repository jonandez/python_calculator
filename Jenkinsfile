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
    stage ("cat dockerfile"){
            steps {
                sh "ls -ltr"
            }
        }
        stage ("docker build image") {
            steps {
                sh "docker build -t josegrelnx/python-calc:latest ."
            }
        }
        stage ("docker login") {
            steps {
                sh "echo $DOCKERHUB_CREDENTIALS | docker login -u josegrelnx --password-stdin"
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