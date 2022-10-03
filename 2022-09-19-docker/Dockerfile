FROM dolfinx/lab:v0.5.1

WORKDIR /tmp/

ADD requirements.txt /tmp/requirements.txt

ENV HDF5_MPI="ON" HDF5_DIR="/usr/local/" CC="mpicc"

RUN pip3 install pandas
RUN pip3 install --no-cache-dir -r requirements.txt --upgrade &&\
    pip3 cache purge

RUN python3 -c "import h5py; print(h5py.__version__)"
ENTRYPOINT ["jupyter", "lab", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]