BUILD_ENV=${1:-dev}
VALUES_FILE=values-$BUILD_ENV.yaml

helm uninstall test

# helm lint . -f $VALUES_FILE

# helm template test . -f $VALUES_FILE

# helm install test . -f $VALUES_FILE --dry-run

# helm install test . -f $VALUES_FILE

helm upgrade --install test . -f $VALUES_FILE
