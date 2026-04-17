from setuptools import setup, find_packages

setup(
    name='airline-booking-price-prediction',
    version='1.0.0',
    description='ML model for predicting airline booking prices',
    author='Data Science Team',
    author_email='support@example.com',
    url='https://github.com/yourusername/airline-booking-price-prediction',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'pandas>=1.5.0',
        'numpy>=1.23.0',
        'scikit-learn>=1.1.0',
        'xgboost>=1.7.0',
        'matplotlib>=3.5.0',
        'seaborn>=0.12.0',
        'jupyter>=1.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'black>=22.0',
            'flake8>=4.0',
            'mypy>=0.900',
        ],
        'deploy': [
            'flask>=2.0',
            'gunicorn>=20.0',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
