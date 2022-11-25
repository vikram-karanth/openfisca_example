# Install the base requirements for the app.
# This stage is to support development.
FROM python:3.7 AS base
WORKDIR /openfisca
SHELL ["/bin/bash", "-c"]

RUN git clone https://github.com/openfisca/openfisca-core.git
# RUN git clone https://github.com/openfisca/country-template.git
# RUN git clone https://github.com/Openfisca-NSW/openfisca_nsw_community_gaming.git
COPY country-template ./country-template
COPY extension-template ./extension-template

RUN python3 -m venv .venv
RUN source .venv/bin/activate

# Change to /openfisca-core
WORKDIR /openfisca/openfisca-core
RUN make install

WORKDIR /openfisca/country-template
RUN make install

WORKDIR /openfisca/extension-template
RUN make install

WORKDIR /openfisca
EXPOSE 5000
# RUN openfisca serve --country-package openfisca_nsw_base --extensions openfisca_nsw_community_gaming --port 4000 --bind 0.0.0.0:4000
CMD ["openfisca", "serve", "--country-package", "openfisca_country_template", "--extensions", "openfisca_extension_template", "--port", "5000", "--bind", "0.0.0.0:5000"]
# cd ..

# CMD ["openfisca", "serve", "-a", "0.0.0.0:8000"]
# openfisca serve --country-package openfisca_nsw_base --extensions openfisca_nsw_community_gaming --port 2000 --bind 0.0.0.0:2000

