import cirq

# 2 qubits:
(q0, q1) = cirq.LineQubit.range(2)

circuit = cirq.Circuit()
circuit.append([cirq.H(q0), cirq.CNOT(q0, q1)])
circuit.append([cirq.measure(q0), cirq.measure(q1)])
print('Circuit:')
print(circuit)

print()

simulation = cirq.Simulator()
results = simulation.run(circuit, repetitions=10)
print('Results:')
print(results)
