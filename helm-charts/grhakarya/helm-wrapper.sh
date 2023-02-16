BUILD_ENV=${1:-dev}
VALUES_FILE=values-$BUILD_ENV.yaml

echo "Deleting chart, please wait..."
helm uninstall --wait grahakarya

# helm lint --debug . --strict --values $VALUES_FILE

# helm template grahakarya . -f $VALUES_FILE

# helm install grahakarya . -f $VALUES_FILE --dry-run

# helm install grahakarya . -f $VALUES_FILE

# helm upgrade --install --wait grahakarya .

# kubectl get svc -A

