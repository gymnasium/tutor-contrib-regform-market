import io
import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "regform_market", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-regform-market",
    version=ABOUT["__version__"],
    url="https://github.com/gymnasium/tutor-contrib-regform-market",
    project_urls={
        "Code": "https://github.com/gymnasium/tutor-contrib-regform-market",
        "Issue tracker": "https://github.com/gymnasium/tutor-contrib-regform-market/issues",
    },
    license="AGPLv3",
    author="Gymnasium",
    author_email="help@thegymnasium.com",
    description="Gymnasium-specific Market field registration form extension for Tutor",
    long_description=load_readme(),
    long_description_content_type="text/x-rst",
    packages=['regform_market'],
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "tutor>=18.0.0,<19.0.0",
        "Django"
    ],
    extras_require={
        "dev": [
            "tutor[dev]>=18.0.0,<19.0.0",
        ]
    },
    entry_points={
        "tutor.plugin.v1": [
            "regform_market = regform_market.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
