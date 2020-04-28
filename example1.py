import cirq

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)
print('Circuit:')
print(circuit)

print()

# Simulate the circuit several times.
simulator = cirq.Simulator()
results = simulator.run(circuit, repetitions=20)
print('Results:')
print(results)
