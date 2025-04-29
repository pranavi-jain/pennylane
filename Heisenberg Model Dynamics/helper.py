import pennylane as qml
import numpy as np


## Create the circuit to execute the time-evolution operator for TFIM for a given time-step

def evolution_circuit_TFIM(num_time_steps, Jx, hz, freq, delta_t, N):
    hbar = 0.658212     # defined in units: eV*fs
    
    # define rotation angles for gates in circuit
    psiX = -2.0 * Jx * delta_t / hbar
    for step in range(num_time_steps):
        t = (step + 0.5) * delta_t
        psiZ = -2.0 * hz * np.cos(2 * np.pi * freq * t) * delta_t / hbar
    
        # implement XX operator
        for q in range(0, N - 1):
            qml.Hadamard(q)
            qml.Hadamard(q + 1)
            qml.CNOT([q, q + 1])
            qml.RZ(psiX, q + 1)
            qml.CNOT([q, q + 1])
            qml.Hadamard(q)
            qml.Hadamard(q + 1)
    
        # implement Z operator
        for q in range(0, N):
            qml.RZ(psiZ, q)
    return


## Create the circuit to execute the time-evolution operator for XY model for a given time-step

def evolution_circuit_XY(num_time_steps, Jx, Jy, delta_t, N):
    hbar = 0.658212     # eV*fs
    
    # define rotation angles for gates in circuit
    psiX = -2.0*Jx*delta_t/hbar
    psiY = -2.0*Jy*delta_t/hbar

    for step in range(num_time_steps):
        # implement XX operator
        for q in range(0, N - 1):
            qml.Hadamard(q)
            qml.Hadamard(q + 1)
            qml.CNOT([q, q + 1])
            qml.RZ(psiX, q + 1)
            qml.CNOT([q, q + 1])
            qml.Hadamard(q)
            qml.Hadamard(q + 1)
        # implement YY operator
        for q in range(0, N-1):
            qml.RX(-np.pi/2, q)
            qml.RX(-np.pi/2,q+1)
            qml.CNOT([q,q+1])
            qml.RZ(psiY,q+1)
            qml.CNOT([q,q+1])
            qml.RX(np.pi/2, q)
            qml.RX(np.pi/2,q+1)
    return
