import setuptools
from pathlib import Path
import re

# 读取 __version__ 和 __release_date__ 自动填入
init_file = Path("dvrctl") / "__init__.py"
content = init_file.read_text()
version_match = re.search(r'__version__\s*=\s*"(.+?)"', content)
release_date_match = re.search(r'__release_date__\s*=\s*"(.+?)"', content)

version = version_match.group(1) if version_match else "0.0.1"
release_date = release_date_match.group(1) if release_date_match else "Unknown"

# 读取 README.md
long_description = Path("README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="dvrctl",
    version=version,
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=[
        # 你的依赖库，例如 "requests>=2.0"
    ],
    description="DaVinci Resolve Control Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LoveinYuu/dvrctl",
    author="LoveinYuu",
    author_email="purewhite820@gmail.com",
    license="Proprietary",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
