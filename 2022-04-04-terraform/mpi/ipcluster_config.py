import os
import sys

# ensure $PREFIX/bin is on $PATH
sys_bin = os.path.join(sys.prefix, "bin")
path = os.environ["PATH"]
if sys_bin not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] = sys_bin + os.pathsep + os.environ["PATH"]

# load host keys
# from subprocess import check_output
#
# known_hosts = os.path.expanduser("~/.ssh/known_hosts")
#
# machinefile = "/shared/machinefile"
# hosts = []
# with open(machinefile) as f:
#     for line in f:
#         hosts.append(line.split(":", 1)[0])
#
# # trust host keys
# key_scan = check_output(["ssh-keyscan"] + hosts)
# with open(known_hosts, "ab") as f:
#     f.write(key_scan)


c = get_config()  # noqa

c.Cluster.engine_launcher_class = "MPI"
c.Cluster.MPIEngineSetLauncher.mpi_cmd = [
    "mpiexec",
    "-machinefile",
    "/shared/machinefile",
]
