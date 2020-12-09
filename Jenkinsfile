node {

    stage("Checkout repo") {
        git branch: 'master',
        url: 'https://github.com/alex-radchenko-github/page_object_example'
    }
    stage("test") {
        sh '/usr/local/bin/pytest'
    }
    stage("report") {
        script {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure_result']]
                ])
        }
    }
}