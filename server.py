import socket
import qiskit as q
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram

"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
"""
message = 'Hello World'

message_bin = ''.join(format(ord(i), 'b') for i in message)
print(message_bin)


circuit = q.QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
simulator = q.Aer.get_backend('statevector_simulator')
result = q.execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
print(statevector)
circuit.draw()

"""
while True:
    clientsocket, address = s.accept()
    print("Connection established to {}".format(address))
    clientsocket.send(bytes("Hello World", "utf-8"))
    clientsocket.close()
"""