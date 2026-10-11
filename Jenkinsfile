pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out project source'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'python -m pip install flask'
            }
        }

        stage('Test') {
            steps {
                sh 'python - <<\'PY\'\nfrom app import app\nclient = app.test_client()\nresponse = client.post("/", data={"num1": "10", "num2": "5", "operation": "add"})\nassert response.status_code == 200\nassert "15.0" in response.get_data(as_text=True) or "15" in response.get_data(as_text=True)\nprint("Calculator test passed")\nPY'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Application is ready to be deployed'
            }
        }
    }
}
