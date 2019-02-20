FROM ubuntu:bionic

# install latest python and nodejs
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

# add yarn ppa
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python2.7 \
    python-pip \
    git \
    git-lfs \
    nodejs=6.14.1-1nodesource1 \
    yarn \
    gettext \
    python-sphinx

# https://github.com/git-lfs/git-lfs/wiki/Installation#docker-recipes
RUN build_deps="curl" && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ${build_deps} ca-certificates && \
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends git-lfs && \
    git lfs install && \
    DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove ${build_deps} && \
    rm -r /var/lib/apt/lists/*

RUN git lfs install

COPY . /kolibri

VOLUME /kolibridist/  # for mounting the whl files into other docker containers
# add buildkite pipeline specific installation here:
CMD cd /kolibri && pip install -r requirements/dev.txt && pip install -r requirements/build.txt && pip install -e . && yarn install && make dist pex && cp /kolibri/dist/* /kolibridist/
