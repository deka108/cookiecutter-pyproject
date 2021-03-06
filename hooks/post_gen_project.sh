#!/usr/bin/env bash

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`
bold=`tput bold`

replace_dotenvfile(){
    sed -ie "s@PROJECT_HOME=.*@PROJECT_HOME=$(pwd)@" "${1}"
    sed -ie "s@PROJECT_CONFIG=.*@PROJECT_CONFIG=$(pwd)/config/config.yaml@" "${1}"
    rm "${1}e"
}

# Replace .env
cp .env-template .env
replace_dotenvfile ".env"

# Create dirs
mkdir -p tmp
