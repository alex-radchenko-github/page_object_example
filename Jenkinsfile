node {

    stage("Checkout repo") {
        git branch: 'master',
        url: 'https://github.com/alex-radchenko-github/page_object_example'
    }
    stage("Install deps") {
        sh '/usr/local/bin/pipenv install'
    }

    stage("test") {
        sh '/usr/local/bin/pipenv run pytest -s -v --br_type=chrome --selenoid=serv TestSmokeTesting.py -sv --alluredir=allure_result'
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