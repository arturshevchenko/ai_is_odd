from setuptools import setup, find_packages

setup(
    name="ai_is_odd",
    version="0.1.1",
    license='MIT',
    description="A super AI-powered library to determine if number is odd or odd with power of AI",
    author="Artur Shevchenko",
    author_email="artur.shev8@gmail.com",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/arturshevchenko/ai_is_odd",
    keywords=['AI', 'EVEN', 'ODD'],
    packages=find_packages(),
    install_requires=[
        "requests==2.32.3",
        "python-dotenv==1.0.1",
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "idna==3.10",
        "urllib3==2.2.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
