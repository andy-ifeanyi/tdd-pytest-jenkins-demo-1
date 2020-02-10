pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage ('Git checkout') {
            steps {
                git 'https://github.com/andy-ifeanyi/tdd-pytest-jenkins-demo-1.git'

            }
        }
        stage ('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh "python palindrome.py"
                sh "python leapyear.py"
            }
        }
        stage ('test') {
            steps {
                sh "pytest -v"
            }
        }
        stage ('deploy'){
            steps {
                echo 'application built, tested, and deployed successfully.'
            }
        }
    }
    post {
        always {
            junit 'test-reports/*.xml'
            echo 'This message will always be displayed irrespective of outcome.'
        }
    }
}