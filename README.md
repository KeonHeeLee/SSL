# Simple naver talktalk

This repo is content that SSL related materials and actual application method explain for security report.
Although it is true that it implemented Naver-talktalk chatbot, it is also the right way to apply SSL certificates to flasks.

## How to set SSL

```python
if __name__ == "__main__":
    ssl_cert = '/etc/letsencrypt/live/<::url::>/fullchain.pem'
    ssl_key =  '/etc/letsencrypt/live/<::url::>/privkey.pem'
    contextSSL =  (ssl_cert, ssl_key)
    app.run(host='0.0.0.0', port=443, debug = True, ssl_context = contextSSL)
```

## How to run

```
$ sudo python3 server.py
```
