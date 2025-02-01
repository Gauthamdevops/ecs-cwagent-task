
FROM amazon/cloudwatch-agent:latest

# Set working directory (optional)
#WORKDIR /opt/

COPY ./cloudwatch-config.json /etc/cwagentconfig/config.json

# Set the entrypoint to use CloudWatch Agent's command line tool

ENV CW_CONFIG_CONTENT=file:/etc/cwagentconfig/config.json

# Define the default command
CMD ["amazon-cloudwatch-agent-ctl", "-a", "start", "-c", "file:/etc/cwagentconfig/config.json", "-s", "true"]


