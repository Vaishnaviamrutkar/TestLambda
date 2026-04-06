name: Deploy Lambda

on:
  push:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Workflow working"