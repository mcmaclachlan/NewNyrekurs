import uuid
c.ConfigurableHTTPProxy.auth_token = str(uuid.uuid4())
voila_service_dict = {
                        'PROXY_TOKEN': c.ConfigurableHTTPProxy.auth_token,
                        'PROXY_API_URL': 'http://%s:%d/' % ("127.0.0.1", 8082)
                    }
voila_service_dict.update(os.environ)
c.JupyterHub.services = [
                            {
                                'name': 'voila',
                                'command': ['bash', '-c', 'jupyter_voila_service'],
                                'environment': voila_service_dict
                            }
                        ]
