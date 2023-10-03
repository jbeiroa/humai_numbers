#!/usr/bin/env sh

# define any environment variables here
export MY_ENV_VAR="some value"

# run the app
uvicorn --log-config logging.conf --host 0.0.0.0 --port 8000 "app.core.main:app" --reload 
