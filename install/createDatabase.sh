#!/usr/bin/env bash
echo "Creating database..."
createuser -s covercore || :
createdb -O covercore covercore || :