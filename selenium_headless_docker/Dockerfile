FROM selenium/standalone-chrome

RUN sudo apt-get update && sudo apt-get install -yq \
    python3 \
    python3-pip \
    git

RUN python3 -m pip install selenium

# Write the test
RUN mkdir ~/test
RUN git clone https://github.com/vrac-demo/codestream-demos ~/test

# Smoke test (should be google.org)
RUN echo "Starting smoke test..."
RUN python3 ~/test/cicd_scripts/seleniumTestTitle.py
RUN echo "...done"
