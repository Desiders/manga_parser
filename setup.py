from setuptools import find_packages, setup

setup(
    name="manga_parser",
    description="Convenient manga parser!",
    version="0.2.0",
    url="https://github.com/Desiders/manga_parser",
    author="Desiders",
    license="Apache2",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    project_urls={
        "Source": "https://github.com/Desiders/manga_parser",
    },
    packages=find_packages(include=['manga_parser', 'manga_parser.*']),
    install_requires=[
        'httpx>=0.19.0,<1.0.0',
        'beautifulsoup4>=4.9.3',
        'lxml>=4.6.3',
        'pydantic>=1.8.2,<2.0.0',
    ],
    python_requires=">=3.5",
)
