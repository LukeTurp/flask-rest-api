#!/usr/bin/env python3

from hash_api.base import app, config

if __name__ == '__main__':
    app.run(host=config.host, port=config.port, debug=config.debug)
