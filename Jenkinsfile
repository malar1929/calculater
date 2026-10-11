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
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Validate App') {
            steps {
                bat 'python -c "from app import app; client = app.test_client(); response = client.post(\'/\', data={\'num1\': \'10\', \'num2\': \'5\', \'operation\': \'add\'}); assert response.status_code == 200; assert \'15.0\' in response.get_data(as_text=True) or \'15\' in response.get_data(as_text=True)"'
            }
        }
    }

    post {
        success {
            echo 'Build Successful'
        }

        failure {
            echo 'Build Failed'
        }
    }
}
