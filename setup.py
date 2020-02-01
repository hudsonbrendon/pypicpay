from setuptools import setup

from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="picpay-python",
    version="0.3",
    description="Aceite PicPay e faça parte do movimento que está revolucionando a relação com o dinheiro no Brasil.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/hudsonbrendon/picpay-python",
    author="Hudson Brendon",
    author_email="contato.hudsonbrendon@gmail.com",
    license="MIT",
    packages=["picpay"],
    install_requires=["requests",],
    zip_safe=False,
)
