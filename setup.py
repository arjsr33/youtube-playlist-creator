from setuptools import setup, find_packages

setup(
    name='yt-playlist-creator',
    version='1.0.0',
    author='Arjun',
    description='A CLI tool to create a YouTube playlist from a text file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/arjsr33/yt-playlist-creator', 
    packages=find_packages(),
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib'
    ],
    entry_points={
        'console_scripts': [
            'create-playlist=yt_playlist_creator.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Multimedia :: Video',
        'Environment :: Console',
    ],
    python_requires='>=3.6',
)
