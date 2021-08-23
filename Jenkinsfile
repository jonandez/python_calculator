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
                git 'https://github.com/jonandez/terra_kube_cluster.git'
            }
        }
    stage ("ccat dockerfile"){
            steps {
                sh "cat Dockerfile"
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