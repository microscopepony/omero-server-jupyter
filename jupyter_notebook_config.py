# Configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'omeroweb': {
        'command': ['/home/jovyan/omero-web-proxy.sh', '{port}', '{base_url}'],
        'timeout': 60,
        'launcher_entry': {
            'enabled': True,
        },
    },
}