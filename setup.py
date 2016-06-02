from setuptools import setup

setup(name = 'jinjaStore',
        version = "0.1",
        description = "Jinja Store for Templating",
        author = "The Binary",
        author_email = "binary4bytes@gmail.com",
        url = "https://github.com/thebinary/jinjaStore",
        packages = ['jinjaStore'],
        package_data = {
                'jinjaStore': [ '*.jinja2' ]
            },
        install_requires = ['jinja2'],
        long_description = "Maintain Store of Jinja Templates for rendering",
        )
        
