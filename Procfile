web: gunicorn --worker-tmp-dir /dev/shm --config gunicorn_config.py app:app && ./stockfish_permission.sh
release: chmod u+x stockfish_permission.sh && ./stockfish_permission.sh
