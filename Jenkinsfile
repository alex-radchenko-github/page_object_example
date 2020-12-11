node {

    stage("Checkout repo") {
        git branch: 'master',
        url: 'https://github.com/alex-radchenko-github/page_object_example'
    }
    stage("requirements") {
        sh '/usr/local/bin/pip3.9 install -r requirements.txt'
    }
    stage("test") {
        sh '/usr/local/bin/pipenv run /usr/local/bin/pytest Tests --br_type=chrome --selenoid=serv -sv --alluredir=allure_result'
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
