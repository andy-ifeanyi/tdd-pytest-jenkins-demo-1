pipeline {
    agent any 
    stages {
        stage ('Git checkout') {
            step {
                git 'https://github.com/andy-ifeanyi/tdd-pytest-jenkins-demo-1.git'

            }
        }
        stage ('build') {
            step {
                sh "python palindrome.py"
                sh "python leapyear.py"
            }
        }
        stage ('test') {
            step {
                sh "pytest -v"
            }
        }
        stage ('deploy'){
            echo 'application built, tested, and deployed successfully.'
        }
    }
    post {
        always {
            junit 'test-reports/*.xml'
            echo 'This message will always be displayed irrespective of outcome.'
        }
    }
}