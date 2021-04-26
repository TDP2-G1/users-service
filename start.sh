#!/usr/bin/env bash
waitress-serve --port $PORT --call "usersServiceApp:create_app"
