pipeline{
    agent any
    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "llmopsaiops"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }
    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(
                        branches: [[name: '*/main']], 
                        extensions: [], 
                        userRemoteConfigs: [[credentialsId: 'Github_Token', url: 'https://github.com/Adnan-edu/mlops_project_1.git']]
                    )
                }
            }
        }

        stage('Setting up our Virtual Environment and Installing dependencies'){
            steps{
                script{
                    echo 'Setting up our Virtual Environment and Installing dependencies............'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Building and Pushing Docker Image to GCR'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and Pushing Docker Image to GCR.............'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker --quiet

                        # Use Docker Buildx to build multi-arch image for Cloud Run (x86_64)
                        docker buildx create --use
                        docker buildx build --platform linux/amd64 \
                            -t gcr.io/${GCP_PROJECT}/ml-project:latest \
                            --push .
                        '''
                    }
                }
            }
        }

        stage('Deploy to Google Cloud Run'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Deploy to Google Cloud Run.............'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}

                        gcloud run deploy ml-project \
                            --image=gcr.io/${GCP_PROJECT}/ml-project:latest \
                            --platform=managed \
                            --region=us-central1 \
                            --allow-unauthenticated \
                            --timeout 15m \
                            --memory=2Gi \
                            --cpu=2
                        '''
                    }
                }
            }
        }        
    }
}
