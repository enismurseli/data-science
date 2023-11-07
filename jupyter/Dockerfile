# Use a lightweight Jupyter Notebook image as a base image
FROM jupyter/minimal-notebook:latest

# Install required Python packages (you can customize this)
RUN pip install cassandra-driver redis

# Expose the Jupyter notebook port
EXPOSE 8888

# Set the working directory for Jupyter notebooks
WORKDIR /notebooks

# Start Jupyter notebook with required environment variables
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--NotebookApp.token=''"]